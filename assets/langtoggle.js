(function () {
  function wire() {
    var alts = {};
    document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(function (l) {
      alts[(l.getAttribute('hreflang') || '').toLowerCase()] = l.getAttribute('href');
    });
    var lang = (document.documentElement.getAttribute('lang') || 'en').toLowerCase();
    var cur = lang.indexOf('zh') === 0 ? 'zh' : 'en';
    var other = cur === 'zh' ? 'en' : 'zh';
    var target = alts[other];
    if (!target) return;
    var btn = document.querySelector('.md-header__option .md-header__button');
    if (!btn) return;
    btn.setAttribute('title', other === 'zh' ? '切换到简体中文' : 'Switch to English');
    btn.addEventListener('click', function (e) {
      e.preventDefault(); e.stopPropagation();
      window.location.href = target;
    }, true);
  }
  if (document.readyState !== 'loading') wire();
  else document.addEventListener('DOMContentLoaded', wire);
  if (window.document$ && document$.subscribe) document$.subscribe(wire);
})();
