import json,html,pathlib
root=pathlib.Path(__file__).parent
# Unpack user-approved, original dashboard screenshots at build time.
# GitHub web uploads retain ZIP archives rather than extracting them.
import zipfile
archive=root/'almehwar_real_mockups.zip'
if archive.is_file():
 expected={f'assets/previews/almehwar-real/{name}.webp' for name in
           ('overview','monthly-report','content-intelligence','platforms','website-intelligence')}
 with zipfile.ZipFile(archive) as z:
  available={item.filename for item in z.infolist() if not item.is_dir()}
  if not expected.issubset(available):
   raise RuntimeError('Dashboard archive is missing approved screenshot files')
  for name in expected:
   target=root/name
   target.parent.mkdir(parents=True,exist_ok=True)
   target.write_bytes(z.read(name))
# WEDJAT original, user-supplied screenshots (not AI renders).
wedjat_archive=root/'wedjat_real_mockups.zip'
wedjat_ready=False
if wedjat_archive.is_file():
 wedjat_files={f'assets/previews/wedjat-real/{name}.webp' for name in
               ('landing','features','how-it-works','workspace')}
 with zipfile.ZipFile(wedjat_archive) as archive_file:
  available={item.filename for item in archive_file.infolist() if not item.is_dir()}
  if not wedjat_files.issubset(available):
   raise RuntimeError('WEDJAT image archive is incomplete; check ZIP contents.')
  for name in wedjat_files:
   target=root/name
   target.parent.mkdir(parents=True,exist_ok=True)
   target.write_bytes(archive_file.read(name))
 wedjat_ready=True
# Approved original screenshots of the AlMehwar outpatient clinics website.
clinics_archive=root/'clinics_real_mockups.zip'
clinics_ready=False
if clinics_archive.is_file():
 clinics_files={f'assets/previews/clinics-real/{name}.webp' for name in
                ('home-hero','specialties-grid','clinic-detail','booking-modal')}
 with zipfile.ZipFile(clinics_archive) as z:
  present={item.filename for item in z.infolist() if not item.is_dir()}
  if not clinics_files.issubset(present):
   raise RuntimeError('Clinics screenshots ZIP is missing required files')
  for name in clinics_files:
   dest=root/name
   dest.parent.mkdir(parents=True,exist_ok=True)
   dest.write_bytes(z.read(name))
 clinics_ready=True
