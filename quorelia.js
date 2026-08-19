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
