# AI Study Buddy — derived support context

<!-- impeccable:product-schema 1 -->

**Current planning status — 24 November 2026:** UX planning is complete under the final DESIGN.md/EXPERIENCE.md and Round 22 decision. Earlier draft/open round notes below are historical. The latest shell, complete learning/source/reliability and mobile references are selected; no architecture or production implementation has started.

This is a derived support extract for visual exploration inside the existing BMAD UX run. It records confirmed source facts and the user's current brief; it is not a new discovery or product specification. The current four-screen concept is selected as recorded below; UX remains in progress.
The authoritative [PRD](../../../../prds/prd-G89-halvorsen-2026-11-03/prd.md) and [addendum](../../../../prds/prd-G89-halvorsen-2026-11-03/addendum.md) govern product behaviour. The existing [DESIGN.md](../../DESIGN.md) and [EXPERIENCE.md](../../EXPERIENCE.md) remain the peer UX contracts; both are currently drafts. See [the detailed UX constraint extract](../prd-ux-constraints.md).

## Platform

web

## Stack

Open Architecture decision. This support document selects no framework, UI library, model, PDF parser or deployment target. Rendered concepts are reviewable mockups, not the production stack.

## Users

Students preparing and practising course material from a text-based academic PDF. The solo developer initially evaluates the product with her own material; cross-discipline usefulness has not been established.

## Product Purpose

Reduce study-material preparation and support understanding/practice through a structured summary, flashcards and a multiple-choice quiz, with inspectable original supporting passages. Source-supported quality takes priority over item count. No achieved time saving or learning gain is claimed.

## Operating Context

Laptop/PC first, with the same web application responsive and usable on mobile; no separate mobile app. One temporary session holds one PDF, one Bokmål/English output language and one Brief/Detailed summary level, all chosen before generation. Navigation preserves generated content and progress; changing PDF/language/level requires a confirmed new session and fresh startup. Reload/closing ends the session.

## Capabilities and Constraints

- Summary: structured headings/concepts/explanations; one selected level per session; navigation to the existing Quiz.
- Flashcards: one front/back card at a time, sources on the back, actual counts, previous/next and repeat the same set without generation. Function return preserves position and hides the answer.
- Quiz: four alternatives, explicit answer confirmation before feedback, locked confirmed answers, short wrong-answer explanation/source access, actual-count result and review/restart of the same questions.
- View source: sidepanel with filename, physical page and highlighted original-language excerpt. Closing preserves position/progress, including a revealed card answer. Location match is not factual verification.
- Visible external-processing explanation and active acknowledgement per accepted upload precede any external transfer. No unsupported privacy/provider claims.
- Honest operation/loading/error states; manual Try again; valid reduced sets with notice; no automatic regeneration/repair/refill. Preserve valid active-session content on failure and reject ended-session results.
- A clearly labelled saved-content demo runs without private keys/paid accounts; own PDFs/fresh generation require live mode. A separately shareable demo PDF remains to be selected.
- Exclude accounts/login, permanent history, multiple documents/variants, non-PDF input, OCR/PDF repair, advanced figure/table interpretation, learning plans, written-answer assessment, advanced statistics, gamified scoring, adaptive learning, spaced repetition and mastery ratings.
- Technical bounds, provider/parser/model choices, cleanup timing and extraction/matching algorithms remain open. Do not invent upload limits or imply completed app/AI-quality tests.

## Brand Commitments

The product name is AI Study Buddy. The user wants a modern, minimalist, intuitive, orderly, airy and professional interface: clear learning-function navigation, strong readable typography, comfortable colors, whitespace, clear cards and simple consistent interactions. Quizlet is inspiration only, not a template to copy. Avoid gamification, crowded screens, too many buttons and unnecessary animation.
The first round presented five different concepts. The user's [preliminary preferences](../../decisions.md) guide a refinement: Notatkort's layout, comfortable typography, rounded forms and simple navigation, combined specifically with Atlas's clearly separated quiz answer boxes, softened with rounded corners and generous spacing. The latest Round 2 requests a full content canvas that changes by learning function: very light sage Summary, warm very light pastel-yellow Flashcards and soft very light pastel-blue Quiz. Keep cards and answer boxes white or nearly white, identify the active tab clearly and use a subtle background transition with reduced-motion support. Compare the three function screens. This supersedes the earlier neutral-canvas exploration; the visual system otherwise stays consistent. Exact shades and final direction remain open, and the PRD's functional scope is unchanged.

Round 3 refines the active Flashcards tab to light warm yellow instead of dark brown. Primary, secondary, hover, border and keyboard-focus treatments follow the active function; disabled controls stay neutral. Detailed summaries need a comfortable reading measure and paragraph/heading rhythm. Add a simple PRD-conforming startup preview with one-PDF selection, output language, summary level and visible external-processing information with active acknowledgement. Show startup and all three learning functions in a browser. These are reviewable visual proposals, not final design approval. Any simulated generation uses clearly labelled illustrative content and makes no external calls.

