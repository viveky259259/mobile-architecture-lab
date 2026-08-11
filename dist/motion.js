/* Shared, opt-in motion runtime for MAL's interactive public pages. */
(function () {
  "use strict";

  var body = document.body;
  var root = document.documentElement;
  var reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)");

  if (!body || !body.dataset.motionPage || (reducedMotion && reducedMotion.matches)) return;

  var pageSelectors = {
    homework: [".nav", ".hero .hero-copy > *", ".brief-card", ".section-head", ".card", ".day", ".callout", ".footer"],
    "assignment-2": [".nav", ".hero .inner > *", ".section-head", ".card", ".day", ".architecture > *", ".callout", ".actions", ".footer"],
    lab3: [".nav", ".hero-grid > *", ".section-head", ".card", ".footer"],
    organizers: [".nav", ".content > :not(.grid)", ".profile-card", "footer"],
    "sponsor-deck": [".slide"]
  };
  var interactiveSelector = ".btn, .nav-cta, .cta, .theme-toggle, .card, .day, .profile-card, .tier, .panel";
  var revealTargets = [];
  var seen = new Set();
  var selectors = pageSelectors[body.dataset.motionPage] || [];

  root.classList.add("motion-runtime");

  selectors.forEach(function (selector) {
    document.querySelectorAll(selector).forEach(function (node) {
      if (seen.has(node)) return;
      seen.add(node);
      revealTargets.push(node);
    });
  });

  revealTargets.forEach(function (node, index) {
    node.setAttribute("data-motion-reveal", "");
    node.style.setProperty("--motion-delay", Math.min(index, 7) * 45 + "ms");
  });

  document.querySelectorAll(interactiveSelector).forEach(function (node) {
    node.setAttribute("data-motion-interactive", "");
    if (!node.hasAttribute("data-motion-reveal")) {
      node.classList.add("motion-interactive-only");
    }
  });

  function reveal(node) {
    node.classList.add("is-motion-visible");
    window.setTimeout(function () {
      node.classList.add("is-motion-settled");
      node.style.setProperty("--motion-delay", "0ms");
    }, 760);
  }

  if (!revealTargets.length) return;

  if (!("IntersectionObserver" in window)) {
    revealTargets.forEach(reveal);
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      reveal(entry.target);
      observer.unobserve(entry.target);
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.07 });

  revealTargets.forEach(function (node) {
    observer.observe(node);
  });
}());
