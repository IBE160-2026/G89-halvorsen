---
name: AI Study Buddy
status: draft
created: 2026-11-14
updated: 2026-11-19
concept: selected
description: Selected Notatkort-based concept with Atlas-inspired Quiz options; UX remains open.
colors:
  home-canvas: '#edeef2'
  summary-canvas: '#eef5ef'
  flashcards-canvas: '#fbf7e5'
  quiz-canvas: '#edf4fc'
  surface: '#ffffff'
  brand-ink: '#343a40'
  headline: '#171a19'
  brand-summary: '#4f9f6f'
  brand-flashcards: '#e0ae26'
  brand-quiz: '#4b9bc8'
typography:
  body:
    fontFamily: '"Avenir Next", Avenir, "Segoe UI", system-ui, sans-serif'
    fontSize: 16px
    lineHeight: '1.6'
  summary:
    fontSize: 17px
    lineHeight: '1.8'
rounded:
  md: 14px
  lg: 16px
  home-card: 34px
components:
  upload-cloud:
    color: '{colors.brand-flashcards}'
  pdf-arrow:
    color: '{colors.brand-ink}'
sources:
  - ../../prds/prd-G89-halvorsen-2026-11-03/prd.md
  - ../../prds/prd-G89-halvorsen-2026-11-03/addendum.md
  - decisions.md
  - imports/front-page-reference.png
---

# AI Study Buddy — Selected UX concept (draft)

## Brand & Style

On 19 November 2026, the user selected the latest **Home, Summary, Flashcards and Quiz** in [.working/study-preview.html](.working/study-preview.html) as the concept to continue. This includes Round 10's Home colours and the existing learning screens. The concept is selected; minor refinements remain possible, these contracts remain drafts and the UX phase is open. See the current decision in [decisions.md](decisions.md) and the [artifact guide](README.md).

Keep Notatkort's soft, minimal, professional character with rounded forms, readable typography and Atlas-inspired separate Quiz answer boxes. The [supplied visual reference](imports/front-page-reference.png) informs the illustrated Home composition. Earlier neutral and warm Home variants are historical alternatives, not competing defaults.

The v1 interface stays English. Generated study material uses the separate **Norwegian Bokmål** / **English** choice; [EXPERIENCE.md](EXPERIENCE.md) defines this distinction. PRD requirements govern behaviour. These peer UX documents record the selected concept; historical sketches and imports do not override them.

## Colors

| Surface or role | Selected concept |
|---|---|
| Home canvas | `{colors.home-canvas}` — light neutral grey |
| Summary canvas | `{colors.summary-canvas}` — very light sage green |
| Flashcards canvas | `{colors.flashcards-canvas}` — very light warm yellow |
| Quiz canvas | `{colors.quiz-canvas}` — very light blue |
| Content cards and answer boxes | `{colors.surface}` |
| Wordmark, Upload your PDF and decorative PDF arrow | `{colors.brand-ink}` |
| Upload cloud and middle logo layer | `{colors.brand-flashcards}` — exact shared golden yellow |
| Upper / lower logo layers | `{colors.brand-summary}` / `{colors.brand-quiz}` |

The logo's three original layers, strokes and existing responsive sizes stay fixed across all four screens. Home's active tab is neutral grey (`#e1e5e9`, border `#737e8b`), with a neutral `#526173` keyboard-focus ring. Learning tabs and enabled primary actions follow their green/yellow/blue function themes; secondary controls are white with coordinated borders, and disabled controls are neutral. The existing pastel illustration cards and corner forms remain unchanged.

## Typography

Use the current Avenir/system stack in `{typography.body.fontFamily}`. Keep **Make studying easier** near black, with the existing responsive 56/48/35px scale. Detailed Summary uses `{typography.summary.fontSize}`, `{typography.summary.lineHeight}` and a maximum 68ch measure, distinct headings and generous paragraph spacing. Current type and layout are the baseline, not a new redesign.

## Layout & Spacing

Prioritise laptop/PC with a responsive single web application. Keep one in-app top menu: Home, Summary, Flashcards, Quiz. Home has a centred introduction and raised white upload/settings card, a PDF illustration on the left and stacked learning cards on the right. Decorations stay clear of important text and controls and simplify or disappear on smaller screens; fields stack as needed. Preserve the existing spacing and responsive rules.

## Elevation & Depth

Keep restrained soft shadows on the Home upload card and illustrations. Learning content remains calm and readable. No added decorative animation; the existing 200ms function-canvas transition respects reduced motion.

## Shapes

Keep the existing rounded card, control and answer-box shapes. The selected prototype uses 16px learning cards, 14px separated Quiz answers and a 34px Home upload card. The logo form remains unchanged.

## Components

- **Home:** obvious dashed rounded PDF selector, clear upload icon, output-language and Summary-detail choices, Generate Summary, concise external-AI/material restrictions, unchecked acknowledgement and temporary-session copy.
- **Summary:** white reading card, Brief/Detailed selected at startup, readable headings/prose and a route to the existing Quiz.
- **Flashcards:** one white front/back card, actual count, Previous/Next, answer-side source link and repeat-same-set treatment.
- **Quiz:** four separate rounded white answer boxes, distinct selected state, Confirm answer, then feedback/source/result treatment.
- **View source:** the existing side panel illustrates filename, physical page and highlighted original excerpt. Full source/state coverage remains to be completed in UX.

## Do's and Don'ts

Preserve the selected visual baseline and use **concept** for preliminary sketches and variants. Keep BMAD's `DESIGN.md`, directory names and references intact. Avoid crowded screens, childish/gamified styling, unnecessary motion and unsupported privacy claims.

Remaining UX work: detail loading/error/coverage and New session/Clear states, complete source and learning-flow coverage, full keyboard/state checks and actual usability review. Then reconcile both draft contracts against the selected concept before any separate UX-completion decision. This update starts no next BMAD phase.
