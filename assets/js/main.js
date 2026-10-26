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


// ATREZZO HOME — mobile callback dialog (2026-10-26)
// Use ONE existing callback form. It remains inline on desktop/tablet.
// On mobile with working JavaScript, move that same form panel into a native
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
  const mobile = window.matchMedia('(max-width: 767px)');
  let openTrigger = null;

  const close = () => { if (modal.open) modal.close(); };
  const syncLayout = () => {
    if (mobile.matches) {
      if (panel.parentNode !== mount) mount.appendChild(panel);
      document.documentElement.classList.add('hero-popup-ready');
    } else {
      close();
      if (panel.parentNode !== wrap) wrap.appendChild(panel);
      document.documentElement.classList.remove('hero-popup-ready');
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
