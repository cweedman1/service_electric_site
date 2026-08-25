# Launch checklist

## Owner verification required

- [ ] Production domain and canonical URL format
- [ ] Publishable business address or explicit decision to omit it
- [ ] Business hours
- [ ] Any preferred public wording beyond the verified Dallas-Fort Worth service area
- [ ] Detailed residential, commercial, and repair capabilities
- [ ] Thermographic imaging scope, equipment, qualifications, process, and deliverables
- [ ] Detailed family/business chronology beyond the verified 1987 founding year
- [ ] Preferred contact/request workflow and responsible recipient
- [ ] License labels and numbers rechecked against owner records
- [ ] Approval of logo usage, photography selection, and provisional customer copy

## Content and local SEO

- [ ] Replace every `service-electric.example.invalid` occurrence with the verified HTTPS origin
- [ ] Change `robots.txt` from global disallow to launch policy and enable its sitemap line
- [ ] Confirm sitemap URLs match canonical redirects and preferred trailing-slash policy
- [ ] Synchronize verified identity through visible copy, `data/site.json`, metadata, JSON-LD, sitemap, and footer
- [ ] Connect and verify Google Search Console after deployment
- [ ] Align site identity with the verified Google Business Profile
- [ ] Add only real reviews, affiliations, brands, service areas, and project claims
- [ ] Review stock-photo licenses/attribution records; never present stock as company work
- [ ] Create a dedicated, approved 1200630 social card if the launch channel needs a large preview

## Technical release

- [ ] Run `python scripts/process-images.py` if source imagery changed
- [ ] Run `python scripts/validate-site.py`
- [ ] Validate JSON-LD with current Schema.org/Google tooling
- [ ] Test keyboard navigation, menu Escape behavior, focus visibility, zoom, and reduced motion
- [ ] Test current mobile, tablet, and desktop viewport ranges
- [ ] Check all internal links and HTTP status codes on the deployed origin
- [ ] Run Lighthouse accessibility, performance, best-practices, and SEO audits
- [ ] Confirm WebP delivery, compression, caching, and no image upscaling
- [ ] Configure CSP, `X-Content-Type-Options`, `Referrer-Policy`, and framing policy at the host
- [ ] Confirm 404 behavior and redirect rules
- [x] Remove visible development-only language from customer pages
- [ ] Confirm analytics/cookie policy only if analytics is actually added

