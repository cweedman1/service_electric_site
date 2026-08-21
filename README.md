# Service Electric of Arlington  website foundation

Slice 1 is a dependency-free, five-page static site for Service Electric of Arlington, LLC. It is intentionally content-limited: the layout is inspectable now, while facts awaiting Ryan Witte's verification remain plainly unresolved.

## Run locally

Serve the project root with any static server. For example:

```powershell
python -m http.server 8000
```

Then open `http://localhost:8000/`. No install or frontend build is required.

## Source of truth

Verified identity and unresolved fields are recorded in `data/site.json`. Before changing business identity, licensing, contact details, service labels, or the origin, update that file first and then synchronize visible HTML, metadata, JSON-LD, sitemap, robots policy, and documentation. Run `python scripts/validate-site.py` afterward.

The placeholder origin uses the reserved `.invalid` top-level domain and is marked with `data-placeholder` in page metadata. `robots.txt` blocks crawling until launch. Never replace either safeguard with a plausible domain.

## Images

Original owner-supplied and candidate files remain under `assets/images/`. Production derivatives live under `assets/optimized/images/` and are referenced by the HTML from that separate directory.

Run `python scripts/process-images.py` from the project root to recreate derivatives (Pillow required at build time). The role map produces only widths needed by current layouts, never upscales, and retains aspect ratio. Add a future photograph by preserving its original in `assets/images/`, assigning it a real display role in the script, generating derivatives, and adding truthful alt text. Stock imagery must never be described as Service Electric's employees, work, customers, facilities, or equipment.

Current production roles are intentionally limited to the home lighting hero, a finished-lighting environment, a worker-on-ladder context, breaker work, diagnostic tools, and four distinct thermography views. The source filenames remain in `process-images.py`, preserving the link between every derivative and its candidate original.

The original logo at `assets/images/logo/service_electric_logo_original.jpg` is immutable. Processing only trims blank paper and resizes the exact pixels; do not trace, redraw, recolor, or approximate it as SVG.

See [architecture](docs/ARCHITECTURE.md) and the [launch checklist](docs/LAUNCH-CHECKLIST.md).

