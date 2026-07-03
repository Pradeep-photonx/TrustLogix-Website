/* TrustLogix redesign — interactions */
(function () {
  "use strict";

  /* ---- Sticky nav (auto-hide animation disabled) ---- */
  var nav = document.getElementById("nav");

  /* ---- Mobile menu toggle ---- */
  var burger = document.getElementById("burger");
  if (burger && nav) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });

    /* On mobile, tapping a dropdown parent toggles it; close menu on leaf click */
    nav.addEventListener("click", function (e) {
      var link = e.target.closest(".nav__link");
      if (link && window.matchMedia("(max-width: 768px)").matches) {
        var item = link.parentElement;
        if (item.querySelector(".nav__dropdown")) {
          e.preventDefault();
          item.classList.toggle("is-expanded");
        }
      }
    });
  }

  /* ---- Business Value carousel ---- */
  var bv = document.getElementById("bv-carousel");
  if (bv) {
    var track = bv.querySelector(".bv__track");
    var slides = bv.querySelectorAll(".bv__slide");
    var dots = bv.querySelectorAll(".bv__dot");
    var arrows = bv.querySelectorAll(".bv__arrow");
    var count = slides.length;
    var index = 0;
    var autoTimer = null;

    var goTo = function (i) {
      index = Math.max(0, Math.min(i, count - 1)); /* clamp — no manual wrap */
      track.style.transform = "translateX(" + -index * 100 + "%)";
      dots.forEach(function (d, di) { d.classList.toggle("is-active", di === index); });
      /* reference disabled-arrow state: prev muted at first, next muted at last */
      arrows.forEach(function (btn) {
        var dir = parseInt(btn.getAttribute("data-dir"), 10);
        var off = (dir < 0 && index === 0) || (dir > 0 && index === count - 1);
        btn.classList.toggle("is-disabled", off);
      });
    };

    arrows.forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (btn.classList.contains("is-disabled")) return;
        goTo(index + parseInt(btn.getAttribute("data-dir"), 10));
        restart();
      });
    });
    dots.forEach(function (d) {
      d.addEventListener("click", function () {
        goTo(parseInt(d.getAttribute("data-i"), 10));
        restart();
      });
    });

    /* autoplay — advances every 5s, loops to start at the end, pauses on hover */
    var start = function () { autoTimer = window.setInterval(function () { goTo(index < count - 1 ? index + 1 : 0); }, 5000); };
    var restart = function () { window.clearInterval(autoTimer); start(); };
    bv.addEventListener("mouseenter", function () { window.clearInterval(autoTimer); });
    bv.addEventListener("mouseleave", restart);
    goTo(0); /* set initial arrow disabled state */
    start();
  }

  /* ---- Testimonials carousel (horizontal scroll) ---- */
  var rTrack = document.getElementById("reviews-track");
  if (rTrack) {
    var rArrows = document.querySelectorAll(".reviews-arrow");
    var rPrev = null, rNext = null;
    rArrows.forEach(function (a) {
      if (a.getAttribute("data-dir") === "-1") rPrev = a; else rNext = a;
    });
    var stepBy = function (dir) {
      var card = rTrack.querySelector(".review");
      var gap = parseFloat(getComputedStyle(rTrack).columnGap) || 16;
      var step = card ? card.getBoundingClientRect().width + gap : rTrack.clientWidth;
      rTrack.scrollBy({ left: dir * step, behavior: "smooth" });
    };
    /* ---- pagination dots (one per "page" of cards in view) ---- */
    var rDotsBox = document.getElementById("reviews-dots");
    var rDots = [];
    var pageCount = 1;
    var buildDots = function () {
      var card = rTrack.querySelector(".review");
      var gap = parseFloat(getComputedStyle(rTrack).columnGap) || 16;
      var cardW = card ? card.getBoundingClientRect().width + gap : rTrack.clientWidth;
      var perView = Math.max(1, Math.round(rTrack.clientWidth / cardW));
      var total = rTrack.querySelectorAll(".review").length;
      var newCount = Math.max(1, Math.ceil(total / perView));
      if (newCount === pageCount && rDots.length) return;
      pageCount = newCount;
      rDotsBox.innerHTML = "";
      rDots = [];
      for (var i = 0; i < pageCount; i++) {
        var d = document.createElement("button");
        d.className = "reviews-dot";
        d.setAttribute("aria-label", "Go to reviews page " + (i + 1));
        (function (idx) {
          d.addEventListener("click", function () {
            var max = rTrack.scrollWidth - rTrack.clientWidth;
            rTrack.scrollTo({ left: pageCount > 1 ? (idx / (pageCount - 1)) * max : 0, behavior: "smooth" });
          });
        })(i);
        rDotsBox.appendChild(d);
        rDots.push(d);
      }
    };

    var updateRArrows = function () {
      var max = rTrack.scrollWidth - rTrack.clientWidth;
      if (rPrev) rPrev.classList.toggle("is-disabled", rTrack.scrollLeft <= 60);
      if (rNext) rNext.classList.toggle("is-disabled", rTrack.scrollLeft >= max - 60);
      var active = max > 0 ? Math.round((rTrack.scrollLeft / max) * (pageCount - 1)) : 0;
      rDots.forEach(function (d, i) { d.classList.toggle("is-active", i === active); });
    };
    rArrows.forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (btn.classList.contains("is-disabled")) return;
        stepBy(parseInt(btn.getAttribute("data-dir"), 10));
      });
    });
    rTrack.addEventListener("scroll", updateRArrows, { passive: true });
    window.addEventListener("resize", function () { buildDots(); updateRArrows(); });
    buildDots();
    updateRArrows();
  }

  /* ---- Resources carousel (horizontal scroll) — supports multiple per page ---- */
  document.querySelectorAll(".res-track").forEach(function (resTrack) {
    var scope = resTrack.closest("section") || document;
    var resArrows = scope.querySelectorAll(".res-arrow");
    var resStep = function (dir) {
      var card = resTrack.querySelector(".res-card");
      var gap = parseFloat(getComputedStyle(resTrack).columnGap) || 16;
      var step = card ? card.getBoundingClientRect().width + gap : resTrack.clientWidth;
      resTrack.scrollBy({ left: dir * step, behavior: "smooth" });
    };
    /* ---- pagination dots (one per "page" of cards in view) ---- */
    var resDotsBox = scope.querySelector(".res-dots");
    var resDots = [];
    var resPageCount = 1;
    var resBuildDots = function () {
      var card = resTrack.querySelector(".res-card");
      var gap = parseFloat(getComputedStyle(resTrack).columnGap) || 16;
      var cardW = card ? card.getBoundingClientRect().width + gap : resTrack.clientWidth;
      var perView = Math.max(1, Math.round(resTrack.clientWidth / cardW));
      var total = resTrack.querySelectorAll(".res-card").length;
      var newCount = Math.max(1, Math.ceil(total / perView));
      if (newCount === resPageCount && resDots.length) return;
      resPageCount = newCount;
      if (!resDotsBox) return;
      resDotsBox.innerHTML = "";
      resDots = [];
      for (var i = 0; i < resPageCount; i++) {
        var d = document.createElement("button");
        d.className = "res-dot";
        d.setAttribute("aria-label", "Go to page " + (i + 1));
        (function (idx) {
          d.addEventListener("click", function () {
            var max = resTrack.scrollWidth - resTrack.clientWidth;
            resTrack.scrollTo({ left: resPageCount > 1 ? (idx / (resPageCount - 1)) * max : 0, behavior: "smooth" });
          });
        })(i);
        resDotsBox.appendChild(d);
        resDots.push(d);
      }
    };
    var resUpdate = function () {
      var max = resTrack.scrollWidth - resTrack.clientWidth;
      resArrows.forEach(function (btn) {
        var dir = parseInt(btn.getAttribute("data-dir"), 10);
        var off = (dir < 0 && resTrack.scrollLeft <= 4) || (dir > 0 && resTrack.scrollLeft >= max - 4);
        btn.classList.toggle("is-disabled", off);
      });
      var active = max > 0 ? Math.round((resTrack.scrollLeft / max) * (resPageCount - 1)) : 0;
      resDots.forEach(function (d, i) { d.classList.toggle("is-active", i === active); });
    };
    resArrows.forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (btn.classList.contains("is-disabled")) return;
        resStep(parseInt(btn.getAttribute("data-dir"), 10));
      });
    });
    resTrack.addEventListener("scroll", resUpdate, { passive: true });
    window.addEventListener("resize", function () { resBuildDots(); resUpdate(); });
    resBuildDots();
    resUpdate();
  });

  /* ---- Scroll reveal ---- */
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealEls = document.querySelectorAll(".reveal");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Animated metric counters ---- */
  var counters = document.querySelectorAll(".metric__value[data-count]");
  var animateCount = function (el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    var start = null;
    var duration = 1600;
    var step = function (ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = Math.round(target * eased);
      el.textContent = val + suffix;
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = target + suffix;
    };
    requestAnimationFrame(step);
  };

  /* count-up animation disabled — static values shown as rendered */
  void counters; void animateCount;
})();
