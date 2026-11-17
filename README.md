# NEXUS Engineering Suite

An offline-first, local-first workbench for software developers, electronics and hardware engineers, network technicians, and technical learners.

## Website
After enabling GitHub Pages from **Settings → Pages → Deploy from branch → main → /(root)**, the site is available at:
https://zaboylah-cell.github.io/Nexus-Engineering-Suite/

## Included browser tools
- Ohm's law and power calculator
- 4-band resistor decoder
- IPv4/CIDR subnet calculator
- JSON formatter and validator
- UTF-8 Base64 encoder/decoder
- Regular-expression tester
- Decimal/binary/hex converter
- Engineering unit conversions
- Unix timestamp converter
- Local engineering notes

## Desktop app
The Python/Tkinter edition works offline and includes Ohm's law, subnet, JSON, Base64, and regex tools. Download the matching build from the repository's **Actions → Build desktop downloads** workflow artifacts. Run the workflow manually or push a version tag (for example `v1.0.0`). Builds are OS-specific: Windows, Linux, and macOS each need their own download.

## Privacy and safety
- No account, password form, payment form, analytics, ads, external JavaScript, or third-party tracking.
- Browser tools perform calculations locally; notes are stored in browser local storage.
- Desktop edition runs locally and does not make network requests.
- No automatic software download or silent installation.
- Never use calculator output as the sole basis for safety-critical engineering decisions. Verify with authoritative component datasheets, standards, and qualified review.

## Run desktop from source
Python 3.9+ with Tkinter:
```bash
python desktop/nexus.py
```

## License
MIT.
