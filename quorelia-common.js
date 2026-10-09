/* ══════════════════════════════════════════════════════════════════════════
   QUORELIA — Comportamiento común a todas las páginas (oct 2026)
   · Textos del encabezado y pie compartidos, en ES / EN / 中文 (data-i18n-c).
   · Menús desplegables, menú del teléfono y marca de la página activa.
   · setLang() para las páginas nuevas. Las páginas antiguas traen su propio
     setLang; aquí sólo se escucha su evento 'quorelia:lang'.
   · Revelado sobrio (.q-rv) y envío de formularios a Formspree.
   Se carga al final del <body>, después del script propio de cada página.
   ══════════════════════════════════════════════════════════════════════════ */
(function(){
'use strict';

var C = {
 es:{
  nav_services:'Servicios', nav_industries:'Industrias', nav_ee:'Eagle Eye', nav_resources:'Recursos', nav_company:'Empresa',
  nav_cta:'Solicitar evaluación', nav_skip:'Saltar al contenido', nav_menu:'Menú', nav_close:'Cerrar',
  s_all_t:'Servicio integral para activos solares', s_all_d:'De la ingeniería a la operación: un solo responsable por su planta',
  s_am_t:'Gestión de activos', s_am_d:'Representante del dueño: desempeño, liquidaciones, contratistas y cumplimiento',
  s_ver_t:'Verificación', s_ver_d:'Cifras que su financista, su directorio y su contratista aceptan',
  s_om_t:'Operación y mantenimiento', s_om_d:'Mantenimiento guiado por datos, con socios de campo certificados',
  s_sb_t:'Solar + baterías', s_sb_d:'Autoconsumo, peak shaving y respaldo, dimensionados con su carga real',
  s_dsl_t:'Reemplazo de diésel', s_dsl_d:'Menos horas de generador y un ahorro medido, no estimado',
  s_eng_t:'Ingeniería', s_eng_d:'Factibilidad, ingeniería del dueño y supervisión de puesta en marcha',
  i_ren_t:'Propietarios de renovables', i_ren_d:'Carteras PMGD, baterías e híbridos',
  i_min_t:'Minería', i_min_d:'Faenas medianas, contratistas y campamentos',
  i_agr_t:'Agricultura', i_agr_d:'Plantas solares agrícolas y packings',
  i_food_t:'Alimentos y cadena de frío', i_food_d:'Plantas de proceso y frigoríficos',
  i_aqua_t:'Acuicultura y pesca', i_aqua_d:'Pontones híbridos y flotas en el sur',
  i_ind_t:'Industria', i_ind_d:'Grandes consumidores y Ley 21.305',
  ee_plat_t:'La plataforma', ee_plat_d:'Cómo Eagle Eye lee, verifica y reporta',
  ee_demo_t:'Demo en vivo', ee_demo_d:'Control Center y tablero BESS con datos de muestra',
  ee_rep_t:'Informes de muestra', ee_rep_d:'Lo que recibe cada mes, con datos ilustrativos',
  r_guide_t:'Guía de normativa eléctrica', r_guide_d:'Qué exigen el CEN, la SEC y la CNE a una planta',
  r_ins_t:'Insights', r_ins_d:'Análisis del mercado eléctrico chileno',
  c_about_t:'Nosotros', c_about_d:'Quiénes firman el contrato',
  c_pub_t:'Sector público', c_pub_d:'Trazabilidad para la fiscalización',
  c_contact_t:'Contacto', c_contact_d:'Evaluación de activos, evaluación energética o 30 minutos',
  f_desc:'Gestión de activos energéticos y verificación para dueños, fondos e industria en Chile. Eagle Eye incluido.',
  f_services:'Servicios', f_industries:'Industrias', f_ee:'Eagle Eye y recursos', f_company:'Empresa', f_contact:'Contacto',
  f_loc:'Santiago, Chile', f_book:'Agendar 30 minutos', f_terms:'Términos', f_priv:'Privacidad',
  f_motto:'Siempre vigilando. Al servicio de la energía del planeta.',
  f_fine:'Los informes de muestra, el Control Center y el tablero BESS de este sitio usan datos ilustrativos de una flota de demostración y no representan instalaciones ni clientes reales.',
  form_sending:'Enviando…', form_ok:'Recibido. Le escribimos dentro de un día hábil. Si prefiere, <a href="https://cal.com/quorelia/30min" target="_blank" rel="noopener">agende 30 minutos ahora</a>.',
  form_req:'Complete los campos marcados con *.', form_fail:'No pudimos enviar el formulario. Escríbanos a {mail} y le respondemos el mismo día.'
 },
 en:{
  nav_services:'Services', nav_industries:'Industries', nav_ee:'Eagle Eye', nav_resources:'Resources', nav_company:'Company',
  nav_cta:'Request an assessment', nav_skip:'Skip to content', nav_menu:'Menu', nav_close:'Close',
  s_all_t:'Complete service for solar assets', s_all_d:'From engineering to operations: one accountable manager for your plant',
  s_am_t:'Asset management', s_am_d:'The owner’s representative: performance, settlements, contractors and compliance',
  s_ver_t:'Verification', s_ver_d:'Numbers your lender, your board and your contractor all accept',
  s_om_t:'Operations & maintenance', s_om_d:'Data-driven maintenance with certified field partners',
  s_sb_t:'Solar + batteries', s_sb_d:'Self-consumption, peak shaving and backup, sized from your measured load',
  s_dsl_t:'Diesel replacement', s_dsl_d:'Fewer generator hours and savings that are measured, not estimated',
  s_eng_t:'Engineering', s_eng_d:'Feasibility, owner’s engineering and commissioning oversight',
  i_ren_t:'Renewable owners', i_ren_d:'PMGD portfolios, batteries and hybrids',
  i_min_t:'Mining', i_min_d:'Mid-size mines, contractors and camps',
  i_agr_t:'Agriculture', i_agr_d:'Farm solar plants and packing houses',
  i_food_t:'Food & cold chain', i_food_d:'Processing plants and cold stores',
  i_aqua_t:'Aquaculture & fisheries', i_aqua_d:'Hybrid feed barges and southern fleets',
  i_ind_t:'Industry', i_ind_d:'Large consumers and Ley 21.305',
  ee_plat_t:'The platform', ee_plat_d:'How Eagle Eye reads, verifies and reports',
  ee_demo_t:'Live demo', ee_demo_d:'Control Center and BESS dashboard on sample data',
  ee_rep_t:'Sample reports', ee_rep_d:'What you receive each month, with illustrative data',
  r_guide_t:'Chile electricity rules guide', r_guide_d:'What the CEN, the SEC and the CNE require of a plant',
  r_ins_t:'Insights', r_ins_d:'Analysis of Chile’s power market',
  c_about_t:'About us', c_about_d:'Who signs the contract',
  c_pub_t:'Public sector', c_pub_d:'Traceability for oversight',
  c_contact_t:'Contact', c_contact_d:'Asset assessment, energy assessment or 30 minutes',
  f_desc:'Energy asset management and verification for owners, funds and industry in Chile. Eagle Eye included.',
  f_services:'Services', f_industries:'Industries', f_ee:'Eagle Eye & resources', f_company:'Company', f_contact:'Contact',
  f_loc:'Santiago, Chile', f_book:'Book 30 minutes', f_terms:'Terms', f_priv:'Privacy',
  f_motto:'Ever watching. In service of the planet’s energy.',
  f_fine:'Sample reports, the Control Center and the BESS dashboard on this site use illustrative data from a demonstration fleet and do not represent real facilities or clients.',
  form_sending:'Sending…', form_ok:'Received. We will write back within one business day. If you prefer, <a href="https://cal.com/quorelia/30min" target="_blank" rel="noopener">book 30 minutes now</a>.',
  form_req:'Please complete the fields marked *.', form_fail:'We could not send the form. Write to {mail} and we will reply the same day.'
 },
 zh:{
  nav_services:'服务', nav_industries:'行业', nav_ee:'Eagle Eye', nav_resources:'资源', nav_company:'公司',
  nav_cta:'申请评估', nav_skip:'跳至正文', nav_menu:'菜单', nav_close:'关闭',
  s_all_t:'光伏资产一体化服务', s_all_d:'从工程到运营：一个对您电站负责的管理方',
  s_am_t:'资产管理', s_am_d:'业主代表：绩效、结算、承包商与合规',
  s_ver_t:'独立核验', s_ver_d:'贷款方、董事会与承包商都认可的数字',
  s_om_t:'运维', s_om_d:'由数据驱动的维护，由认证现场合作伙伴执行',
  s_sb_t:'光伏 + 储能', s_sb_d:'自发自用、削峰与备用电源，按实测负荷设计',
  s_dsl_t:'柴油替代', s_dsl_d:'减少发电机运行时数，节省经实测而非估算',
  s_eng_t:'工程', s_eng_d:'可行性研究、业主工程师与调试监督',
  i_ren_t:'可再生能源业主', i_ren_d:'PMGD 组合、储能与混合电站',
  i_min_t:'矿业', i_min_d:'中型矿山、承包商与营地',
  i_agr_t:'农业', i_agr_d:'农场光伏电站与包装厂',
  i_food_t:'食品与冷链', i_food_d:'加工厂与冷库',
  i_aqua_t:'水产养殖与渔业', i_aqua_d:'南部的混合动力饲料平台与船队',
  i_ind_t:'工业', i_ind_d:'大型用能企业与第 21.305 号法律',
  ee_plat_t:'平台', ee_plat_d:'Eagle Eye 如何读取、核验与报告',
  ee_demo_t:'在线演示', ee_demo_d:'基于示例数据的控制中心与储能看板',
  ee_rep_t:'样例报告', ee_rep_d:'每月交付内容（示意数据）',
  r_guide_t:'智利电力法规指南', r_guide_d:'CEN、SEC 与 CNE 对电站的要求',
  r_ins_t:'洞察', r_ins_d:'智利电力市场分析',
  c_about_t:'关于我们', c_about_d:'签署合同的团队',
  c_pub_t:'公共部门', c_pub_d:'服务监管的可追溯性',
  c_contact_t:'联系我们', c_contact_d:'资产评估、能源评估或 30 分钟会议',
  f_desc:'面向智利业主、基金与工业企业的能源资产管理与独立核验。含 Eagle Eye。',
  f_services:'服务', f_industries:'行业', f_ee:'Eagle Eye 与资源', f_company:'公司', f_contact:'联系',
  f_loc:'智利 圣地亚哥', f_book:'预约 30 分钟', f_terms:'条款', f_priv:'隐私',
  f_motto:'始终守望，服务地球能源。',
  f_fine:'本站的样例报告、控制中心与储能看板均使用演示电站组合的示意数据，不代表真实电站或客户。',
  form_sending:'发送中…', form_ok:'已收到。我们将在一个工作日内回复。您也可以<a href="https://cal.com/quorelia/30min" target="_blank" rel="noopener">立即预约 30 分钟</a>。',
  form_req:'请填写带 * 的字段。', form_fail:'表单未能发送。请发邮件至 {mail}，我们当天回复。'
 }
};
window.Q_COMMON = C;

function lang(){ var l=(document.documentElement.getAttribute('lang')||'es').slice(0,2); return C[l]?l:'es'; }
function t(k){ var d=C[lang()]; return (d && d[k]!==undefined) ? d[k] : (C.es[k]||''); }

function applyCommon(){
  var d=C[lang()];
  document.querySelectorAll('[data-i18n-c]').forEach(function(el){
    var k=el.getAttribute('data-i18n-c'); if(d[k]!==undefined) el.innerHTML=d[k];
  });
  document.querySelectorAll('[data-i18n-c-aria]').forEach(function(el){
    var k=el.getAttribute('data-i18n-c-aria'); if(d[k]!==undefined) el.setAttribute('aria-label', d[k]);
  });
}

/* ── setLang para páginas nuevas (window.Q_PAGE = {es:{},en:{},zh:{}}) ── */
if (typeof window.setLang !== 'function') {
  window.setLang = function(l){
    if(!C[l]) l='es';
    var root=document.documentElement; root.setAttribute('lang', l);
    ['btn','mb'].forEach(function(p){ ['en','es','zh'].forEach(function(k){
      var b=document.getElementById(p+'-'+k); if(b) b.classList.toggle('on', l===k); }); });
    var P=(window.Q_PAGE && window.Q_PAGE[l]) || {};
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k=el.getAttribute('data-i18n'); if(P[k]!==undefined) el.innerHTML=P[k]; });
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el){
      var k=el.getAttribute('data-i18n-ph'); if(P[k]!==undefined) el.setAttribute('placeholder', P[k]); });
    document.querySelectorAll('[data-i18n-aria]').forEach(function(el){
      var k=el.getAttribute('data-i18n-aria'); if(P[k]!==undefined) el.setAttribute('aria-label', P[k]); });
    if(P.__title) document.title=P.__title;
    var md=document.querySelector('meta[name="description"]'); if(md && P.__desc) md.setAttribute('content', P.__desc);
    try{ localStorage.setItem('q-lang', l); }catch(e){}
    window.dispatchEvent(new Event('quorelia:lang'));
  };
  /* Guardar el texto original (español) para poder volver a él */
  (function(){
    if(!window.Q_PAGE) return;
    var es=window.Q_PAGE.es=window.Q_PAGE.es||{};
    document.querySelectorAll('[data-i18n]').forEach(function(el){
      var k=el.getAttribute('data-i18n'); if(es[k]===undefined) es[k]=el.innerHTML; });
    document.querySelectorAll('[data-i18n-ph]').forEach(function(el){
      var k=el.getAttribute('data-i18n-ph'); if(es[k]===undefined) es[k]=el.getAttribute('placeholder')||''; });
    if(es.__title===undefined) es.__title=document.title;
    var md=document.querySelector('meta[name="description"]'); if(md && es.__desc===undefined) es.__desc=md.getAttribute('content');
  })();
  (function(){
    var s=null; try{ s=localStorage.getItem('q-lang'); }catch(e){}
    var nav=(navigator.language||'es').toLowerCase();
    window.setLang(s || (nav.indexOf('zh')===0 ? 'zh' : nav.indexOf('en')===0 ? 'en' : 'es'));
  })();
}
window.addEventListener('quorelia:lang', applyCommon);
applyCommon();

