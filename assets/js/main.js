
(function(){
  'use strict';
  document.documentElement.classList.add('js');

  var nav = document.querySelector('.site-nav');
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.querySelector('.nav-panel');
  var lastY = window.pageYOffset;

  function onScroll(){
    var y = window.pageYOffset;
    if(nav){
      if(y > 90 && y > lastY + 4){ nav.classList.add('nav-hidden'); }
      else { nav.classList.remove('nav-hidden'); }
    }
    lastY = y;
  }
  window.addEventListener('scroll', onScroll, { passive:true });

  if(toggle && panel){
    toggle.addEventListener('click', function(){
      var open = panel.classList.toggle('is-open');
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    panel.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){
        panel.classList.remove('is-open');
        toggle.classList.remove('is-open');
        toggle.setAttribute('aria-expanded','false');
      });
    });
  }

  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var dots = Array.prototype.slice.call(document.querySelectorAll('.dot'));
  var current = 0;
  var timer = null;
  var DELAY = 6500;

  function goTo(i){
    if(!slides.length) return;
    current = (i + slides.length) % slides.length;
    slides.forEach(function(s, idx){ s.classList.toggle('is-active', idx === current); });
    dots.forEach(function(d, idx){
      d.classList.toggle('is-active', idx === current);
      d.setAttribute('aria-current', idx === current ? 'true' : 'false');
    });
  }
  function next(){ goTo(current + 1); }
  function prev(){ goTo(current - 1); }
  function restart(){
    if(timer) clearInterval(timer);
    if(slides.length > 1) timer = setInterval(next, DELAY);
  }

  dots.forEach(function(d, idx){
    d.addEventListener('click', function(){ goTo(idx); restart(); });
  });
  document.querySelectorAll('[data-carousel="next"]').forEach(function(b){
    b.addEventListener('click', function(){ next(); restart(); });
  });
  document.querySelectorAll('[data-carousel="prev"]').forEach(function(b){
    b.addEventListener('click', function(){ prev(); restart(); });
  });

  var hero = document.querySelector('.hero');
  if(hero && slides.length > 1){
    var startX = 0, startY = 0, tracking = false;
    hero.addEventListener('touchstart', function(e){
      var t = e.changedTouches[0];
      startX = t.clientX; startY = t.clientY; tracking = true;
    }, { passive:true });
    hero.addEventListener('touchend', function(e){
      if(!tracking) return;
      tracking = false;
      var t = e.changedTouches[0];
      var dx = t.clientX - startX;
      var dy = t.clientY - startY;
      if(Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)){
        if(dx < 0){ next(); } else { prev(); }
        restart();
      }
    }, { passive:true });
  }
  restart();

  var pullStart = 0, pulling = false;
  var indicator = document.querySelector('.pull-indicator');
  document.addEventListener('touchstart', function(e){
    if(window.pageYOffset <= 0){ pullStart = e.touches[0].clientY; pulling = true; }
  }, { passive:true });
  document.addEventListener('touchmove', function(e){
    if(!pulling || !indicator) return;
    var dist = e.touches[0].clientY - pullStart;
    if(dist > 0 && window.pageYOffset <= 0){
      indicator.style.opacity = Math.min(dist / 90, 1);
      indicator.style.transform = 'translate(-50%,' + Math.min(dist / 2, 46) + 'px)';
    }
  }, { passive:true });
  document.addEventListener('touchend', function(e){
    if(!pulling || !indicator) return;
    pulling = false;
    indicator.style.opacity = 0;
    indicator.style.transform = 'translate(-50%,0)';
    if(window.pageYOffset <= 0 && indicator.dataset.armed === '1'){
      goTo(0); restart();
    }
  }, { passive:true });
  if(indicator){ indicator.dataset.armed = '1'; }

  var revealItems = Array.prototype.slice.call(document.querySelectorAll('.reveal'));
  function show(el){ el.classList.add('is-visible'); }
  if('IntersectionObserver' in window){
    var obs = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){ show(entry.target); obs.unobserve(entry.target); }
      });
    }, { threshold:0, rootMargin:'0px 0px -40px 0px' });
    revealItems.forEach(function(el){
      var r = el.getBoundingClientRect();
      if(r.top < window.innerHeight && r.bottom > 0){ show(el); }
      else { obs.observe(el); }
    });
  } else {
    revealItems.forEach(show);
  }
  window.setTimeout(function(){ revealItems.forEach(show); }, 2200);

  var counters = Array.prototype.slice.call(document.querySelectorAll('[data-count]'));
  function runCounter(el){
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1400, t0 = null;
    function frame(ts){
      if(!t0) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = target * eased;
      el.textContent = (target % 1 === 0 ? Math.round(val) : val.toFixed(1)) + suffix;
      if(p < 1) requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);
  }
  if('IntersectionObserver' in window){
    var cObs = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){ runCounter(entry.target); cObs.unobserve(entry.target); }
      });
    }, { threshold:.4 });
    counters.forEach(function(el){ cObs.observe(el); });
  } else {
    counters.forEach(runCounter);
  }

  document.querySelectorAll('.faq-item').forEach(function(item){
    var btn = item.querySelector('.faq-q');
    var ans = item.querySelector('.faq-a');
    if(!btn || !ans) return;
    btn.addEventListener('click', function(){
      var open = item.classList.contains('is-open');
      if(open){
        ans.style.maxHeight = '0px';
        item.classList.remove('is-open');
        btn.setAttribute('aria-expanded','false');
      } else {
        item.classList.add('is-open');
        ans.style.maxHeight = ans.scrollHeight + 'px';
        btn.setAttribute('aria-expanded','true');
      }
    });
  });

  function validateField(input){
    var field = input.closest('.field');
    if(!field) return true;
    var value = (input.value || '').trim();
    var ok = true;
    if(input.hasAttribute('required') && !value){ ok = false; }
    if(ok && input.type === 'email' && value){
      ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }
    field.classList.toggle('is-invalid', !ok);
    return ok;
  }

  document.querySelectorAll('form[data-validate]').forEach(function(form){
    form.querySelectorAll('input,select,textarea').forEach(function(input){
      input.addEventListener('blur', function(){ validateField(input); });
      input.addEventListener('input', function(){
        if(input.closest('.field') && input.closest('.field').classList.contains('is-invalid')) validateField(input);
      });
    });
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var valid = true;
      form.querySelectorAll('input,select,textarea').forEach(function(input){
        if(!validateField(input)) valid = false;
      });
      var success = form.parentElement.querySelector('.form-success') || form.querySelector('.form-success');
      if(!valid){
        var firstBad = form.querySelector('.field.is-invalid input,.field.is-invalid select,.field.is-invalid textarea');
        if(firstBad) firstBad.focus();
        return;
      }
      var payload = {};
      form.querySelectorAll('input,select,textarea').forEach(function(input){
        if(input.name) payload[input.name] = input.value;
      });
      payload._time = new Date().toISOString();
      try{
        var store = JSON.parse(localStorage.getItem('fr_leads') || '[]');
        store.push(payload);
        localStorage.setItem('fr_leads', JSON.stringify(store));
      }catch(err){}
      if(success){
        success.classList.add('is-shown');
        success.textContent = form.getAttribute('data-success') || 'Thanks. Your request is in and the team will be in touch within one working day.';
      }
      form.reset();
      window.setTimeout(function(){ if(success) success.classList.remove('is-shown'); }, 7000);
    });
  });

  document.querySelectorAll('a[href^="#"]').forEach(function(link){
    link.addEventListener('click', function(e){
      var id = link.getAttribute('href');
      if(id.length < 2) return;
      var target = document.querySelector(id);
      if(!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior:'smooth', block:'start' });
    });
  });

  document.querySelectorAll('[data-year]').forEach(function(el){
    el.textContent = new Date().getFullYear();
  });
})();
