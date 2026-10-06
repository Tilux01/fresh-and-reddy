# Fresh & Reddy - Design Blueprint

## 1. Design Philosophy
Premium, modern, artisanal corporate, bold. Conveys an uncompromising high-end office beverage service with a rebellious edge ("make bad office coffee a thing of the past").

- Visual density: spacious and deliberate. Generous horizontal padding, breathing room around components so central 3D product imagery carries maximum visual weight.
- Theme balance: pure dark-mode experience (#1a1a1a to #242424 tonal range), dark-textured product mockups (black/red paper cups) contrasted with ultra-crisp white typography.

## 2. Color Tokens
| Token | Name | Hex | RGBA | Usage |
|---|---|---|---|---|
| Base | Background Main | #1e1e1e | rgba(30,30,30,1) | Page backdrop |
| Base | Surface Primary | #262626 | rgba(38,38,38,1) | Card containers, navigation background |
| Base | Surface Hover | #323232 | rgba(50,50,50,1) | Interactive card/button hover |
| Accent | Brand Red | #e53935 | rgba(229,57,53,1) | Active dots, accents, cup typography |
| Text | Text Primary | #ffffff | rgba(255,255,255,1) | Headings, primary links |
| Text | Text Muted | #9e9e9e | rgba(158,158,158,1) | Body description, footer subtext |
| Text | Text Subdued | #757575 | rgba(117,117,117,1) | Disabled links, inactive metadata |
| Border | Border Subtle | - | rgba(255,255,255,0.15) | Outlined borders, dividers |

## 3. Typography
- Headings & Display: Geometric sans-serif, Montserrat Black (900) stack.
- Body & UI: Clean modern grotesk, Inter stack.

| Level | Size | Weight | Line Height | Tracking |
|---|---|---|---|---|
| Display Hero | 56px / 3.5rem | 900 | 1.05 | -0.03em |
| Section Title / Tagline | 14px / 0.875rem | 600 | 1.2 | +0.05em |
| Body Copy | 12px / 0.75rem | 400 | 1.5 | normal |
| Navigation Links | 11px / 0.6875rem | 500 | 1.0 | +0.08em |
| Footer / Meta | 10px / 0.625rem | 400 | 1.0 | +0.1em |

## 4. Layout Architecture
- Container max-width 1280px centered, fluid horizontal padding 64px desktop minimum.
- 8px spacing grid: 4px micro, 8px tight, 16px component, 24px gap, 48px section block.
- Section sequence (home): Top Bar Navigation -> Hero Main Body -> Pagination Dots -> Footer Bar.
- Z-index: base content 1, 3D floating elements 10, fixed nav 100, modals 1000.

## 5. Component Blueprint
### A. Navigation Bar
Fixed top, full width. Interior padding 32px horizontal / 24px vertical. Left: stacked logo badge (FRESH / & REDDY). Right: HOME, ABOUT, COFFEE TASTING, SERVICES, EQUIPMENT, CULTURE, CONTACT US. Item gap 32px. Uppercase, tracking +0.08em.

### B. Hero Buttons
- Primary "BOOK A FREE TRIAL": pill radius 9999px, solid #ffffff background, charcoal #1a1a1a text, weight 600, padding 12px 28px.
- Secondary "OUR SERVICES": pill, transparent background, border 1px rgba(255,255,255,0.4), white text, weight 600, padding 12px 28px. Hover: border solid #ffffff, background rgba(255,255,255,0.05).

### C. Carousel Dot Indicators
Vertical stack, far right edge of canvas. 5 dots. Inactive: 6px white circle at 0.4 opacity. Active: expanded / Brand Red #e53935. Gap 12px.

### D. Footer Bar
Left taxonomy: COFFEE - TEA - WATER - SNACKS - DELIVERED (middle dots, tracking +0.1em). Center: mouse scroll indicator (pill outline with internal wheel dot). Right: social icons plus directional arrows in circular ghost buttons (border 1px rgba(255,255,255,0.2)).

## 6. Motion Mechanics
- Page load: staggered fade-in and slide-up for hero typography, 0.8s, cubic-bezier(0.16, 1, 0.3, 1).
- 3D floating cups: continuous sinusoidal bobbing on the Z-axis with slight rotational sway.
- Hover transitions: all 0.25s ease-in-out.
- Mobile gestures: swipe left/right for carousel switching, pull-down refresh micro-interaction.
