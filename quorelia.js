/* ══════════════════════════════════════════════════════════════════════════
   QUORELIA — Comportamiento compartido
   Menú móvil accesible + revelado al hacer scroll.
   Ambos se activan solos si encuentran los elementos esperados en la página.
   ══════════════════════════════════════════════════════════════════════════ */

/* ── Menú móvil ─────────────────────────────────────────────────────────
   Panel lateral con foco atrapado, cierre con Escape, al tocar fuera y al
   elegir un enlace. Bloquea el scroll de fondo mientras está abierto. */
(function menuMovil(){
  var b = document.getElementById('burger'),
      d = document.getElementById('drawer'),
      s = document.getElementById('scrim'),
      c = document.getElementById('d-close'),
      last = null;
  if (!b || !d || !s) return;

  function abrir(){
    last = document.activeElement;
    d.hidden = false; s.hidden = false;
    requestAnimationFrame(function(){ d.classList.add('on'); s.classList.add('on'); });
    b.setAttribute('aria-expanded','true');
    document.body.classList.add('locked');
    var f = d.querySelector('nav a'); if (f) f.focus({preventScroll:true});
  }
  function cerrar(){
    d.classList.remove('on'); s.classList.remove('on');
    b.setAttribute('aria-expanded','false');
    document.body.classList.remove('locked');
    setTimeout(function(){ if(!d.classList.contains('on')){ d.hidden = true; s.hidden = true; } }, 330);
    if (last) last.focus({preventScroll:true});
  }

  b.addEventListener('click', function(){ d.classList.contains('on') ? cerrar() : abrir(); });
  s.addEventListener('click', cerrar);
  if (c) c.addEventListener('click', cerrar);
  d.querySelectorAll('nav a, .d-foot a').forEach(function(a){ a.addEventListener('click', cerrar); });

  document.addEventListener('keydown', function(e){
    if (!d.classList.contains('on')) return;
    if (e.key === 'Escape'){ cerrar(); return; }
    if (e.key !== 'Tab') return;
    var f = d.querySelectorAll('a[href], button:not([disabled])');
    if (!f.length) return;
    var primero = f[0], ultimo = f[f.length-1];
    if (e.shiftKey && document.activeElement === primero){ e.preventDefault(); ultimo.focus(); }
    else if (!e.shiftKey && document.activeElement === ultimo){ e.preventDefault(); primero.focus(); }
  });
  window.addEventListener('resize', function(){
    if (window.innerWidth > 1000 && d.classList.contains('on')) cerrar();
  });
})();

/* ── Video de fondo del hero ────────────────────────────────────────────
   Se activa si existe #hero-video. El póster y el fondo CSS quedan de
   respaldo mientras descarga y si el navegador no puede reproducirlo.
   En móvil y con reducción de movimiento no se descarga en absoluto. */
(function heroVideo(){
  var v = document.getElementById('hero-video');
  if (!v) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reduce || window.innerWidth < 720){
    v.removeAttribute('autoplay'); v.pause();
    var src = v.querySelector('source');
    if (src) src.removeAttribute('src');
    v.removeAttribute('src'); v.load();
    return;
  }
  v.addEventListener('canplay', function(){ v.classList.add('ready'); }, {once:true});
  v.addEventListener('error', function(){ v.style.display = 'none'; });

  if ('IntersectionObserver' in window){
    new IntersectionObserver(function(es){
      if (es[0].isIntersecting){ var p = v.play(); if (p && p.catch) p.catch(function(){}); }
      else v.pause();
    }, {threshold:0.01}).observe(v.parentNode);
  }
})();

/* ══════════════════════════════════════════════════════════════════════════
   MOVIMIENTO — sistema tipo Palantir
   ══════════════════════════════════════════════════════════════════════════ */
var REDUCE = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* 1 · Revelado por líneas
   Mide dónde parte cada línea de texto ya maquetada y la envuelve en una
   máscara, para que suba desde abajo. Se recalcula si cambia el ancho o
   el idioma, porque el quiebre de línea cambia con ambos. */
function partirEnLineas(el){
  if (REDUCE) return;
  if (!el.dataset.original) el.dataset.original = el.innerHTML;
  el.innerHTML = el.dataset.original;

  // envolver cada palabra para medir su posición vertical
  var walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null);
  var textos = [], n;
  while ((n = walker.nextNode())) textos.push(n);
  textos.forEach(function(t){
    if (!t.nodeValue.trim()) return;
    var frag = document.createDocumentFragment();
    t.nodeValue.split(/(\s+)/).forEach(function(p){
      if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(p)); return; }
      if (!p) return;
      var w = document.createElement('span');
      w.className = '_w'; w.textContent = p;
      frag.appendChild(w);
    });
    t.parentNode.replaceChild(frag, t);
  });

  // agrupar palabras por su coordenada superior = línea visual
  var lineas = [], actual = null, ultimoTop = null;
  el.querySelectorAll('._w').forEach(function(w){
    var top = Math.round(w.offsetTop);
    if (ultimoTop === null || Math.abs(top - ultimoTop) > 4){
      actual = []; lineas.push(actual); ultimoTop = top;
    }
    actual.push(w);
  });
  if (!lineas.length) return;

  // reconstruir: una máscara por línea
  var html = lineas.map(function(ws){
    var contenido = ws.map(function(w){
      // conservar el color de los <span> de énfasis
      var padre = w.parentElement;
      if (padre && padre !== el && padre.tagName === 'SPAN' && padre.className !== '_w'){
        return '<span class="' + padre.className + '" style="' + padre.getAttribute('style') + '">' + w.textContent + '</span>';
      }
      return w.textContent;
    }).join(' ');
    return '<span class="ln"><span>' + contenido + '</span></span>';
  }).join('');
  el.innerHTML = html;
  el.classList.add('reveal-lines');
}

