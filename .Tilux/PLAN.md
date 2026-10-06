# Fresh & Reddy - Master Build Plan

## Pages
1. index.html - full-viewport hero carousel (5 slides), pagination dots, footer bar
2. about.html - origin story, stats, values, team
3. coffee-tasting.html - tasting experience, flavour notes, booking, FAQ
4. services.html - service tiers, process timeline, add-ons, pricing
5. equipment.html - machine lineup, specs, maintenance
6. culture.html - sustainability, sourcing, community, careers
7. contact.html - enquiry form, info cards, map, FAQ

## Activity Sequence
1. Save design blueprint and project answers.
2. Build shared design system CSS (tokens, nav, hero, cup composition, components, responsive).
3. Build main.js (nav behaviour, carousel, swipe, pull-to-refresh, reveals, counters, accordion, form validation).
4. Build index.html hero carousel with CSS-rendered 3D floating cups.
5. Build the six inner pages using shared components.
6. Serve on port 8081 and open in Edge.

## Shared Components
- Fixed navigation with stacked logo badge and active state
- Pill buttons (primary white, secondary ghost)
- Section header (tagline + title + sub)
- Card grid (2/3/4 columns)
- Stat row, process timeline, pricing tiers, FAQ accordion, CTA band
- Form fields with inline validation states
- Full site footer and home footer bar

## Interaction Map
- Nav: shrink/hide on scroll, mobile drawer, active link highlight
- Hero: dot navigation, arrow controls, autoplay, touch swipe
- Dots: click to jump to slide
- FAQ: click to expand, icon rotates
- Forms: validate on submit, inline errors, success state, local lead capture
- Counters: animate when scrolled into view
- Reveals: IntersectionObserver with immediate in-view pass and failsafe timer

## Wiring Guarantee
Every nav link, button, form, dot and accordion is wired to real behaviour. No dead ends, no placeholder links.
