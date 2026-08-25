# Architecture

## Pages

- `/`  identity, service categories, thermography entry point, and company-history invitation
- `/services.html`  Residential, Commercial, and Repairs only
- `/thermographic-imaging.html`  distinct technical service
- `/about.html`  family continuity, 1987 founding, DFW roots, and original-artwork history
- `/contact.html`  semantic slots for contact data; no form or invented details

The five-page architecture can later gain dedicated service or location pages only when business needs, verified service geography, and search evidence justify them.

## Frontend system

The site is plain semantic HTML with no runtime dependency. CSS is mobile-first and split by responsibility:

- `tokens.css`  color, typography, spacing, and shared measurements
- `base.css`  reset, typography, layout primitives, focus, reduced motion
- `components.css`  navigation, hero, cards, media, footer, contact slots
- `pages.css`  limited page-specific compositions

`navigation.js` is the only JavaScript. It manages mobile-menu state, Escape-to-close, link-close, and responsive reset. Without JavaScript, desktop navigation remains available; the mobile button is the only enhanced interaction.

## Visual system

Warm off-white and near-black establish an approachable, technically grounded base. Service Electric red sets identity and section rhythm; yellow is reserved for focus, highlights, and primary actions. Thermal blue appears only in the thermography context. Photography follows a work-to-result-to-technical-detail rhythm rather than repeating generic infrastructure.

The typography uses a system-only stack: Trebuchet MS/Aptos Display/Segoe UI for broader, warm display forms and Segoe UI/Helvetica/Arial for sustained reading. Fluid sizes are capped, headings have controlled measure, and the primary tablet breakpoint remains stacked until 56rem to avoid cramped headline columns.

The full original artwork appears prominently once, on About, as black-on-light artwork inside a warm paper panel. It is never blended, inverted, recolored, traced, or treated as a watermark. Navigation uses a text identity so the artwork is not repeated as decoration.

## Identity and content discipline

`data/site.json` is the editorial source of truth. It separates facts verified by Ryan or the business card, conservative provisional service descriptions, and unresolved launch data. This static slice deliberately avoids a templating dependency; synchronization is a documented editorial operation protected by the validation script. If the content surface grows, a small build-time templating step can consume this file without changing public URLs.

## SEO and structured data

Every page has a unique title, meta description, canonical, Open Graph data, X card data, one primary heading, and page-specific JSON-LD. Placeholder URLs use `service-electric.example.invalid`, which cannot resolve as a production property. Crawling is globally disallowed until launch.

The business entity uses Schema.org `Electrician`, a current valid subtype of `HomeAndConstructionBusiness` and `LocalBusiness`. The type was selected from the official Schema.org hierarchy rather than inventing `ElectricalContractor`. Markup contains the business name, office telephone, public email, Arlington/Texas home base, Dallas-Fort Worth service area, 1987 founding date, supplied license identifiers, and visible service descriptions. Page entities use `WebPage`, `AboutPage`, `ContactPage`, and `Service` where visible content supports them. Street address, postal code, hours, ratings, detailed service-area boundaries, and production URL remain absent.

## Content status

Verified public facts include both supplied phone numbers, the public email, license numbers, service labels, Ryan Witte as owner/contact, Arlington as the home base, the Dallas-Fort Worth service area, the 1987 founding year, family continuity, and the original-artwork history.

Provisional copy is limited to conservative descriptions of residential electrical needs, commercial electrical needs, repairs and troubleshooting, and the general role of infrared thermographic imaging. It does not enumerate detailed capabilities or make claims about availability, outcomes, credentials, equipment, or deliverables.

Unresolved items remain centralized in `data/site.json`: detailed business chronology, detailed service capabilities, exact thermography scope and qualifications, hours, address, precise service-territory boundaries beyond DFW, production domain, preferred contact workflow, and whether both phone numbers remain public long-term.

The sitemap is intentionally small. Future Search Console and Google Business Profile work belongs after the production origin and business facts are confirmed.

## Deployment assumptions

Deploy as immutable static files with the project root as the static document root. Configure HTTPS, compression, long-lived caching for fingerprint-stable media where the platform permits, and security headers at the host. The architecture uses external styles/scripts and no dynamic HTML, supporting a strict Content Security Policy; JSON-LD requires an appropriate hash or nonce if `script-src` excludes inline data blocks.