(function revelarTitulares(){
  if (REDUCE) return;
  // Excluir titulares que contienen una palabra rotativa: partirlos en líneas
  // reconstruye el innerHTML y destruiría el rotor.
  var titulares = Array.prototype.filter.call(
    document.querySelectorAll('h1.mega, h2.big'),
    function(h){ return !h.querySelector('[data-rotor]'); }
  );
  if (!titulares.length) return;

  function preparar(){
    titulares.forEach(function(h){
      h.classList.remove('in');
      partirEnLineas(h);
    });
    var io = new IntersectionObserver(function(es, o){
      es.forEach(function(e){
        if (e.isIntersecting){ e.target.classList.add('in'); o.unobserve(e.target); }
      });
    }, { rootMargin:'0px 0px -6% 0px', threshold:0.1 });
    titulares.forEach(function(h){
      io.observe(h);
      if (h.getBoundingClientRect().top < window.innerHeight * 0.95) h.classList.add('in');
    });
  }
  preparar();

  var t;
  window.addEventListener('resize', function(){
    clearTimeout(t); t = setTimeout(preparar, 220);
  });
  // el cambio de idioma reescribe el texto: volver a partir
  window.addEventListener('quorelia:lang', function(){ setTimeout(preparar, 40); });
})();

/* 2 · Palabra rotativa — cicla los verbos del producto en su sitio */
(function rotor(){
  document.querySelectorAll('[data-rotor]').forEach(function(el){
    var palabras = el.getAttribute('data-rotor').split('|').map(function(s){ return s.trim(); });
    if (palabras.length < 2) return;
    el.classList.add('rotor'); el.innerHTML = '';
    var i = 0;
    var actual = document.createElement('i');
    actual.textContent = palabras[0];
    actual.setAttribute('data-state','in');
    el.appendChild(actual);
    // ancho fijo al término más largo, para que no salte el texto vecino
    var medidor = document.createElement('i');
    medidor.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap;';
    el.appendChild(medidor);
    var ancho = 0;
    palabras.forEach(function(p){ medidor.textContent = p; ancho = Math.max(ancho, medidor.offsetWidth); });
    el.removeChild(medidor);
    if (ancho) el.style.width = ancho + 'px';
    if (REDUCE) return;

    var visible = true;
    if ('IntersectionObserver' in window){
      new IntersectionObserver(function(es){ visible = es[0].isIntersecting; }).observe(el);
    }
    setInterval(function(){
      if (!visible || document.hidden) return;
      i = (i + 1) % palabras.length;
      var siguiente = document.createElement('i');
      siguiente.textContent = palabras[i];
      siguiente.setAttribute('data-state','next');
      el.appendChild(siguiente);
      requestAnimationFrame(function(){
        requestAnimationFrame(function(){
          actual.setAttribute('data-state','out');
          siguiente.setAttribute('data-state','in');
        });
      });
      var viejo = actual; actual = siguiente;
      setTimeout(function(){ if (viejo.parentNode) viejo.parentNode.removeChild(viejo); }, 700);
    }, 2200);
  });
})();

/* 3 · Conteo de cifras — sube hasta el valor al entrar en pantalla */
(function contarCifras(){
  var vals = document.querySelectorAll('.fig .v');
  if (!vals.length || REDUCE) return;
  var io = new IntersectionObserver(function(es, o){
    es.forEach(function(e){
      if (!e.isIntersecting) return;
      var el = e.target, texto = el.textContent.trim();
      o.unobserve(el);
      // sólo números simples: 38.616 · 91,7% · 2.029  (no "2 / 977")
      var m = texto.match(/^([\d.]+)(,\d+)?(%?)$/);
      if (!m) return;
      var entero = m[1].replace(/\./g,''), dec = m[2] ? m[2].replace(',','.') : '';
      var destino = parseFloat(entero + dec);
      if (!isFinite(destino) || destino <= 0) return;
      var decimales = m[2] ? m[2].length - 1 : 0;
      var t0 = null, dur = 1100;
      function fmt(n){
        var s = n.toFixed(decimales);
        var partes = s.split('.');
        partes[0] = partes[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');
        return partes.join(',') + m[3];
      }
      function paso(t){
        if (!t0) t0 = t;
        var p = Math.min((t - t0) / dur, 1);
        var e2 = 1 - Math.pow(1 - p, 4);           // salida suave
        el.textContent = fmt(destino * e2);
        if (p < 1) requestAnimationFrame(paso); else el.textContent = texto;
      }
      requestAnimationFrame(paso);
    });
  }, { threshold:0.4 });
  vals.forEach(function(v){ io.observe(v); });
})();

/* ── Revelado al hacer scroll ───────────────────────────────────────────── */
(function revelado(){
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = document.querySelectorAll('.rv');
  if (!els.length) return;
  var io = new IntersectionObserver(function(es, o){
    es.forEach(function(e){
      if (e.isIntersecting){ e.target.classList.add('in'); o.unobserve(e.target); }
    });
  }, { rootMargin:'0px 0px -8% 0px', threshold:0.05 });
  els.forEach(function(el){ io.observe(el); });
  requestAnimationFrame(function(){
    els.forEach(function(el){
      if (el.getBoundingClientRect().top < window.innerHeight * 0.95){
        el.classList.add('in'); io.unobserve(el);
      }
    });
  });
})();
