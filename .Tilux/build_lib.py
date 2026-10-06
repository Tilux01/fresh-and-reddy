
import os
ICON = {
 "cup":'<svg viewBox="0 0 24 24"><path d="M6 5h12l-1.2 13.2A3 3 0 0 1 13.8 21h-3.6a3 3 0 0 1-3-2.8L6 5z"/><path d="M5 5h14"/></svg>',
 "truck":'<svg viewBox="0 0 24 24"><path d="M2 7h11v9H2z"/><path d="M13 10h4l4 4v2h-8z"/><circle cx="6" cy="18.5" r="1.6"/><circle cx="17" cy="18.5" r="1.6"/></svg>',
 "machine":'<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="2.5"/><path d="M8 9h4v4H8z"/><path d="M15 9v7"/><path d="M8 16.5h8"/></svg>',
 "leaf":'<svg viewBox="0 0 24 24"><path d="M20 4c0 9-6.5 14-14 14 0-9 6.5-14 14-14z"/><path d="M6 18L18 6"/></svg>',
 "shield":'<svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 5-3 8.2-7 9-4-.8-7-4-7-9V6l7-3z"/><path d="M9.5 12.5l2 2 3.5-4"/></svg>',
 "clock":'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.2"/><path d="M12 7.4V12l3 2"/></svg>',
 "users":'<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.2"/><path d="M3.2 20c0-3.4 2.6-6.2 5.8-6.2S14.8 16.6 14.8 20"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6.1"/><path d="M21 20c0-2.6-1.6-4.8-3.9-5.7"/></svg>',
 "spark":'<svg viewBox="0 0 24 24"><path d="M12 3.5v5.5M12 15v5.5M3.5 12H9M15 12h5.5"/><circle cx="12" cy="12" r="1.3"/></svg>',
 "drop":'<svg viewBox="0 0 24 24"><path d="M12 3.5s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11z"/></svg>',
 "check":'<svg viewBox="0 0 24 24"><path d="M4.5 12.5l5 5 10-10.5"/></svg>',
 "wrench":'<svg viewBox="0 0 24 24"><path d="M14.5 6.2a4.2 4.2 0 0 1 5.3 5.3l-8.6 8.6-5.3-5.3 8.6-8.6z"/><path d="M7.5 16.5l-1.5 1.5"/></svg>',
 "bag":'<svg viewBox="0 0 24 24"><path d="M6 8h12l1 12H5L6 8z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/></svg>',
 "gauge":'<svg viewBox="0 0 24 24"><path d="M4 16a8 8 0 0 1 16 0"/><path d="M12 16l4-4"/></svg>',
 "headset":'<svg viewBox="0 0 24 24"><path d="M4 13v-1a8 8 0 0 1 16 0v1"/><rect x="3" y="13" width="4" height="6" rx="2"/><rect x="17" y="13" width="4" height="6" rx="2"/></svg>',
}
STAR='<svg viewBox="0 0 24 24"><path d="M12 3.4l2.6 5.4 5.9.9-4.3 4.1 1 5.9L12 17l-5.2 2.7 1-5.9L3.5 9.7l5.9-.9z"/></svg>'
FB='<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4.5"/><path d="M13.6 20v-6.6h2.2l.4-2.6h-2.6V9.2c0-.8.2-1.3 1.4-1.3h1.3V5.6c-.6-.1-1.4-.1-2.2-.1-2.2 0-3.6 1.3-3.6 3.7v1.6H8.4v2.6h2.1V20"/></svg>'
IG='<svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4.5"/><circle cx="12" cy="12" r="3.4"/><circle cx="16.7" cy="7.3" r=".9"/></svg>'
NAVITEMS=[("Home","index.html"),("About","about.html"),("Coffee Tasting","coffee-tasting.html"),
          ("Services","services.html"),("Equipment","equipment.html"),("Culture","culture.html"),("Contact Us","contact.html")]

def head(title,desc):
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<script>document.documentElement.className+=" js";</script>\n'
            f'<title>{title}</title>\n<meta name="description" content="{desc}">\n'
            '<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Montserrat:wght@600;700;800;900&display=swap" rel="stylesheet">\n'
            '<link rel="stylesheet" href="assets/css/styles.css?v=1">\n</head>\n')
def nav(active):
    links="".join('<a href="%s"%s>%s</a>'%(h,' class="is-active"' if n==active else '',n) for n,h in NAVITEMS)
    return ('<header class="site-nav">\n<div class="nav-inner">\n'
            '<a class="brand" href="index.html" aria-label="Fresh and Reddy home">'
            '<span class="brand-name">Fresh</span><span class="brand-name"><span class="amp">&amp;</span> Reddy</span></a>\n'
            '<nav class="nav-links" aria-label="Primary">'+links+'</nav>\n'
            '<button class="nav-toggle" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>\n'
            '</div>\n<div class="nav-panel">'+links+'</div>\n</header>\n')
