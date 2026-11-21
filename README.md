# BRO Nexus — PC Toolkit & NEXUS Engineering Suite

**Website name:** BRO Nexus  
**Website:** https://zaboylah-cell.github.io/Nexus-Engineering-Suite/  
**Description:** BRO Nexus is the official home of BRO PC Toolkit and NEXUS Engineering Suite: a cross-platform collection of local-first PC utilities and engineering tools for Windows, macOS and the web.

## Website
Enable GitHub Pages in **Settings → Pages → Deploy from branch → main → /(root)**. The website uses one HTML interface and loads its public site configuration from `site.json`.

## Included tools
- System overview (desktop)
- Disk manager with read-only drive capacity (desktop)
- File organizer preview (desktop; no automatic moves/deletes)
- App launcher and operating-system settings shortcuts (desktop)
- Network connectivity diagnostics (desktop)
- Security Center shortcuts (desktop)
- Web shortcuts
- Engineering calculators and developer tools: Ohm's law, resistor decoder, subnet calculator, JSON formatter, Base64, regex, number/unit conversions, timestamp converter, notes and more

## Desktop editions — no Python
The Windows and macOS apps use Electron with HTML, CSS and JavaScript. The same root `index.html` is used by the website and desktop app. No Python runtime is used.

### Run from source
Install Node.js 22 or later, then:
```bash
npm install
npm start
```

### Build packages
```bash
npm run build:win
npm run build:mac
```
Windows builds produce an installer and portable EXE. macOS builds produce a DMG and ZIP app bundle. Build each platform on its matching GitHub Actions runner.

## Releases
Push a version tag such as `v1.0.0`. GitHub Actions builds Windows and macOS packages and publishes them as downloadable assets in the repository's **Releases** section. The website's Releases navigation points to that page. Manual workflow runs create downloadable workflow artifacts but do not publish a release.

## Privacy and safety
- No account or password collection, analytics, telemetry, ads, hidden downloads or automatic software installation.
- Disk information and folder previews are read-only.
- The app opens only allow-listed system settings and HTTP/HTTPS links.
- The file organizer previews files; it does not move or delete them.
- Unsigned builds may show standard OS security prompts. Code signing/notarization requires developer credentials.

## License
MIT.