/* ── Menús desplegables del escritorio ─────────────────────────────── */
var items=document.querySelectorAll('.q-nav__item');
function closeAll(except){ items.forEach(function(it){ if(it!==except){ it.classList.remove('open');
  var b=it.querySelector('.q-nav__btn'); if(b) b.setAttribute('aria-expanded','false'); } }); }
items.forEach(function(it){
  var b=it.querySelector('.q-nav__btn'); if(!b) return;
  b.addEventListener('click', function(e){
    e.stopPropagation();
    var open=!it.classList.contains('open');
    closeAll(it); it.classList.toggle('open', open); it.classList.remove('closed');
    b.setAttribute('aria-expanded', open?'true':'false');
  });
  it.addEventListener('mouseleave', function(){ it.classList.remove('closed'); });
});
document.addEventListener('click', function(){ closeAll(null); });
document.addEventListener('keydown', function(e){
  if(e.key==='Escape'){ items.forEach(function(it){ if(it.classList.contains('open')||it.matches(':hover')){ it.classList.add('closed'); } }); closeAll(null);
    if(document.activeElement && document.activeElement.closest && document.activeElement.closest('.q-nav__item')) document.activeElement.blur(); }
});

/* ── Menú del teléfono ─────────────────────────────────────────────── */
(function(){
  var b=document.getElementById('q-burger'), d=document.getElementById('q-drawer'),
      s=document.getElementById('q-scrim'), c=document.getElementById('q-dclose'), last=null;
  if(!b||!d||!s) return;
  function abrir(){ last=document.activeElement; d.hidden=false; s.hidden=false;
    requestAnimationFrame(function(){ d.classList.add('on'); s.classList.add('on'); });
    b.setAttribute('aria-expanded','true'); document.body.classList.add('locked');
    var f=d.querySelector('summary, a'); if(f) f.focus({preventScroll:true}); }
  function cerrar(){ d.classList.remove('on'); s.classList.remove('on'); b.setAttribute('aria-expanded','false');
    document.body.classList.remove('locked');
    setTimeout(function(){ if(!d.classList.contains('on')){ d.hidden=true; s.hidden=true; } }, 330);
    if(last) last.focus({preventScroll:true}); }
  b.addEventListener('click', function(){ d.classList.contains('on')?cerrar():abrir(); });
  s.addEventListener('click', cerrar); if(c) c.addEventListener('click', cerrar);
  d.querySelectorAll('a').forEach(function(a){ a.addEventListener('click', cerrar); });
  document.addEventListener('keydown', function(e){
    if(!d.classList.contains('on')) return;
    if(e.key==='Escape'){ cerrar(); return; }
    if(e.key!=='Tab') return;
    var f=d.querySelectorAll('a[href], button:not([disabled]), summary'); if(!f.length) return;
    var a=f[0], z=f[f.length-1];
    if(e.shiftKey && document.activeElement===a){ e.preventDefault(); z.focus(); }
    else if(!e.shiftKey && document.activeElement===z){ e.preventDefault(); a.focus(); }
  });
  window.addEventListener('resize', function(){ if(window.innerWidth>1000 && d.classList.contains('on')) cerrar(); });
})();