def site_footer():
    cols=[("Company",[("About","about.html"),("Culture","culture.html"),("Contact Us","contact.html")]),
          ("Services",[("Coffee Tasting","coffee-tasting.html"),("Office Supply","services.html"),("Equipment","equipment.html")]),
          ("Explore",[("Book a Free Trial","contact.html"),("Our Services","services.html"),("Coffee Tasting","coffee-tasting.html")])]
    colhtml="".join('<div class="footer-col"><h4>'+c+'</h4>'+"".join('<a href="%s">%s</a>'%(h,n) for n,h in items)+'</div>' for c,items in cols)
    tax="".join('<span>%s</span>'%t + ('<span class="sep">&#9679;</span>' if i<4 else '') for i,t in enumerate(["Coffee","Tea","Water","Snacks","Delivered"]))
    return ('<footer class="site-footer">\n<div class="container">\n<div class="footer-grid">\n'
            '<div class="footer-brand"><a class="brand" href="index.html"><span class="brand-name">Fresh</span>'
            '<span class="brand-name"><span class="amp">&amp;</span> Reddy</span></a>'
            '<p>Specialty coffee, tea, water and pantry supply for offices that refuse to settle for the breakroom standard. Roasted, delivered and serviced end to end.</p>'
            '<div class="taxonomy" style="margin-top:20px">'+tax+'</div></div>\n'+colhtml+'\n</div>\n'
            '<div class="footer-bottom">\n<span>&copy; <span data-year>2025</span> Fresh &amp; Reddy. All rights reserved.</span>\n'
            '<div class="footer-social"><a class="icon-btn" href="https://www.facebook.com/" target="_blank" rel="noopener" aria-label="Facebook">'+FB+'</a>'
            '<a class="icon-btn" href="https://www.instagram.com/" target="_blank" rel="noopener" aria-label="Instagram">'+IG+'</a></div>\n'
            '</div>\n</div>\n</footer>\n')
def scripts():
    return '<script src="assets/js/main.js?v=1"></script>\n</body>\n</html>\n'
def section(tag,title,sub,inner,alt=False):
    cls="section alt" if alt else "section"
    h=('<div class="section-head reveal">'+(('<span class="section-tag">%s</span>'%tag) if tag else '')
       +'<h2 class="section-title">%s</h2>'%title+(('<p class="section-sub">%s</p>'%sub) if sub else '')+'</div>')
    return '<section class="%s">\n<div class="container">\n%s\n%s\n</div>\n</section>\n'%(cls,h,inner)
def page_hero(cur,title,lede):
    return ('<section class="page-hero">\n<div class="container">\n<nav class="breadcrumb"><a href="index.html">Home</a>'
            '<span>/</span><span class="cur">%s</span></nav>\n<h1 class="page-title">%s</h1>\n<p class="page-lede">%s</p>\n</div>\n</section>\n'%(cur,title,lede))
def card(icon,title,body,extra=""):
    return '<article class="card reveal"><div class="card-icon">%s</div><h3>%s</h3><p>%s</p>%s</article>'%(ICON[icon],title,body,extra)
def card_list(items):
    return '<ul class="card-list">'+"".join('<li>%s</li>'%i for i in items)+'</ul>'
def faq(items):
    out='<div class="faq reveal">'
    for q,a in items:
        out+='<div class="faq-item"><button class="faq-q" aria-expanded="false">%s<span class="faq-icon"></span></button><div class="faq-a"><p>%s</p></div></div>'%(q,a)
    return out+'</div>'
def quote(text,by):
    return '<article class="quote reveal"><div class="quote-stars">%s</div><blockquote>%s</blockquote><span class="quote-by">%s</span></article>'%(STAR*5,text,by)
def cta_band(title,sub,btn,bhref):
    return ('<section class="section">\n<div class="container">\n<div class="cta-band reveal">\n<div><h2>%s</h2><p>%s</p></div>\n'
            '<a class="btn btn-primary btn-lg" href="%s">%s</a>\n</div>\n</div>\n</section>\n'%(title,sub,bhref,btn))
def steps(items):
    out='<div class="steps reveal">'
    for i,(t,d) in enumerate(items):
        out+='<div class="step"><span class="step-num">%02d</span><h3>%s</h3><p>%s</p></div>'%(i+1,t,d)
    return out+'</div>'
def stats(items):
    out='<div class="stat-row reveal">'
    for val,suf,lab in items:
        out+='<div class="stat"><div class="stat-value" data-count="%s" data-suffix="%s">0%s</div><div class="stat-label">%s</div></div>'%(val,suf,suf,lab)
    return out+'</div>'
def person(ini,name,role,bio):
    return ('<article class="person reveal"><div class="person-media"><span class="initials">%s</span></div>'
            '<div class="person-body"><h3>%s</h3><span class="person-role">%s</span><p>%s</p></div></article>'%(ini,name,role,bio))
def wrap(title,desc,active,body):
    return head(title,desc)+nav(active)+'<main>\n'+body+'</main>\n'+site_footer()+scripts()
