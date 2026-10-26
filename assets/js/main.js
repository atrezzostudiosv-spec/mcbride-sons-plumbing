// ATREZZO — Shared navigation for independent static pages.
(() => {
  const button = document.querySelector('[data-mobile-toggle]');
  const menu = document.getElementById('mobile-menu');
  const icon = document.getElementById('mobile-menu-icon');
  const close = () => {
    if (!button || !menu) return;
    menu.classList.add('hidden');
    button.setAttribute('aria-expanded', 'false');
    if (icon) { icon.classList.remove('fa-xmark'); icon.classList.add('fa-bars'); }
  };
  if (button && menu) {
    button.addEventListener('click', () => {
      const opening = menu.classList.contains('hidden');
      menu.classList.toggle('hidden', !opening);
      button.setAttribute('aria-expanded', String(opening));
      if (icon) {
        icon.classList.toggle('fa-xmark', opening);
        icon.classList.toggle('fa-bars', !opening);
      }
    });
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape' && !menu.classList.contains('hidden')) {
        close(); button.focus();
      }
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click',close));
  }
})();


// Real staging form submit, with a third-party email relay (FormSubmit.co).
// 200/OK means provider accepted the request, NOT proof of Gmail delivery.
// Never pretend submission succeeded on failure.
(() => {
  document.querySelectorAll('form[data-atrezzo-test-form]').forEach(form => {
    form.addEventListener('submit', async (event) => {
      if (!form.checkValidity()) return;
      event.preventDefault();
      const submit = form.querySelector('button[type="submit"]');
      const status = form.querySelector('[data-form-status]');
      if (!submit || !status) return;
      submit.disabled = true;
      submit.setAttribute('aria-busy', 'true');
      status.textContent = 'Sending test request…';
      status.classList.remove('text-red-700','text-green-800');
      try {
        const data = Object.fromEntries(new FormData(form).entries());
        const response = await fetch('https://formsubmit.co/ajax/atrezzostudiosv@gmail.com', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(data)
        });
        const result = await response.json();
        if (!response.ok || !(result.success === true || result.success === 'true')) {
          throw new Error('Submission was not accepted by the form service.');
        }
        status.classList.add('text-green-800');
        status.textContent = 'Test request accepted by the form service. Atrezzo Studios must still verify receipt in Gmail. This is not a service booking.';
        form.reset();
      } catch (error) {
        status.classList.add('text-red-700');
        status.textContent = 'The test request could not be sent. Your information is still in the form; please try again or call the business directly.';
      } finally {
        submit.disabled = false;
        submit.removeAttribute('aria-busy');
      }
    });
  });
})();


// ATREZZO HOME — mobile and tablet callback dialog (2026-10-26)
// Use ONE existing callback form. It remains inline on desktop (>=1024px).
// On tablet/mobile with working JavaScript, move that same form panel into a native
// <dialog> (focus containment, Escape, backdrop); without JS it stays inline.
(() => {
  const wrap = document.getElementById('callback-form');
  const trigger = document.querySelector('.hero-form-link[href="#callback-form"]');
  const panel = wrap && wrap.querySelector('.form-outer');
  if (!wrap || !trigger || !panel || !window.matchMedia) return;

  const modal = document.createElement('dialog');
  if (typeof modal.showModal !== 'function') return;
  modal.id = 'home-callback-dialog';
  modal.className = 'hero-callback-dialog';
  modal.setAttribute('aria-label', 'Request a Callback');

  const toolbar = document.createElement('div');
  toolbar.className = 'hero-dialog-toolbar';
  const title = document.createElement('strong');
  title.textContent = 'Request a Callback';
  const closeButton = document.createElement('button');
  closeButton.type = 'button';
  closeButton.className = 'hero-dialog-close';
  closeButton.setAttribute('aria-label', 'Close callback form');
  closeButton.textContent = '×';
  toolbar.append(title, closeButton);

  const mount = document.createElement('div');
  mount.className = 'hero-dialog-content';
  modal.append(toolbar, mount);
  document.body.appendChild(modal);

  // Match the layout breakpoint, not the handset hardware.
  const mobile = window.matchMedia('(max-width: 1023px)');
  let openTrigger = null;

  const close = () => { if (modal.open) modal.close(); };
  const syncLayout = () => {
    if (mobile.matches) {
      if (panel.parentNode !== mount) mount.appendChild(panel);
      document.documentElement.classList.add('hero-popup-ready');
      trigger.setAttribute('aria-haspopup', 'dialog');
      trigger.setAttribute('aria-controls', modal.id);
    } else {
      close();
      if (panel.parentNode !== wrap) wrap.appendChild(panel);
      document.documentElement.classList.remove('hero-popup-ready');
      trigger.removeAttribute('aria-haspopup');
      trigger.removeAttribute('aria-controls');
    }
  };

  trigger.addEventListener('click', event => {
    if (!mobile.matches || panel.parentNode !== mount) return;
    event.preventDefault();
    openTrigger = trigger;
    modal.showModal();
    document.body.classList.add('hero-dialog-open');
    closeButton.focus();
  });

  closeButton.addEventListener('click', close);
  modal.addEventListener('click', event => {
    if (event.target === modal) close();
  });
  modal.addEventListener('close', () => {
    document.body.classList.remove('hero-dialog-open');
    if (mobile.matches && openTrigger && openTrigger.isConnected) {
      openTrigger.focus();
    }
    openTrigger = null;
  });

  if (typeof mobile.addEventListener === 'function') {
    mobile.addEventListener('change', syncLayout);
  } else if (typeof mobile.addListener === 'function') {
    mobile.addListener(syncLayout);
  }

  syncLayout();
})();