Round 4 fixes the entire v1 interface in English, with no UI-language selector. Output language remains a separate Norwegian Bokmål/English choice for generated study material. Use Summary, Flashcards, Quiz, Norwegian Bokmål, English, Brief and Detailed consistently, while preserving original-language excerpts and filenames. Refine startup to a light neutral grey canvas with a prominent dashed rounded PDF-selection area and supplied upload icon, more balanced form weight, and shorter essential help. Pastels begin in learning functions. The preview headline is provisionally “Turn your PDF into study tools”; headline alternatives and final visual direction still await user review.

Following headline feedback, use **Make studying easier** in the current preview, supported by a concise explanation of the PDF-to-Summary/Flashcards/Quiz workflow. This updates the earlier provisional headline; the overall visual design still awaits review.

## Evidence on Hand

The final PRD/addendum define the v1 contract. The UX run and draft contracts already exist and must continue in place. Local T1–T3 evaluation PDFs are not public demo assets; a limited PDF extraction inspection does not prove complete coverage or generated-content quality. Concept content and simulated interactions are illustrative, not implementation or validation evidence.

## Accessibility & Inclusion

The addendum requires UX follow-up on keyboard use, readability and understandable source-location/support wording. Responsive mobile use is confirmed. No additional certification or completed accessibility audit is claimed here.
## Front-page reference refinement — Round 5

Continue the existing draft preview using [the user's visual reference](../../imports/front-page-reference.png). Match the large centred heading, elevated white form, grey canvas, pastel learning-card/PDF illustrations, soft corner shapes and desktop composition. Green startup accents and pastel decorations are allowed by this latest reference; the full learning canvases remain function themed. Keep fixed English UI and existing PRD behaviour, accurate click-to-choose copy, Generate Summary, material-sharing restrictions, active acknowledgement and temporary-session information. Do not copy the reference's unsupported storage guarantee. This is visual exploration, not final design approval.

## Shared navigation and startup refinement — Round 6

The user prefers the illustrated direction but requests a somewhat smaller near-black headline, one shared clickable Home/Summary/Flashcards/Quiz menu at the top inside the app on every screen, no external screen picker, clearer upload icon and a shorter upload area. Keep decorative PDF and pastel learning cards clear of the heading and important form content; simplify or hide them on smaller screens. The menu browses prewritten example screens, preserves practice state and makes no PDF/AI calls. Home is a prototype screen choice, not Clear/New session. Existing PRD rules for real active sessions, generation and acknowledged external processing remain authoritative. See Round 6 in decisions.md and the draft EXPERIENCE.md navigation boundary; no final design approval or production implementation is implied.

## Neutral Home and brand colours — Round 7

The active Home tab is provisionally neutral grey, while learning functions retain their existing green/yellow/blue themes. Upload and decorative PDF-arrow accents use #788CA7. The unchanged logo layers use existing theme-border colours, upper Summary green #6c8a76, middle Flashcards yellow #8e783e and lower Quiz blue #62809c, fixed across screens. Brand text and Upload your PDF share dark grey #343a40. Only these colour roles change; geometry, content, behaviour and remaining controls stay unchanged. The user will review these colours before final approval.

## Current concept selection — 19 November 2026

This section supersedes the historical round notes above. The user has selected the latest Home, Summary, Flashcards and Quiz in the existing study-preview.html as the concept for continued UX work. Home stays light grey with the illustrated PDF/learning cards and corner forms; the unchanged shared logo uses green #4f9f6f, yellow #e0ae26 and blue #4b9bc8. The upload cloud directly shares #e0ae26, while the PDF arrow and wordmark use #343a40. Learning canvases stay Summary #eef5ef, Flashcards #fbf7e5 and Quiz #edf4fc. Keep the single in-app menu, typography, layout, separate rounded Quiz answers and current behaviour. Earlier neutral/warm variants are historical alternatives.

Minor refinements remain possible. DESIGN.md/EXPERIENCE.md remain drafts, with loading/error/coverage, New session, complete learning/source and keyboard/state/usability work still open. Use concept terminology for preliminary sketches; preserve BMAD paths and product requirements. No production implementation, next phase or UX completion is implied.

## Session-action simplification — Round 13

The user removes the duplicate Clear action and keeps only New session. Confirmation still explains/removes active session working data and progress, preserves the original device file and gives empty Home. The student may stop there; a new upload/settings/acknowledgement is needed only to study again. Cancel preserves the active session and old content cannot reappear after confirmation. PRD FR-16 is retired without renumbering; FR-15/shared rules retain its protections. Current concepts compare a Session disclosure with one visible New session button; placement is not selected. Earlier Clear references above are historical and superseded. UX stays open.

## Selected placement — Round 14

The user selects Visible button. The main study-preview.html now places one New session button directly beside document context on learning screens, wrapping below the document name on mobile. Keep the illustrated empty Home, shared navigation/logo/theme/type and confirmed reset semantics. The earlier Session-menu comparison is historical and not selected. No separate Clear action, extra Home placement or final UX completion is adopted. See current DESIGN/EXPERIENCE for remaining coverage and preview versus production boundaries.
