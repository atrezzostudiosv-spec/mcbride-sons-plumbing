/* ATREZZO — Seven service pages: mobile-only popup for the EXISTING hero form.
   Desktop/tablet >=768px remain inline. No JS / unsupported <dialog>: inline form remains.
   Do not clone forms, override submit handling or intercept page scroll. */
(() => {
  const hero = document.querySelector('.detail-hero');
  const grid = hero?.querySelector('.service-hero-grid');
  const copy = grid?.querySelector('.service-hero-copy');
  const panel = grid?.querySelector('.hero-contact-panel');
  const contact = copy?.querySelector('a[href*="/contact-us/index.html"]');
  const heading = panel?.querySelector('.hero-contact-heading');
  const form = panel?.querySelector('form[data-atrezzo-test-form]');
  if (!grid || !copy || !panel || !contact || !heading || !form ||
      !window.matchMedia || typeof HTMLDialogElement === 'undefined' ||
      typeof HTMLDialogElement.prototype.showModal !== 'function') return;

  const smallScreen = window.matchMedia('(max-width: 767px)');
  const marker = document.createComment('Original service form mount');
  grid.insertBefore(marker, panel);

  const trigger = document.createElement('button');
  trigger.type = 'button';
  trigger.className = 'at-service-popup-trigger';
  trigger.textContent = heading.textContent.trim() || 'Request Service';
  trigger.hidden = true;

  const dialog = document.createElement('dialog');
  dialog.id = 'at-service-form-dialog';
  dialog.className = 'at-service-form-dialog';
  dialog.setAttribute('aria-labelledby', heading.id);

  const toolbar = document.createElement('div');
  toolbar.className = 'at-service-form-dialog-toolbar';
  const label = document.createElement('strong');
  label.textContent = 'Service inquiry / Atrezzo demo';
  const closeButton = document.createElement('button');
  closeButton.type = 'button';
  closeButton.className = 'at-service-form-dialog-close';
  closeButton.setAttribute('aria-label', 'Close service request form');
  closeButton.textContent = '×';
  toolbar.append(label, closeButton);
  dialog.appendChild(toolbar);
  document.body.appendChild(dialog);

  contact.classList.add('at-service-original-contact');
  contact.parentElement.insertBefore(trigger, contact);

  trigger.setAttribute('aria-haspopup', 'dialog');
  trigger.setAttribute('aria-controls', dialog.id);
  trigger.setAttribute('aria-expanded', 'false');

  const restorePanel = () => {
    if (panel.parentNode !== grid) {
      marker.parentNode?.insertBefore(panel, marker.nextSibling);
    }
  };

  const sync = () => {
    if (smallScreen.matches) {
      if (panel.parentNode !== dialog) dialog.appendChild(panel);
      trigger.hidden = false;
      document.documentElement.classList.add('at-service-popup-ready');
    } else {
      if (dialog.open) dialog.close();
      document.documentElement.classList.remove('at-service-dialog-open','at-service-popup-ready');
      restorePanel();
      trigger.hidden = true;
      trigger.setAttribute('aria-expanded', 'false');
    }
  };

  trigger.addEventListener('click', () => {
    if (!smallScreen.matches) return;
    if (panel.parentNode !== dialog) dialog.appendChild(panel);
    try {
      dialog.showModal();
      document.documentElement.classList.add('at-service-dialog-open');
      trigger.setAttribute('aria-expanded','true');
      closeButton.focus({preventScroll:true});
    } catch (error) {
      document.documentElement.classList.remove('at-service-dialog-open','at-service-popup-ready');
      restorePanel();
      trigger.hidden = true;
    }
  });

  const close = () => { if (dialog.open) dialog.close(); };
  closeButton.addEventListener('click', close);
  dialog.addEventListener('click', (event) => {
    if (event.target === dialog) close();
  });
  dialog.addEventListener('close', () => {
    document.documentElement.classList.remove('at-service-dialog-open');
    trigger.setAttribute('aria-expanded','false');
    if (smallScreen.matches && !trigger.hidden) trigger.focus({preventScroll:true});
  });

  smallScreen.addEventListener?.('change', sync);
  window.addEventListener('resize',sync,{passive:true});
  sync();
})();