projects=[
 dict(slug='identyra-studio',title='Identyra Studio',tag='EMPLOYEE ID AUTOMATION',category='Products',status='Product website & ID studio',summary='A branded employee ID and certificate service with a self-service card studio, Excel uploads and image preparation.',challenge='Preparing employee ID cards from spreadsheets and mixed photo files takes repetitive manual work.',solution='An end-to-end identity card workflow: configure the brand, import employee data and photos, review individual cards and export print-ready files.',role='Product concept, UX design, brand identity and AI-assisted implementation.',tools=['Product Website','Excel Import','Photo Processing','PNG / PDF Export'],features=['Arabic landing page with services and pricing','Company branding and logo upload','Employee spreadsheet and photo import','Card preview, photo adjustment and export'],color='mint',number='01',link='https://identyra-studio.vercel.app/business.html#faq'),
 dict(slug='almehwar-dashboard',title='AlMehwar Social Intelligence',tag='MARKETING ANALYTICS',category='Analytics',status='Internal project / anonymized showcase',summary='A real social intelligence command center integrating monthly reporting, platform performance, content analysis and decisions.',challenge='Performance data lived across different channels and reporting surfaces, making it difficult to compare trends consistently.',solution='A consolidated reporting environment for exploring social performance, website insights and campaign comparisons.',role='Analytics logic, dashboard architecture, reporting workflows and AI-assisted implementation.',tools=['Google Sheets','Apps Script','GA4','Search Console','APIs'],features=['Monthly Report and executive KPIs','Platforms and Content Intelligence','Comparisons and Competitors','Recommendations and Data Health'],color='cyan',number='02'),
 dict(slug='wedjat',title='WEDJAT',tag='INDEPENDENT PRODUCT',category='Products',status='Evolving product',summary='An agency operations and social intelligence workspace for clients, tasks, content calendars, campaigns and analytics.',challenge='Agencies need one place to coordinate client work, publishing and performance reporting without fragmented tools.',solution='An evolving agency workspace bringing together client management, task workflows, content planning and marketing intelligence.',role='Product direction, experience design and AI-assisted implementation.',tools=['Next.js','Vercel','Supabase','OAuth'],features=['Client and agency workflows','Tasks and content calendars','Campaign and reporting views','Product design iteration'],color='violet',number='03',link='https://wedjatapp.com'),
 dict(slug='clinics-landing-page',title='AlMehwar Clinics Schedule',tag='OUTPATIENT CLINICS',category='Web',status='Published clinics schedule',summary='A focused digital schedule for patients to explore outpatient clinics, specialties and doctors appointment information.',challenge='Printed or scattered outpatient schedules make it hard to find a specialty and the right doctor quickly.',solution='A focused, responsive outpatient timetable experience supporting specialty discovery and schedule browsing.',role='Page planning, schedule UX and AI-assisted web UI implementation.',tools=['Responsive UI','UX Design','Schedule Filtering'],features=['Outpatient clinic schedules','Specialty and doctor browsing','Clear timetable presentation','Mobile-friendly access'],color='mint',number='04',link='https://almehwar-clinics-mohamed-alaa4.vercel.app/#'),
 dict(slug='badge-generator',title='Custom Badge Generator',tag='WORKFLOW TOOL',category='Tools',status='Iterative prototype',summary='Turning repetitive badge preparation into a more manageable digital workflow.',challenge='Manually arranging individual photos and details on badges is repetitive and time-consuming.',solution='A tool exploring image upload, image placement, attendee details and export-friendly layouts.',role='Workflow design, interface planning and iterative implementation.',tools=['Web UI','Image Handling','Workflow Design'],features=['Image upload','Positioning and zoom controls','Personalized fields','Output workflow exploration'],color='amber',number='05'),
 dict(slug='marketing-analytics',title='Content & Performance Operations',tag='SOCIAL MEDIA INTELLIGENCE',category='Analytics',status='Experience / Sample workflow',summary='Turning channel-level performance into structured insights for better content decisions.',challenge='High volumes of platform metrics can obscure the lessons behind content performance.',solution='Repeatable approaches to content evaluation, channel reporting and campaign analysis.',role='Social media operations, reporting and interpretation.',tools=['Meta Business Suite','TikTok Analytics','YouTube Analytics','Google Sheets'],features=['Content analysis','Platform comparisons','Competitor reporting','Actionable insights'],color='rose',number='06'),
 dict(slug='healthcare-intelligence-demo',title='ClarityOS — Marketing Intelligence',tag='CUSTOM ANALYTICS PRODUCT',category='Products',status='Independent interactive demo / synthetic data',summary='A rebrandable marketing intelligence dashboard based on the architecture of real reporting workflows, with entirely fictional demo data.',challenge='Marketing teams need a repeatable way to connect channel insights, evaluate content and organize next actions.',solution='A standalone, rebrandable interactive demonstration featuring monthly reporting, platforms, content analysis, website intelligence, comparisons and recommendations.',role='Product concept, workflow design and demo implementation informed by experience building marketing dashboards.',tools=['Interactive Web Demo','Synthetic Data','Marketing Analytics','Custom Branding'],features=['Monthly reports and platform intelligence','Content analysis and quality controls','Comparisons, competitors and recommendations','Brand customization and sample exports'],color='mint',number='07',link='https://clarityos-intelligence-demo.vercel.app'),
]
(root/'projects.json').write_text(json.dumps(projects,indent=2),encoding='utf-8')
config={'name':'Mohamed Alaa','title':'Marketing Technology & AI Solutions Specialist','email':'','whatsapp':'','linkedin':'','github':'','availability':True,'siteUrl':'','formEndpoint':''}
if not (root/'site.config.json').exists():
 (root/'site.config.json').write_text(json.dumps(config,indent=2),encoding='utf-8')
