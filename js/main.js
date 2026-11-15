/* ==========================================================================
   Pesona Wakatobi — Shared JavaScript
   Vanilla JS, tanpa dependensi eksternal.
   ========================================================================== */
(function () {
  'use strict';

  /* ----------------------------------------------------------------------
     1. Mobile menu (hamburger)
     ---------------------------------------------------------------------- */
  function initMobileMenu() {
    var hamburger = document.getElementById('hamburger');
    var navLinks = document.getElementById('navLinks');
    if (!hamburger || !navLinks) return;

    function setOpen(open) {
      navLinks.classList.toggle('active', open);
      hamburger.setAttribute('aria-expanded', String(open));
      hamburger.setAttribute('aria-label', open ? 'Tutup menu navigasi' : 'Buka menu navigasi');
      document.body.style.overflow = open ? 'hidden' : '';
    }

    hamburger.addEventListener('click', function () {
      setOpen(!navLinks.classList.contains('active'));
    });

    navLinks.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    document.addEventListener('click', function (e) {
      if (!navLinks.classList.contains('active')) return;
      if (navLinks.contains(e.target) || hamburger.contains(e.target)) return;
      setOpen(false);
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navLinks.classList.contains('active')) {
        setOpen(false);
        hamburger.focus();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 900 && navLinks.classList.contains('active')) {
        setOpen(false);
      }
    });
  }

  /* ----------------------------------------------------------------------
     2. Navbar scroll state — makin solid saat halaman di-scroll
     ---------------------------------------------------------------------- */
  function initScrollNav() {
    var navbar = document.querySelector('.navbar');
    if (!navbar) return;

    var ticking = false;
    function update() {
      navbar.classList.toggle('is-scrolled', window.scrollY > 24);
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });
    update();
  }

  /* ----------------------------------------------------------------------
     3. Scroll reveal untuk kartu pulau
     Fallback aman: tanpa IntersectionObserver / reduced-motion -> langsung tampil.
     ---------------------------------------------------------------------- */
  function initScrollReveal() {
    var cards = document.querySelectorAll('.island-card');
    if (!cards.length) return;

    var reduced = window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (!('IntersectionObserver' in window) || reduced) {
      cards.forEach(function (card) { card.classList.add('visible'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });

    cards.forEach(function (card) { observer.observe(card); });
  }

  /* ----------------------------------------------------------------------
     4. Penomoran kartu destinasi (01, 02, 03, ...)
     ---------------------------------------------------------------------- */
  function initCardNumbers() {
    document.querySelectorAll('.destinations').forEach(function (grid) {
      var cards = grid.querySelectorAll('.dest-card');
      cards.forEach(function (card, i) {
        var media = card.querySelector('.dest-card__media');
        if (!media || media.querySelector('.dest-card__num')) return;
        var badge = document.createElement('span');
        badge.className = 'dest-card__num';
        badge.setAttribute('aria-hidden', 'true');
        badge.textContent = String(i + 1).padStart(2, '0');
        media.appendChild(badge);
      });
    });
  }

  /* ----------------------------------------------------------------------
     4b. Grid 2-kartu dipusatkan (fallback untuk browser tanpa :has())
     ---------------------------------------------------------------------- */
  function initTwoCardGrid() {
    document.querySelectorAll('.destinations').forEach(function (grid) {
      if (grid.querySelectorAll('.dest-card').length === 2) {
        grid.classList.add('destinations--pair');
      }
    });
  }

  /* ----------------------------------------------------------------------
     5. Tandai link navigasi aktif sesuai halaman sekarang
     ---------------------------------------------------------------------- */
  function initActiveNav() {
    var path = window.location.pathname.split('/').pop();
    var current = path || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(function (link) {
      var href = link.getAttribute('href');
      if (href === current) link.setAttribute('aria-current', 'page');
    });
  }

  /* ----------------------------------------------------------------------
     6. Perbarui tahun footer secara otomatis
     ---------------------------------------------------------------------- */
  function initFooterYear() {
    var year = String(new Date().getFullYear());
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = year;
    });
  }

  /* ---------------------------------------------------------------------- */
  function init() {
    initMobileMenu();
    initScrollNav();
    initScrollReveal();
    initCardNumbers();
    initTwoCardGrid();
    initActiveNav();
    initFooterYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
