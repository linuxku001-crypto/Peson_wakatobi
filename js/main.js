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
    }

    hamburger.addEventListener('click', function () {
      setOpen(!navLinks.classList.contains('active'));
    });

    // Tutup menu setelah link di-klik
    navLinks.addEventListener('click', function (e) {
      if (e.target.closest('a')) setOpen(false);
    });

    // Tutup menu saat klik di luar area menu
    document.addEventListener('click', function (e) {
      if (!navLinks.classList.contains('active')) return;
      if (navLinks.contains(e.target) || hamburger.contains(e.target)) return;
      setOpen(false);
    });

    // Tutup menu saat tekan Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navLinks.classList.contains('active')) {
        setOpen(false);
        hamburger.focus();
      }
    });

    // Reset state saat kembali ke lebar desktop
    window.addEventListener('resize', function () {
      if (window.innerWidth > 768) setOpen(false);
    });
  }

  /* ----------------------------------------------------------------------
     2. Scroll reveal untuk kartu pulau
     Fallback aman: bila IntersectionObserver tidak ada, semua kartu langsung tampil.
     ---------------------------------------------------------------------- */
  function initScrollReveal() {
    var cards = document.querySelectorAll('.island-card');
    if (!cards.length) return;

    if (!('IntersectionObserver' in window)) {
      cards.forEach(function (card) { card.classList.add('visible'); });
      return;
    }

    var reduced = window.matchMedia &&
      window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduced) {
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
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    cards.forEach(function (card) { observer.observe(card); });
  }

  /* ----------------------------------------------------------------------
     3. Tandai link navigasi aktif sesuai halaman sekarang
     ---------------------------------------------------------------------- */
  function initActiveNav() {
    var current = window.location.pathname.split('/').pop() || 'index.html';
    var links = document.querySelectorAll('.nav-links a');
    links.forEach(function (link) {
      var href = link.getAttribute('href');
      if (!href) return;
      if (href === current || (current === '' && href === 'index.html')) {
        link.setAttribute('aria-current', 'page');
      }
    });
  }

  /* ----------------------------------------------------------------------
     4. Perbarui tahun footer secara otomatis
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
    initScrollReveal();
    initActiveNav();
    initFooterYear();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
