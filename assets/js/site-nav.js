// McBride shared Services navigation — works on every static page.
// Services label links to overview; adjacent caret opens six service pages.
// Mobile submenu has its own disclosure; no keyboard/scroll trapping.
(() => {
  const header=document.querySelector('.at-site-nav');
  if (!header) return;
  const group=header.querySelector('[data-services-menu]');
  const toggle=group?.querySelector('.at-services-toggle');
  const panel=group?.querySelector('.at-services-panel');
  const mobileToggle=header.querySelector('.at-mobile-services-toggle');
  const mobileList=header.querySelector('.at-mobile-services-list');
  if(!group || !toggle || !panel || !mobileToggle || !mobileList) return;
  const closeDesktop=()=>{
    group.classList.remove('is-open');
    toggle.setAttribute('aria-expanded','false');
  };
  const showDesktop=()=>{
    if(group.classList.contains('is-dismissed'))return;
    group.classList.add('is-open');
    toggle.setAttribute('aria-expanded','true');
  };
  group.addEventListener('pointerenter',showDesktop);
  group.addEventListener('pointerleave',()=>{
    group.classList.remove('is-dismissed');
    if(!group.contains(document.activeElement))closeDesktop();
  });
  group.addEventListener('focusin',showDesktop);
  group.addEventListener('focusout',event=>{
    if(!group.contains(event.relatedTarget)){
      group.classList.remove('is-dismissed');
      closeDesktop();
    }
  });
  toggle.addEventListener('click',()=>{
    const open=toggle.getAttribute('aria-expanded')!=='true' || group.classList.contains('is-dismissed');
    group.classList.remove('is-dismissed');
    group.classList.toggle('is-open',open);
    toggle.setAttribute('aria-expanded',String(open));
  });
  group.addEventListener('keydown',e=>{
    if(e.key==='Escape'){
      group.classList.add('is-dismissed');
      closeDesktop();
      toggle.focus();
    }
  });
  document.addEventListener('pointerdown',e=>{
    if(!group.contains(e.target))closeDesktop();
  });
  panel.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeDesktop));
  mobileToggle.addEventListener('click',()=>{
    const opening=mobileToggle.getAttribute('aria-expanded')!=='true';
    mobileToggle.setAttribute('aria-expanded',String(opening));
    mobileToggle.setAttribute('aria-label',opening?'Collapse services submenu':'Expand services submenu');
    mobileToggle.textContent=opening?'−':'+';
    mobileList.hidden=!opening;
  });
  header.addEventListener('keydown',e=>{
    if(e.key==='Escape' && !mobileList.hidden){
      mobileToggle.setAttribute('aria-expanded','false');
      mobileToggle.setAttribute('aria-label','Expand services submenu');
      mobileToggle.textContent='+';
      mobileList.hidden=true;
      mobileToggle.focus();
    }
  });
  mobileList.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
    mobileList.hidden=true;
    mobileToggle.setAttribute('aria-expanded','false');
    mobileToggle.setAttribute('aria-label','Expand services submenu');
    mobileToggle.textContent='+';
  }));
})();
