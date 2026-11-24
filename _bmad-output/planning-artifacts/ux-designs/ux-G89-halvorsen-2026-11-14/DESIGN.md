---
name: AI Study Buddy
status: final
planning_status: complete
created: 2026-11-14
updated: 2026-11-24
finalized: 2026-11-24
concept: selected
description: Selected Notatkort-based concept with Atlas-inspired Quiz options; complete for UX planning, with implementation refinements permitted.
colors:
  home-canvas: '#edeef2'
  summary-canvas: '#eef5ef'
  flashcards-canvas: '#fbf7e5'
  quiz-canvas: '#edf4fc'
  surface: '#ffffff'
  ink: '#29372f'
  secondary-ink: '#56615b'
  brand-ink: '#343a40'
  headline: '#171a19'
  brand-summary: '#4f9f6f'
  brand-flashcards: '#e0ae26'
  brand-quiz: '#4b9bc8'
  correct-surface: '#edf5ef'
  incorrect-surface: '#fbefed'
  home-tab: '#e1e5e9'
  home-focus: '#526173'
  summary-action: '#dceadf'
  summary-action-ink: '#244b34'
  summary-focus: '#315d3f'
  flashcards-action: '#f2dfa0'
  flashcards-action-ink: '#514319'
  flashcards-focus: '#766023'
  quiz-action: '#d3e5f6'
  quiz-action-ink: '#284b6b'
  quiz-focus: '#315e88'
typography:
  body:
    fontFamily: '"Avenir Next", Avenir, "Segoe UI", system-ui, sans-serif'
    fontSize: 16px
    lineHeight: '1.6'
  summary:
    fontSize: 17px
    lineHeight: '1.8'
rounded:
  control: 10px
  md: 14px
  lg: 16px
  home-card: 34px
spacing:
  learning-gap: 22px
  summary-paragraph: 20px
  home-actions: 14px
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

# AI Study Buddy — Selected UX concept

## Brand & Style

**Complete for UX planning, 24 November 2026.** The user accepts the latest concept and authorises closure after the consolidated check finds no critical planning gaps. Home, Summary, Flashcards, Quiz, complete learning/source flows and the Round 21 reliability/mobile treatment are the selected implementation reference. Minor refinements remain possible during implementation; no production readiness or live AI quality is implied. See [the final report](validation-report.md).

Keep Notatkort's soft, minimal, professional character, readable type and rounded forms, with Atlas-inspired separate Quiz answers. The [supplied Home reference](imports/front-page-reference.png) informs the illustrated composition. Quizlet informed the study experience, without determining the app's visual identity. Earlier grey-blue, warm Home and navigation variants are historical alternatives; their decisions remain in [decisions.md](decisions.md).

The PRD governs behaviour. DESIGN.md and [EXPERIENCE.md](EXPERIENCE.md) are peer contracts and win over mocks/imports on UX conflicts. The [promoted concept overview](mockups/ux-overview.html) contains complete learning, reliability and processing references. [The selected shell](mockups/selected-shell.html) preserves the illustrated Home and basic one-question example; use [complete learning flow](mockups/complete-learning-flow.html) for the full Quiz, cards and sources. These are complementary references, not competing concepts. Their outside-app review selectors and sample counts are not product features or limits.

## Colors

| Role | Token |
| --- | --- |
| Home / Summary / Flashcards / Quiz canvas | `{colors.home-canvas}` / `{colors.summary-canvas}` / `{colors.flashcards-canvas}` / `{colors.quiz-canvas}` |
| Cards and answer boxes | `{colors.surface}` |
| Reading text / supporting text | `{colors.ink}` / `{colors.secondary-ink}` |
| Wordmark, Upload your PDF, decorative PDF arrow | `{colors.brand-ink}` |
| Heading Make studying easier | `{colors.headline}` |
| Logo upper / middle / lower layer | `{colors.brand-summary}` / `{colors.brand-flashcards}` / `{colors.brand-quiz}` |
| Upload cloud | `{colors.brand-flashcards}` exactly |
| Correct / incorrect answer surface | `{colors.correct-surface}` / `{colors.incorrect-surface}`, paired with explicit text |

Keep the original logo's shape, strokes and responsive sizes identical across tabs. Home's active tab is neutral `{colors.home-tab}` with `{colors.home-focus}` focus. Learning tabs and enabled primary actions follow their function's action/action-ink/focus tokens; secondary controls stay white with coordinated borders. Disabled controls stay neutral. A selected Quiz answer may be softly tinted; Confirm answer remains neutral until selection. Keep the existing illustration colours and corner forms.

Implementation targets: normal text at least 4.5:1, large text at least 3:1, and essential control/focus boundaries at least 3:1 against adjacent colours. Test actual rendered states, including hover, selected, error and zoom. Colour alone never conveys function, success or failure; decorative logo/cloud colours are not essential text or sole instructions. The prototype inspection does not certify a complete accessibility audit.