def e(s):return html.escape(str(s),quote=True)
def visual(p,large=False):
 return f'''<div class="project-art art-{p['color']} {'project-art-large' if large else ''}" aria-hidden="true"><div class="art-top"><span class="art-dots"><i></i><i></i><i></i></span><span>INTELLIGENCE / {p['number']}</span></div><div class="art-interface"><div class="art-rail"><b></b><b></b><b></b><b></b></div><div class="art-main"><div class="art-lines"><span></span><span></span></div><div class="art-stats"><div><small>INSIGHT</small><strong>↗</strong></div><div><small>ANALYSIS</small><strong>◎</strong></div><div><small>SYSTEM</small><strong>⌁</strong></div></div><svg viewBox="0 0 360 140" preserveAspectRatio="none"><defs><linearGradient id="fill-{p['number']}" x1="0" x2="0" y1="0" y2="1"><stop stop-color="currentColor" stop-opacity=".27"/><stop offset="1" stop-color="currentColor" stop-opacity="0"/></linearGradient></defs><path d="M0 115 C40 110 38 50 86 78 S146 125 189 68 244 89 284 35 327 62 360 14 L360 140 L0 140Z" fill="url(#fill-{p['number']})"/><path d="M0 115 C40 110 38 50 86 78 S146 125 189 68 244 89 284 35 327 62 360 14" fill="none" stroke="currentColor" stroke-width="3"/></svg><div class="art-bottom"><span></span><span></span><span></span></div></div></div></div>'''
def head(title,description,depth=0):
 prefix='../'*depth
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#080e18"><meta name="description" content="{e(description)}"><title>{e(title)} | Mohamed Alaa</title><link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg"><link rel="stylesheet" href="{prefix}assets/styles.css"><meta property="og:type" content="website"><meta property="og:title" content="{e(title)} | Mohamed Alaa"><meta property="og:description" content="{e(description)}"><meta property="og:image" content="{prefix}assets/og.svg"><script defer src="{prefix}assets/site.js"></script></head><body>'''
def header(depth=0):
 prefix='../'*depth
 return f'''<header class="nav-wrap"><nav class="nav container" aria-label="Main navigation"><a class="brand" href="{prefix}index.html" aria-label="Mohamed Alaa home"><img class="ma-logo" src="{prefix}assets/ma-mark.svg" alt="" width="46" height="34"><span class="brand-name">MOHAMED ALAA<small>MARKETING × TECHNOLOGY</small></span></a><button class="menu-toggle" type="button" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button><div class="nav-links" id="nav-links"><a href="{prefix}index.html#home">Home</a><a href="{prefix}index.html#services">Services</a><a href="{prefix}index.html#work">Work</a><a href="{prefix}index.html#contact">Contact</a></div><a class="nav-cta" href="{prefix}index.html#contact">Hire Me <span aria-hidden="true">↗</span></a></nav></header>'''
def footer(depth=0):
 prefix='../'*depth
 return f'''<footer class="footer"><div class="container footer-inner"><a class="footer-brand" href="{prefix}index.html" aria-label="Mohamed Alaa"><img class="ma-logo" src="{prefix}assets/ma-mark.svg" alt="" width="46" height="34"></a><span>Independent thinking. Practical solutions.</span><span>© 2026 Mohamed Alaa</span><a href="#top">Back to top ↑</a></div></footer></body></html>'''
def preview_path(p):
 if p['slug']=='almehwar-dashboard': return 'assets/previews/almehwar-real/overview.webp'
 if p['slug']=='wedjat' and wedjat_ready: return 'assets/previews/wedjat-real/landing.webp'
 if p['slug']=='clinics-landing-page' and clinics_ready: return 'assets/previews/clinics-real/home-hero.webp'
 ext='avif' if p['slug']=='identyra-studio' else 'svg'
 return 'assets/previews/'+p['slug']+'.'+ext
def projectcard(p):
 return f'''<a class="project-card" data-category="{p['category']}" href="work/{p['slug']}/"><div class="project-card-art"><img src="{preview_path(p)}" alt="{e('Actual Identyra Studio website collage' if p['slug']=='identyra-studio' else 'Illustrative demo preview of '+p['title'])}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block"/></div><div class="project-card-info"><div class="project-eyebrow">{p['tag']} <span>/{p['number']}</span></div><h3>{p['title']} <span class="project-arrow" aria-hidden="true">↗</span></h3><p>{p['summary']}</p><div class="project-meta"><span>{p['status']}</span><span>View case study ↗</span></div></div></a>'''