// ATREZZO HOME — cinematic background and editorial motion (2026-10-26).
// Source: Stepan SK / Pexels #7584762, illustrative licensed footage.
// Keep the CSS photo as a static fallback and do not download MP4 on
// mobile/tablet, reduced-motion, data-saving or very slow connections.
(() => {
  const hero = document.querySelector('.hero');
  const video = hero && hero.querySelector('video.hero-video');
  const toggle = hero && hero.querySelector('.hero-video-toggle');
  if (!hero || !video || !toggle || !window.matchMedia) return;

  const desktop = window.matchMedia('(min-width: 1024px)');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const connection = navigator.connection || navigator.mozConnection || navigator.webkitConnection;
  const urls = [
    // The 720p copy is preferred over heavier 1080p to reduce transfer.
    'https://videos.pexels.com/video-files/7584762/7584762-hd_1280_720_25fps.mp4',
    'https://videos.pexels.com/video-files/7584762/7584762-hd_1920_1080_25fps.mp4'
  ];

  let nextSource = 0;
  let mediaActive = false;
  let inView = true;
  let hasFrame = false;
  let userPaused = false;

  const mediaAllowed = () => desktop.matches && !reduced.matches &&
    !(connection && (connection.saveData ||
      /^(slow-2g|2g)$/.test(connection.effectiveType || '')));

  const visibleToUser = () => !document.hidden && inView;

  const syncButton = () => {
    toggle.hidden = !(mediaAllowed() && mediaActive && hasFrame && inView);
    toggle.textContent = userPaused ? 'Play video' : 'Pause video';
    toggle.setAttribute('aria-label',
      userPaused ? 'Play background video' : 'Pause background video');
  };

  const stop = () => {
    video.pause();
    hero.classList.remove('hero-video-playing');
    syncButton();
  };

  const reset = () => {
    stop();
    video.removeAttribute('src');
    video.load();
    mediaActive = false;
    hasFrame = false;
    nextSource = 0;
    userPaused = false;
    toggle.hidden = true;
  };

  const attemptPlay = () => {
    if (!mediaAllowed() || !visibleToUser() || userPaused) return;
    const result = video.play();
    if (result && typeof result.catch === 'function') {
      result.catch(() => {
        if (!hasFrame) hero.classList.remove('hero-video-playing');
        syncButton();
      });
    }
  };

  const loadSource = () => {
    if (!mediaAllowed() || nextSource >= urls.length) return;
    video.src = urls[nextSource++];
    video.load();
    attemptPlay();
  };

  video.addEventListener('playing', () => {
    if (!mediaAllowed() || !visibleToUser()) { stop(); return; }
    hasFrame = true;
    hero.classList.add('hero-video-playing');
    syncButton();
  });

  video.addEventListener('error', () => {
    hero.classList.remove('hero-video-playing');
    hasFrame = false;
    toggle.hidden = true;
    if (mediaAllowed() && nextSource < urls.length) loadSource();
    // With neither hosted file available, the static photo remains.
  });

  toggle.addEventListener('click', () => {
    if (!mediaAllowed() || !hasFrame) return;
    userPaused = !userPaused;
    if (userPaused) video.pause();
    else attemptPlay();
    syncButton();
  });

  const sync = () => {
    if (!mediaAllowed()) {
      if (mediaActive) reset();
      return;
    }
    if (!visibleToUser()) {
      stop();
      return;
    }
    if (!mediaActive) {
      mediaActive = true;
      nextSource = 0;
      loadSource();
    } else if (!userPaused) {
      attemptPlay();
    } else if (hasFrame) {
      hero.classList.add('hero-video-playing');
    }
    syncButton();
  };

  if (typeof desktop.addEventListener === 'function') desktop.addEventListener('change', sync);
  else if (typeof desktop.addListener === 'function') desktop.addListener(sync);
  if (typeof reduced.addEventListener === 'function') reduced.addEventListener('change', sync);
  else if (typeof reduced.addListener === 'function') reduced.addListener(sync);
  if (connection && typeof connection.addEventListener === 'function') connection.addEventListener('change', sync);
  document.addEventListener('visibilitychange', sync);

  if (window.IntersectionObserver) {
    const visibilityObserver = new IntersectionObserver(entries => {
      if (!entries.length) return;
      inView = entries[0].isIntersecting;
      sync();
    }, {threshold: 0.06});
    visibilityObserver.observe(hero);
  }
  sync();
})();

// Restrained scroll reveals, inspired by editorial timing, not copied effects.
// Progressive enhancement: content is always visible without IntersectionObserver.
(() => {
  if (!window.IntersectionObserver || !window.matchMedia ||
      window.matchMedia('(prefers-reduced-motion: reduce)').matches ||
      window.matchMedia('(max-width: 767px)').matches) return;
  const selectors = [
    '.intro .intro-grid > div',
    '.services .section-heading > div',
    '.services .section-heading > p',
    '.family .family-heading',
    '.family .family-person',
    '.approach .approach-left',
    '.approach .value-line',
    '.end-cta .end-grid > div'
  ];
  const targets = [...document.querySelectorAll(selectors.join(','))];
  if (!targets.length) return;

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, {threshold:0.08, rootMargin:'0px 0px -7% 0px'});

  targets.forEach((el, index) => {
    el.classList.add('atrezzo-reveal');
    // Tiny stagger for adjacent authentic family portraits, never long delays.
    if (el.classList.contains('family-person')) {
      const galleryIndex = [...el.parentNode.children].indexOf(el);
      el.style.setProperty('--reveal-delay', (galleryIndex * 85) + 'ms');
    }
    observer.observe(el);
  });
})();
