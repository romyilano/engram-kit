/* ===========================================================================
   ENGRAM // KIT — landing interactions
   Scroll progress · reveal-on-scroll · parallax. Respects reduced-motion.
   =========================================================================== */
(function () {
  "use strict";

  var reduce = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- scroll progress bar -------------------------------------------- */
  var bar = document.querySelector(".progress");
  function onScrollProgress() {
    var h = document.documentElement;
    var scrolled = h.scrollTop / (h.scrollHeight - h.clientHeight);
    if (bar) bar.style.width = (scrolled * 100).toFixed(2) + "%";
  }

  /* ---- reveal on scroll ----------------------------------------------- */
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if (reduce) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---- parallax -------------------------------------------------------- */
  var heroImgs = Array.prototype.slice.call(
    document.querySelectorAll(".hero__panels img"));
  var artImgs = Array.prototype.slice.call(
    document.querySelectorAll("[data-parallax]"));
  var ticking = false;

  function applyParallax() {
    var y = window.pageYOffset;

    // hero panels drift at varied speeds
    heroImgs.forEach(function (img, i) {
      var speed = 0.12 + (i % 4) * 0.05;
      img.style.transform = "translate3d(0," + (-y * speed) + "px,0)";
    });

    // feature art drifts relative to its own viewport position
    artImgs.forEach(function (img) {
      var rect = img.getBoundingClientRect();
      var vh = window.innerHeight || document.documentElement.clientHeight;
      if (rect.bottom < 0 || rect.top > vh) return;
      var progress = (rect.top + rect.height / 2 - vh / 2) / vh; // -0.5..0.5-ish
      var shift = progress * -28;
      img.style.transform = "translate3d(0," + shift.toFixed(1) + "px,0) scale(1.08)";
    });

    ticking = false;
  }

  function onScroll() {
    onScrollProgress();
    if (reduce) return;
    if (!ticking) {
      window.requestAnimationFrame(applyParallax);
      ticking = true;
    }
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", onScroll, { passive: true });
  onScroll();
})();