services=[('01','chart-no-axes-combined','Marketing Dashboards & Reporting','Make performance easier to understand.','Custom KPI views, channel reports, campaign comparisons and Google Sheets automation.'),('02','workflow','AI & Workflow Automation','Spend less time on repetitive work.','Automated reporting, data synchronization, AI-assisted summaries and lightweight workflows.'),('03','panels-top-left','Landing Pages & Websites','Give your next visitor a better experience.','Responsive landing pages, campaign experiences, lead-generation pages and performance setup.'),('04','radar','Social Media Analytics & Strategy','Find the signal behind the metrics.','Channel audits, content analysis, competitor reporting and actionable recommendations.'),('05','blocks','AI-Assisted Digital Solutions','Build a tool around your actual process.','Internal interfaces, workflow utilities, reporting tools and practical prototypes.')]
service_icons=['◫','⤳','▣','◎','▧']
service_html=''.join(f'''<article class="service-card"><div class="service-card-top"><span class="service-symbol">{service_icons[i]}</span><span class="service-number">{x[0]}</span></div><h3>{x[2]}</h3><strong>{x[3]}</strong><p>{x[4]}</p><a href="#contact">Discuss a project <span aria-hidden="true">↗</span></a></article>''' for i,x in enumerate(services))
home=head('Marketing Technology & AI Solutions Specialist','Dashboards, automation, marketing analytics and better digital experiences built by Mohamed Alaa.')+header()+'''
<main id="top"><section id="home" class="hero hero-editorial container">
<div class="hero-content"><p class="hero-kicker"><span class="kicker-dot"></span> MARKETING × DATA × AI</p>
<h1>Marketing<br>Technology &amp;<br><em>AI Solutions.</em></h1>
<p class="hero-description">I build dashboards, digital tools and smarter workflows that make business simpler.</p>
<div class="hero-actions"><a class="btn btn-primary" href="#work">View My Work <span>↗</span></a><a class="btn btn-outline" href="#contact">Let's Talk <span>↗</span></a></div>
</div><div class="hero-portrait" aria-label="Mohamed Alaa portrait"><span class="hero-big-mark" aria-hidden="true">MA</span><img class="hero-person" src="assets/mohamed-hero-cutout.webp" width="620" height="849" alt="Mohamed Alaa wearing a cream blazer and black shirt" fetchpriority="high" decoding="async"><span class="hero-portrait-caption">MOHAMED ALAA&nbsp; / &nbsp;EGYPT</span></div></section>
<section id="work" class="section work-section"><div class="container"><div class="section-head"><div><p class="eyebrow"><span class="eyebrow-line"></span> 01 / SELECTED WORK</p><h2>Selected work.<br><em>Real solutions.</em></h2></div><p>Products, dashboards and digital experiences.</p></div><div class="filters" aria-label="Filter projects"><button class="filter active" type="button" data-filter="All" aria-pressed="true">All Work</button><button class="filter" type="button" data-filter="Analytics" aria-pressed="false">Analytics</button><button class="filter" type="button" data-filter="Products" aria-pressed="false">Products</button><button class="filter" type="button" data-filter="Web" aria-pressed="false">Web</button><button class="filter" type="button" data-filter="Tools" aria-pressed="false">Tools</button></div><div class="project-grid">'''+''.join(projectcard(p) for p in projects)+'''</div><p class="work-note">Project previews are demos with fictional information.</p></div></section>

<section id="services" class="section container"><div class="section-head"><div><p class="eyebrow"><span class="eyebrow-line"></span> 02 / SERVICES</p><h2>What I can<br><em>build for you.</em></h2></div><p>Useful digital solutions tailored to your business.</p></div><div class="services-grid">'''+service_html+'''</div></section>

<section id="contact" class="section container contact-section"><div class="contact-top"><p class="eyebrow"><span class="eyebrow-line"></span> 03 / CONTACT</p><span class="contact-spark">✳</span></div><h2>Have a project<br><em>in mind?</em></h2><p>Let's build something useful.</p><div class="contact-layout"><div class="contact-form-panel"><form id="contact-form" novalidate><div class="field-row"><label>Your name <input name="name" required autocomplete="name" placeholder="Your name"></label><label>Email address <input name="email" type="email" required autocomplete="email" placeholder="you@company.com"></label></div><div class="field-row"><label>Company <small>(optional)</small><input name="company" placeholder="Company / organization"></label><label>What do you need?<select name="service" required><option value="">Select a service</option><option>Marketing Dashboards & Reporting</option><option>AI & Workflow Automation</option><option>Landing Pages & Websites</option><option>Social Media Analytics & Strategy</option><option>AI-Assisted Digital Solutions</option><option>Other / Not sure</option></select></label></div><label>Tell me about the project <textarea name="message" required rows="5" placeholder="What are you looking to solve?"></textarea></label><label>Budget range <small>(optional)</small><select name="budget"><option value="">Prefer to discuss</option><option>Under $500</option><option>$500–$1,500</option><option>$1,500–$5,000</option><option>$5,000+</option></select></label><div class="hidden-trap" aria-hidden="true"><label>Leave empty<input name="website" tabindex="-1" autocomplete="off"></label></div><button class="btn btn-primary" type="submit">Prepare My Inquiry <span>↗</span></button><p class="form-status" id="form-status" role="status">Contact details are not configured yet. This form will never pretend a message was sent.</p></form></div><div class="contact-side"><span class="contact-side-label">CONTACT ME</span><a class="contact-link" data-contact="email" hidden href="#">Email <span>↗</span></a><a class="contact-link" data-contact="whatsapp" hidden href="#">WhatsApp <span>↗</span></a><a class="contact-link" data-contact="linkedin" hidden href="#">LinkedIn <span>↗</span></a><a class="contact-link" data-contact="github" hidden href="#">GitHub <span>↗</span></a><p class="contact-placeholder">Contact links will appear once the real details are added to <code>site.config.json</code>.</p><div class="contact-availability"><span class="live-dot"></span> OPEN TO FREELANCE COLLABORATIONS</div></div></div></section></main>'''+footer()
(root/'index.html').write_text(home,encoding='utf-8')
def demo_gallery(p):
 if p['slug']=='clinics-landing-page' and clinics_ready:
  pages=[('specialties-grid','Specialties & Clinics'),('clinic-detail','Doctors & Schedules'),('booking-modal','Appointment Booking Flow')]
  figures=''.join('<figure><img loading="lazy" src="../../assets/previews/clinics-real/'+name+'.webp" alt="Original clinics interface screenshot — '+label+'"><figcaption>'+label+'</figcaption></figure>' for name,label in pages)
  return '<section class="case-gallery" aria-label="Actual outpatient clinics website screenshots"><h2>Explore the clinics experience</h2><p>Original screenshots from the outpatient clinics website, presented within a consistent browser frame.</p><div class="case-gallery-grid">'+figures+'</div></section>'
 if p['slug']=='wedjat' and wedjat_ready:
  pages=[('features','Platform Features'),('how-it-works','How It Works'),('workspace','Actual Workspace — private labels concealed')]
  figures=''.join('<figure><img loading="lazy" src="../../assets/previews/wedjat-real/'+name+'.webp" alt="Real WEDJAT screenshot: '+label+'"><figcaption>'+label+'</figcaption></figure>' for name,label in pages)
  return '<section class="case-gallery" aria-label="WEDJAT real screenshots"><h2>Inside WEDJAT</h2><p>Original product screenshots presented within a fixed browser frame. Some internal labels are obscured for privacy.</p><div class="case-gallery-grid">'+figures+'</div></section>'
 if p['slug']!='almehwar-dashboard': return ''
 return '''<section class="case-gallery" aria-label="Dashboard screenshots"><h2>Inside the dashboard</h2><p>Actual screenshots of the supplied synthetic-data demonstration, shown inside consistent browser frames.</p><div class="case-gallery-grid"><figure><img loading="lazy" src="../../assets/previews/almehwar-real/monthly-report.webp" alt="Monthly Report demo screenshot" ><figcaption>Monthly Report</figcaption></figure><figure><img loading="lazy" src="../../assets/previews/almehwar-real/content-intelligence.webp" alt="Content Intelligence demo screenshot" ><figcaption>Content Intelligence</figcaption></figure><figure><img loading="lazy" src="../../assets/previews/almehwar-real/platforms.webp" alt="Platforms demo screenshot" ><figcaption>Platforms</figcaption></figure><figure><img loading="lazy" src="../../assets/previews/almehwar-real/website-intelligence.webp" alt="Website Intelligence demo screenshot" ><figcaption>Website Intelligence</figcaption></figure></div></section>'''
