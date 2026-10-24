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
