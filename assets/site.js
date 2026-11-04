// Theme toggle with a circular reveal from the button (View Transitions API)
(function () {
  var root = document.documentElement;
  var btn = document.querySelector('.theme-toggle');
  if (!btn) return;
  var mq = window.matchMedia('(prefers-color-scheme: dark)');
  function current() { return root.dataset.theme || (mq.matches ? 'dark' : 'light'); }
  function apply(t) {
    root.dataset.theme = t;
    try { localStorage.setItem('theme', t); } catch (e) {}
    btn.setAttribute('aria-label', t === 'dark' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro');
  }
  btn.setAttribute('aria-label', current() === 'dark' ? 'Cambiar a tema claro' : 'Cambiar a tema oscuro');
  btn.addEventListener('click', function () {
    var next = current() === 'dark' ? 'light' : 'dark';
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!document.startViewTransition || reduce) { apply(next); return; }
    var r = btn.getBoundingClientRect();
    var x = r.left + r.width / 2, y = r.top + r.height / 2;
    var radius = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
    root.classList.add('theme-switching');
    var vt = document.startViewTransition(function () { apply(next); });
    vt.ready.then(function () {
      root.animate(
        { clipPath: ['circle(0px at ' + x + 'px ' + y + 'px)', 'circle(' + radius + 'px at ' + x + 'px ' + y + 'px)'] },
        { duration: 650, easing: 'cubic-bezier(.2,.7,.2,1)', pseudoElement: '::view-transition-new(root)' }
      );
    });
    vt.finished.finally(function () { root.classList.remove('theme-switching'); });
  });
})();