for p in projects:
 d=root/'work'/p['slug'];d.mkdir(parents=True,exist_ok=True)
 items=''.join(f'<span>{e(t)}</span>' for t in p['tools']); feats=''.join(f'<li><span>↗</span>{e(t)}</li>' for t in p['features'])
 ext=f'<a class="btn btn-outline" href="{e(p["link"])}" target="_blank" rel="noopener noreferrer">{"Open interactive demo" if p["slug"] == "healthcare-intelligence-demo" else "Visit product website"} ↗</a>' if p.get('link') else ''
 page=head(p['title'],p['summary'],2)+header(2)+f'''<main id="top"><section class="case-hero container"><a class="back-link" href="../../index.html#work">← Back to all projects</a><div class="case-meta"><span>{e(p['tag'])}</span><span>{e(p['status'])}</span></div><h1>{e(p['title'])}<span class="period">.</span></h1><p>{e(p['summary'])}</p><div class="case-hero-art"><img src="../../{preview_path(p)}" alt="{e('Actual Identyra Studio website collage' if p['slug']=='identyra-studio' else 'Illustrative demo interface for '+p['title'])}" loading="eager" style="width:100%;height:auto;display:block;border-radius:15px"/></div><p class="case-disclaimer">{'Actual Identyra Studio screenshots supplied by the project owner; no private employee records.' if p['slug']=='identyra-studio' else 'DEMO VERSION — Representative interface illustration using fictional sample data only. No real business, employee, or patient data is shown.'}</p>{demo_gallery(p)}</section><section class="case-content container"><div class="case-sidebar"><p class="eyebrow"><span class="eyebrow-line"></span> PROJECT {p['number']}</p><h3>Overview</h3><div class="tool-tags">{items}</div></div><div class="case-story"><div class="case-block"><span>01 / THE CHALLENGE</span><h2>The problem.</h2><p>{e(p['challenge'])}</p></div><div class="case-block"><span>02 / THE APPROACH</span><h2>The solution.</h2><p>{e(p['solution'])}</p></div><div class="case-block"><span>03 / MY CONTRIBUTION</span><h2>What I worked on.</h2><p>{e(p['role'])}</p></div><div class="case-block"><span>04 / THE EXPERIENCE</span><h2>Key areas.</h2><ul class="feature-list">{feats}</ul></div><div class="case-block"><span>05 / OUTCOME & LEARNINGS</span><h2>What matters.</h2><p>This case study focuses on the workflow and design approach. Demo visualizations use fictional data. Quantitative outcomes and feature availability are not claimed without independent verification. Iteration and user feedback continue to shape how the solution evolves.</p>{ext}</div></div></section><section class="next-project container"><p class="eyebrow"><span class="eyebrow-line"></span> KEEP EXPLORING</p><a href="../{projects[(projects.index(p)+1)%len(projects)]['slug']}/">Next project <span>{e(projects[(projects.index(p)+1)%len(projects)]['title'])} ↗</span></a></section><section class="case-cta container"><h2>Working on something similar?</h2><a class="btn btn-primary" href="../../index.html#contact">Let's discuss it ↗</a></section></main>'''+footer(2)
 (d/'index.html').write_text(page,encoding='utf-8')
