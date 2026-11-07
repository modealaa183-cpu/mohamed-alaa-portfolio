(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav-links');
  if (menu && nav) {
    menu.addEventListener('click', () => { const isOpen = nav.classList.toggle('is-open'); menu.setAttribute('aria-expanded', String(isOpen)); });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { nav.classList.remove('is-open'); menu.setAttribute('aria-expanded', 'false'); }));
  }
  document.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
    document.querySelectorAll('[data-filter]').forEach(b => { b.classList.remove('active'); b.setAttribute('aria-pressed', 'false'); });
    button.classList.add('active'); button.setAttribute('aria-pressed', 'true');
    document.querySelectorAll('[data-category]').forEach(card => { card.hidden = button.dataset.filter !== 'All' && card.dataset.category !== button.dataset.filter; });
  }));
  const prefix = location.pathname.includes('/work/') ? '../../' : './';
  fetch(prefix + 'site.config.json').then(r => r.json()).then(config => {
    const links = { email: config.email && `mailto:${config.email}`, whatsapp: config.whatsapp && `https://wa.me/${config.whatsapp.replace(/\D/g,'')}`, linkedin: config.linkedin, github: config.github };
    let hasContact = false;
    Object.entries(links).forEach(([key, url]) => { const a = document.querySelector(`[data-contact="${key}"]`); if (a && url) { a.href = url; a.hidden = false; hasContact = true; if (/^https?:/.test(url)) {a.target='_blank';a.rel='noopener noreferrer';} } });
    const placeholder = document.querySelector('.contact-placeholder'); if (placeholder && hasContact) placeholder.hidden = true;
    const form = document.getElementById('contact-form'); if (!form) return;
    const status = document.getElementById('form-status');
    form.addEventListener('submit', async event => {
      event.preventDefault();
      if (!form.reportValidity()) { status.textContent = 'Please complete the required fields with a valid email address.'; return; }
      const fd = new FormData(form);
      if (fd.get('website')) return;
      const payload = Object.fromEntries(fd.entries()); delete payload.website;
      if (config.formEndpoint) {
        const submit = form.querySelector('[type=submit]');submit.disabled=true;
        status.textContent='Submitting your inquiry…';
        try {
          const res=await fetch(config.formEndpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
          if (!res.ok) throw new Error('Form service returned an error.');
          status.textContent='Thanks! Your inquiry was submitted successfully.';form.reset();
        } catch { status.textContent='Your message could not be submitted. Please use a direct contact channel instead.'; }
        finally {submit.disabled=false;}
      } else if(config.email) {
        const subject=encodeURIComponent('Project inquiry — '+payload.service);
        const body=encodeURIComponent(`Name: ${payload.name}\nEmail: ${payload.email}\nCompany: ${payload.company}\nService: ${payload.service}\nBudget: ${payload.budget}\n\n${payload.message}`);
        location.href=`mailto:${config.email}?subject=${subject}&body=${body}`;
        status.textContent='Your email app should open with a prepared draft. Please send it from there; it has not been submitted by this site.';
      } else {
        status.textContent='Inquiry not sent. The site owner must configure an email or form endpoint in site.config.json before contact is available.';
      }
    });
  }).catch(() => { const s=document.getElementById('form-status');if(s)s.textContent='Contact configuration could not be loaded. No message has been sent.'; });
})();