/* ── Página activa en el menú ──────────────────────────────────────── */
(function(){
  function norm(p){ p=(p||'/').split('#')[0].split('?')[0]; p=p.replace(/index\.html$/,''); if(p.slice(-5)!=='.html' && p.slice(-1)!=='/') p+='/'; return p; }
  var here=norm(location.pathname);
  document.querySelectorAll('.q-nav__link, .q-dnav a').forEach(function(a){
    var u; try{ u=new URL(a.getAttribute('href'), location.href); }catch(e){ return; }
    if(u.origin!==location.origin || u.hash) return;
    if(norm(u.pathname)===here){
      a.classList.add('on'); a.setAttribute('aria-current','page');
      var it=a.closest('.q-nav__item'); if(it){ var b=it.querySelector('.q-nav__btn'); if(b) b.classList.add('on'); }
      var det=a.closest('details'); if(det) det.open=true;
    }
  });
})();

/* ── Revelado sobrio ───────────────────────────────────────────────── */
(function(){
  var els=document.querySelectorAll('.q-rv'); if(!els.length) return;
  if(!('IntersectionObserver' in window)){ els.forEach(function(e){ e.classList.add('in'); }); return; }
  var io=new IntersectionObserver(function(es,o){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); o.unobserve(e.target); } }); },
    {rootMargin:'0px 0px -6% 0px', threshold:0.05});
  els.forEach(function(e){ if(e.getBoundingClientRect().top < window.innerHeight) e.classList.add('in'); else io.observe(e); });
})();

