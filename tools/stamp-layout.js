#!/usr/bin/env node
/* Estampa el encabezado y el pie compartidos en cada página pública.
   Uso:  node tools/stamp-layout.js            (todas las páginas de PAGES)
         node tools/stamp-layout.js a.html b/   (sólo esas)
   Fuente única: tools/layout/header.html y tools/layout/footer.html.
   Entre marcadores <!-- Q:HEADER --> … <!-- /Q:HEADER --> y <!-- Q:FOOTER --> … <!-- /Q:FOOTER -->
   el contenido se reemplaza en cada corrida; no edite a mano dentro de ellos.
   En páginas antiguas, la primera corrida reemplaza su menú y su pie propios. */
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const HEADER = fs.readFileSync(path.join(__dirname, 'layout', 'header.html'), 'utf8').trim();
const FOOTER = fs.readFileSync(path.join(__dirname, 'layout', 'footer.html'), 'utf8').trim();
const JS_FLAG = "<script>document.documentElement.classList.add('js')</script><!--q:js-->";
const COMMON = '<script src="/quorelia-common.js"></script><!--q:common-->';

const PAGES = [
  'index.html', 'plataforma.html', 'story.html', 'insights.html', 'demos.html', 'gobierno.html',
  'informe.html', 'agenda.html', 'normativa-electrica-chile.html', 'privacidad.html', 'terminos.html',
  'servicios/index.html',
  'servicios/gestion-de-activos/index.html', 'servicios/verificacion/index.html',
  'servicios/operacion-y-mantenimiento/index.html', 'servicios/solar-y-baterias/index.html',
  'servicios/reemplazo-diesel/index.html', 'servicios/ingenieria/index.html',
  'industrias/propietarios-renovables/index.html', 'industrias/mineria/index.html',
  'industrias/agricultura/index.html', 'industrias/alimentos-cadena-de-frio/index.html',
  'industrias/acuicultura-pesca/index.html', 'industrias/industria/index.html',
  'contacto/index.html',
];

function stamp(rel) {
  const file = path.join(ROOT, rel);
  if (!fs.existsSync(file)) return `${rel}: skipped (missing)`;
  let s = fs.readFileSync(file, 'utf8');
  const notes = [];

  // 1 · bandera js en el <head> (el revelado sólo oculta contenido si hay JS)
  if (!s.includes('<!--q:js-->')) {
    const before = s;
    s = s.replace(/(<meta\s+charset=["']?[^"'>\s]*["']?\s*\/?>)/i, `$1\n${JS_FLAG}`);
    notes.push(s !== before ? 'js-flag' : 'js-flag(NOT FOUND: add <meta charset> to <head>)');
  }

  // 2 · encabezado
  const hBlock = `<!-- Q:HEADER -->\n${HEADER}\n<!-- /Q:HEADER -->`;
  if (/<!-- Q:HEADER -->[\s\S]*?<!-- \/Q:HEADER -->/.test(s)) {
    s = s.replace(/<!-- Q:HEADER -->[\s\S]*?<!-- \/Q:HEADER -->/, () => hBlock);
    notes.push('header');
  } else {
    const body = s.search(/<body[^>]*>/i);
    const endHeader = s.indexOf('</header>');
    const candidates = ['<!-- menú móvil -->', '<div class="scrim"', '<aside class="drawer"', '<header']
      .map(m => s.indexOf(m, body)).filter(i => i > -1);
    const start = candidates.length ? Math.min(...candidates) : -1;
    if (start > -1 && endHeader > start) {
      s = s.slice(0, start) + hBlock + s.slice(endHeader + '</header>'.length);
      notes.push('header(replaced old)');
    } else {
      s = s.replace(/(<body[^>]*>)/i, `$1\n${hBlock}`);
      notes.push('header(inserted)');
    }
  }

  // 3 · pie
  const fBlock = `<!-- Q:FOOTER -->\n${FOOTER}\n<!-- /Q:FOOTER -->`;
  if (/<!-- Q:FOOTER -->[\s\S]*?<!-- \/Q:FOOTER -->/.test(s)) {
    s = s.replace(/<!-- Q:FOOTER -->[\s\S]*?<!-- \/Q:FOOTER -->/, () => fBlock);
    notes.push('footer');
  } else if (/<footer[\s\S]*?<\/footer>/.test(s)) {
    s = s.replace(/<footer[\s\S]*?<\/footer>/, () => fBlock);
    notes.push('footer(replaced old)');
  } else {
    s = s.replace(/<\/body>/i, `${fBlock}\n</body>`);
    notes.push('footer(inserted)');
  }

  // 4 · script común, al final (después del script propio de la página)
  if (!s.includes('<!--q:common-->')) {
    s = s.replace(/<\/body>/i, `${COMMON}\n</body>`);
    notes.push('common.js');
  }

  // 5 · destino del enlace "Saltar al contenido" en páginas antiguas sin <main id="main">
  if (!/id="main"/.test(s)) {
    const at = s.indexOf("<!-- /Q:HEADER -->");
    const i = s.indexOf("<section", at);
    if (i > -1) { s = s.slice(0, i) + '<span id="main" tabindex="-1"></span>\n' + s.slice(i); notes.push('main-anchor'); }
  }

  fs.writeFileSync(file, s);
  return `${rel}: ${notes.join(', ')}`;
}

const args = process.argv.slice(2);
const list = args.length ? args.map(a => a.endsWith('/') ? a + 'index.html' : a) : PAGES;
list.forEach(rel => console.log(stamp(rel)));