## Typography

Use `{typography.body.fontFamily}` and `{typography.body.fontSize}` / `{typography.body.lineHeight}`. Keep Make studying easier near black with the selected responsive 56/48/35px scale. Detailed Summary uses `{typography.summary.fontSize}` / `{typography.summary.lineHeight}`, maximum 68ch, clear headings and `{spacing.summary-paragraph}` paragraph spacing. Preserve current typography rather than introducing a new type direction.

## Layout & Spacing

Laptop/PC is primary; the same web app responds to mobile. Use one top Home / Summary / Flashcards / Quiz menu. Empty Home has a centred introduction and white upload/settings card; active Home replaces that form with read-only session information and actions. Keep the PDF illustration left and three pastel learning cards right, clear of the heading/form; simplify or hide decoration on narrow screens.

Use `{spacing.learning-gap}` between learning groups. At app widths up to 540px centre Flashcards/Quiz prompts, options, help, counts, feedback/results, notices and action groups, including empty/loading/error boxes. Summary reading prose/notices and original source excerpts stay left-aligned. Header/navigation/document information retain their selected wrapping treatment. Desktop placement stays as reviewed. All essential controls reflow without horizontal page scrolling at 320px.

## Elevation & Depth

Retain soft shadows on the Home card and illustrations. Keep learning surfaces calm. The existing 200ms canvas-colour transition respects reduced motion; no extra decorative animation is planned.

## Shapes

Use `{rounded.lg}` learning cards, `{rounded.md}` separated Quiz answers, `{rounded.control}` standard actions and `{rounded.home-card}` Home card. Preserve the selected logo geometry. Active Home's paired actions retain their approved 15px corners.

## Components

| Component | Selected visual treatment / reference |
| --- | --- |
| Navigation | Single wrapping top menu, rounded active tab, visible function-coloured focus. [Shell](mockups/selected-shell.html). |
| Empty Home | Dashed rounded upload zone, golden cloud, two labelled choice fields, concise sharing/temporary-session copy and unchecked acknowledgement. White card on grey. [Shell](mockups/selected-shell.html). |
| Active Home | Read-only filename/settings. Equal-column desktop actions, equal full-width mobile stack; 56px height, 16px/500 text, 15px corners and `{spacing.home-actions}` gap. Continue green, New session light neutral #f2f3f5. [Shell](mockups/selected-shell.html). |
| Summary | White reading card, comfortable measure and heading rhythm, source links and route to existing Quiz. [Complete flow](mockups/complete-learning-flow.html). |
| Flashcards | One white front/back card, actual counter, Previous/Next, answer-side source link; matching end/restart surface. [Complete flow](mockups/complete-learning-flow.html). |
| Quiz | Four separate rounded boxes, clear selection/Confirm, labelled correct/incorrect feedback, locked review, actual result and wrong-question list. [Complete flow](mockups/complete-learning-flow.html). |
| View source | White side panel with separate original passages, filename, physical page and highlighted excerpts; full-width responsive reader. [Complete flow](mockups/complete-learning-flow.html). |
| New session dialog | Existing white confirmation, clear loss boundary, Cancel and confirm, visible focus. Same pattern from Home and learning tabs. [Shell](mockups/selected-shell.html). |
| Processing / error card | Reuse the same rounded status geometry, concise heading/body/recovery. Mobile icon above centred text. [Processing states](mockups/processing-states.html) and [reliability](mockups/reliability-states.html). |
| Usable-content notice / demo information | Short explicit heading and explanation, distinct from blocking errors, actual remaining count where applicable. [Reliability](mockups/reliability-states.html). |

Four outcome presentations cover the 17 test scenarios: document error, generation error, usable-content notice and demo information; processing is the existing fifth pattern. Technical causes stay internal. Use a new reason/action as needed without adding a new visual system per cause. [The internal mapping](.working/reliability-scenarios.md) retains acceptance/publication distinctions.

## Do's and Don'ts

Preserve the selected identity and English UI terminology. Keep ordinary reading readable, action hierarchy clear, keyboard focus visible and student messages concise. Avoid crowded screens, childish/gamified styling, unnecessary motion, invalid partially published content and unsupported privacy/source-quality claims. Use “concept” for preliminary variants; keep BMAD filenames intact.

All IA surfaces have visual references in [the final coverage inventory](.working/ux-coverage-review.md). [Recorded checks](.working/review-v1-error-simplification/inspection.json) and [the final report](validation-report.md) distinguish prototype evidence from implementation/evaluation obligations. Fine spacing/copy refinements, real-device/zoom/assistive-technology testing and actual user observation remain follow-up work. No architecture work or commit/push is included in planning closure.
