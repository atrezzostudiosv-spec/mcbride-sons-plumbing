/* ATREZZO — service reviews: CSS infinite rail with keyboard/motion pause.
   No autoplay where reduced motion is requested; all original reviews readable without JS. */
(()=>{const section=document.querySelector(".at-reviews");if(!section)return;
const btn=section.querySelector("[data-review-pause]");if(!btn)return;
section.dataset.motionReady="true";btn.hidden=false;
const reduced=window.matchMedia?.("(prefers-reduced-motion: reduce)");
const update=()=>{const paused=section.dataset.paused==="true";btn.setAttribute("aria-pressed",String(paused));btn.innerHTML=paused?'<span aria-hidden="true">▶</span> Resume motion':'<span aria-hidden="true">Ⅱ</span> Pause motion';btn.disabled=Boolean(reduced?.matches);btn.setAttribute("aria-label",reduced?.matches?"Automatic review movement disabled by reduced-motion preference":paused?"Resume automatic review movement":"Pause automatic review movement");};
btn.addEventListener("click",()=>{section.dataset.paused=section.dataset.paused==="true"?"false":"true";update();});
reduced?.addEventListener?.("change",update);update();
})();
