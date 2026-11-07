# Mohamed Alaa — Portfolio

Premium, responsive and static portfolio focused on client acquisition, real project case studies and marketing technology services.

## Why static HTML/CSS/JS?

GitHub Pages is the primary target. This avoids a framework dependency, makes cold-loads and upkeep simpler, and supports the five case-study routes as real directory indexes. Trade-off: editing layouts and adding components is less modular than React/Astro, though project content lives in `build.py` / `projects.json`.

## Run locally

```bash
python3 build.py
python3 -m http.server 8000
```

Open `http://localhost:8000`. Do not open `index.html` directly with the `file://` protocol: the contact config is fetched over HTTP.

## GitHub Pages publishing

1. Create a **new personal portfolio repository**, ideally `YOUR_USERNAME.github.io`, separate from any employer project. Add these files to its `main` branch.
2. Go to **Settings → Pages → Build and deployment** and set the source to **GitHub Actions**.
3. Push to `main`. `.github/workflows/deploy.yml` builds and publishes the site.
4. For a project repository (rather than `YOUR_USERNAME.github.io`) GitHub serves it under `/<repo>/`. The generated relative URLs work under either location.
5. Verify the live site, case-study routes, navigation and configured contact links after deployment.

The public URL is unknown until a repository is created and Pages completes its deployment.

## Edit contact configuration

Edit `site.config.json`:
- `email`: real email, e.g. `hello@example.com`.
- `whatsapp`: international number with country prefix (digits only recommended).
- `linkedin`, `github`: actual public profile URLs.
- `formEndpoint`: optional real JSON POST endpoint from a form provider. The form **never** claims delivery without a successful response. Configure server-side validation and spam protection at the provider.
- `availability`: currently editable data; adjust the visible availability wording in `build.py` if changing it.

**Important:** If email and endpoint are both blank, the contact form explicitly does not submit. When email is set without an endpoint, it opens the visitor's email application with a prepared draft rather than sending automatically. There are no API credentials on the frontend.

## Edit projects and case studies

The source content is defined in `build.py`'s `projects` array and exported to `projects.json` when `python3 build.py` is run. Edit this source of truth and rerun the build before pushing. Each project gets its own `work/<slug>/index.html` route. Preview art is illustrative and not taken from internal company data. For approved real screenshots, replace generated preview markup and use appropriately optimized assets.

## Content status / missing inputs

- Need real public contact details (email, WhatsApp, LinkedIn, GitHub profile).
- Need explicit publishable screenshots and proven feature/status details for case studies.
- Need a verified CV file before showing Download CV.
- Need a real site URL/domain for production canonical URLs, `sitemap.xml` and absolute Open Graph image URL. These are **not claimed as configured** yet.
- Need confirmed social media / product material publication permission as applicable.
- The visual demo metrics are *qualitative*, not purported results.

## QA

- Static pages and source files can be checked with `python3 test_site.py`.
- Test manually on widths 320, 375, 768, 1024+ using DevTools, keyboard navigation and the real deployed URL.
- Do not treat code generation alone as a passed Lighthouse report or a verified deployed website.
