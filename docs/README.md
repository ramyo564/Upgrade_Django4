# Upgrade_Django4 Dashboard Template

This folder contains a reusable dashboard package adapted from the shared `portfolio_template` structure.

## Files
- `index.html`: layout skeleton
- `style.css`: UI and responsive styles
- `script.js`: renderer for sections/cards/navigation/mermaid modal
- `config.js`: Upgrade_Django4 content configuration
- `diagrams.js`: mermaid graph source strings
- `learnmore-links.js`: card -> README anchor mapping

## Structure rules
- Every card key (`mermaidId`) must exist in three places:
1. `config.js` service card definition
2. `diagrams.js` object key
3. `learnmore-links.js` object key

- Top panel diagram keys follow the same rule:
1. `config.js` `topPanels[*].diagramId`
2. `diagrams.js` object key

## Learn More rules
- Hybrid mode is used:
1. `EVIDENCE` link opens internal evidence page (`docs/evidence/upgrade_django4/index.html#<card-id>`).
2. `README` link opens original `Upgrade_Django4/README.md` anchor (`#lm-*`).
- `learnmore-links.js` keeps README anchor mapping and is reused to generate README links in cards.

## Validation checklist
- All cards render mermaid diagrams
- All Learn More links open expected README sections
- Mobile menu, responsive grid, and modal zoom work correctly