/* ── Formularios (Formspree → jay@quorelia.org) ────────────────────────
   <form class="q-form" data-endpoint="mljraopz" data-subject="Evaluación de activos">
   Cada campo con name; los obligatorios con required. Un <div class="fmsg"> dentro
   del formulario muestra el resultado. El botón de envío lleva [data-send]. */
window.Q = window.Q || {};
Q.t = t;
Q.bindForm = function(f){
  if(!f || f.dataset.bound) return; f.dataset.bound='1';
  var msg=f.querySelector('.fmsg'), btn=f.querySelector('[data-send]');
  var lbl=btn && (btn.querySelector('[data-label]')||btn);
  function show(kind, html){ if(msg){ msg.className='fmsg '+kind; msg.innerHTML=html; } }
  function clean(s){ return String(s||'').replace(/<[^>]*>/g,'').trim(); }
  f.addEventListener('submit', function(e){
    e.preventDefault();
    var hp=f.querySelector('[name="_gotcha"]'); if(hp && hp.value) return;
    if(!f.checkValidity()){ show('bad', t('form_req')); var bad=f.querySelector(':invalid'); if(bad) bad.focus(); return; }
    var data={}; new FormData(f).forEach(function(v,k){ if(k==='_gotcha') return;
      data[k]= data[k]!==undefined ? data[k]+', '+v : v; });
    var who=clean(data.name||data.first_name||'')+(data.company?' · '+clean(data.company):'');
    data._subject='Quorelia · '+(f.getAttribute('data-subject')||'Contacto')+(who?' · '+who:'');
    data.page=location.pathname; data.lang=lang();
    var endpoint=f.getAttribute('data-endpoint')||'mljraopz';
    var orig=lbl?lbl.textContent:''; if(btn) btn.disabled=true; if(lbl) lbl.textContent=t('form_sending');
    var body=Object.keys(data).map(function(k){ return k+': '+clean(data[k]); }).join('\n');
    var mail='<a href="mailto:jay@quorelia.org?subject='+encodeURIComponent(data._subject)+'&body='+encodeURIComponent(body)+'">jay@quorelia.org</a>';
    fetch('https://formspree.io/f/'+endpoint,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
      .then(function(r){ if(!r.ok) throw new Error('http '+r.status); f.reset(); show('ok', t('form_ok'));
        if(window.gtag) try{ gtag('event','generate_lead',{form:f.getAttribute('data-subject')||'contact'}); }catch(e){} })
      .catch(function(){ show('bad', t('form_fail').replace('{mail}', mail)); })
      .then(function(){ if(btn) btn.disabled=false; if(lbl) lbl.textContent=orig; });
  });
};
document.querySelectorAll('form.q-form').forEach(Q.bindForm);

/* Pestañas accesibles: [role=tablist] > [role=tab][aria-controls] */
document.querySelectorAll('[role="tablist"]').forEach(function(list){
  var tabs=list.querySelectorAll('[role="tab"]');
  function sel(tab){ tabs.forEach(function(x){ var on=x===tab; x.setAttribute('aria-selected', on?'true':'false'); x.tabIndex=on?0:-1;
    var p=document.getElementById(x.getAttribute('aria-controls')); if(p) p.hidden=!on; }); }
  tabs.forEach(function(tab,i){
    tab.addEventListener('click', function(){ sel(tab); if(history.replaceState) history.replaceState(null,'','#'+tab.getAttribute('aria-controls')); });
    tab.addEventListener('keydown', function(e){ var j=null;
      if(e.key==='ArrowRight') j=(i+1)%tabs.length; if(e.key==='ArrowLeft') j=(i-1+tabs.length)%tabs.length;
      if(j!==null){ e.preventDefault(); tabs[j].focus(); sel(tabs[j]); } });
  });
  var h=(location.hash||'').slice(1), start=null;
  tabs.forEach(function(x){ if(x.getAttribute('aria-controls')===h) start=x; });
  sel(start||tabs[0]);
});
})();