(root/'404.html').write_text(head('Page Not Found','The page you requested could not be found.')+header()+'''<main class="notfound container"><p class="eyebrow">404 / NOT FOUND</p><h1>Lost in the data?</h1><p>This page isn't here. Let's get you back to the good stuff.</p><a class="btn btn-primary" href="./index.html">Go home ↗</a></main>'''+footer(),encoding='utf-8')
(root/'robots.txt').write_text('User-agent: *\nAllow: /\n',encoding='utf-8')
(root/'.nojekyll').write_text('',encoding='utf-8')
# Generate canonical URLs and sitemap only after a verified public site URL is configured.
config=json.loads((root/'site.config.json').read_text(encoding='utf-8'))
base=config.get('siteUrl','').strip().rstrip('/')
if base.startswith('https://'):
 from xml.sax.saxutils import escape as xml_escape
 urls=['/',*['/work/'+p['slug']+'/' for p in projects]]
 entries=[]
 for url in urls:
  file=root/'index.html' if url=='/' else root/url.lstrip('/')/'index.html'
  if file.exists():
   content=file.read_text(encoding='utf-8')
   canonical=base+url
   content=content.replace('</head>',f'<link rel="canonical" href="{html.escape(canonical,quote=True)}"><meta property="og:url" content="{html.escape(canonical,quote=True)}"><meta property="og:image" content="{html.escape(base,quote=True)}/assets/og.svg"></head>')
   file.write_text(content,encoding='utf-8')
   entries.append('<url><loc>'+xml_escape(canonical)+'</loc></url>')
 (root/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(entries)+'</urlset>',encoding='utf-8')
 (root/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n',encoding='utf-8')
else:
 (root/'sitemap.xml').unlink(missing_ok=True)
print('Generated',len(projects),'project pages')
