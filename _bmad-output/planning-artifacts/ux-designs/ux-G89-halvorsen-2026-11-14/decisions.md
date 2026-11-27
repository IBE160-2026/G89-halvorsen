# AI Study Buddy — UX concept decisions

**Current status — Round 22, 24 November 2026:** UX planning complete; the latest concept and complete learning/source/reliability/mobile references are selected. Minor implementation refinements remain possible. Earlier open/draft statements record their historical round. See [the completion decision](#planning-completion--round-22-selected-concept-and-consolidated-check) and [final report](validation-report.md).

## Current selection — 24 November 2026

**Selected concept — UX planning complete.** The user has selected the latest **Home, Summary, Flashcards and Quiz** together as the concept for continued UX work. Use [.working/study-preview.html](.working/study-preview.html) and [the current browser export](.working/browser-preview/index.html). The selected Home includes Round 10: light-grey canvas, unchanged green/yellow/blue logo, golden-yellow upload cloud `#e0ae26` and dark-grey PDF arrow `#343a40`. The learning views retain their existing function-themed pastels, Notatkort foundation and separate rounded Atlas-inspired Quiz answers.

Minor implementation refinements remain possible. Round 22 selects the complete learning/source/reliability and mobile references following user acceptance and the consolidated check. DESIGN.md and EXPERIENCE.md have `status: final` and `planning_status: complete`. Actual user observation, full accessibility and production validation remain implementation/evaluation follow-up. Do not start the architecture phase.

**Session-action decision — Round 13:** Keep only **New session**. The separate Clear action is removed because both had the same outcome and confused the user. Confirmation still protects the active session; ending at empty Home does not require a new upload. **Round 14 selects Visible button:** one directly visible New session button beside the document context on learning screens. The Session-menu option is not selected. This supersedes earlier Clear requirements and sketches; see the latest decision below.

Use **concept** for preliminary sketches and variants. BMAD filenames/structure remain unchanged. Earlier rounds below preserve what was preferred, pending or superseded at that time; their historical status is not the current selection. See [the artifact guide](README.md) for current versus historical files.

**Active Home selected — Round 18, 20 November 2026:** The user approves the active Home card and both flows. The [main source](.working/study-preview.html) and [browser index](.working/browser-preview/index.html) retain empty Home before a session and show filename, read-only output language/Summary detail, and the approved equal-sized Round 17 actions during an active session. Continue studying returns to the last visited learning tab with content and progress preserved; returning to Flashcards shows the front of the retained card. The existing New session dialog preserves everything on Cancel/Escape; confirmation clears the working session to empty Home, leaves the original local file unaffected and does not require starting again. The preserved [Round 18 active Home review](.working/study-preview-active-home-r18.html) and [browser entry](.working/browser-preview/active-home-r18.html) show the labelled active example before status integration. The Round 15 diagnostic entry remains frozen history; earlier separate active Home concepts remain preserved.


**Status patterns selected — Round 20, 24 November 2026:** The user explicitly approves all three Round 19 processing, PDF-problem and AI-failure presentations on desktop/mobile. Adopt these patterns in the main concept and use the [fresh status review](.working/study-preview-status-r20.html) / [browser entry](.working/browser-preview/statuses-r20.html). Processing names the operation without invented progress or automatic completion; the password-required PDF presentation recovers through confirmed New session; the Flashcards AI failure preserves valid Summary and offers manual Try again. Label any scenario controls outside the app as preview-only. The prior main is frozen as [.working/study-preview-round-19.html](.working/study-preview-round-19.html). The separate Round 19 comparison and older entries retain their historical review state.

**Complete references selected — Round 22:** Use the existing PRD together with the [fresh combined review](.working/remaining-ux-review-r21.html), stable [browser entry](.working/browser-preview/remaining-ux.html), separate [reliability](.working/reliability-review.html) and [learning/source](.working/learning-flows-review.html) concepts, and the [coverage matrix](.working/ux-coverage-review.md). Reuse four outcome presentations plus pending for all 17 internal cases; use plain-English feedback, preserve valid content/progress on failed Cards/Quiz attempts and share the requested mobile alignment. The complete reliability/learning presentations are now selected for UX planning under Round 22. Shared status copy/alignment also refine the selected main. Preserve the chosen visual direction, English interface, fixed Bokmål/English study material and Brief/Detailed Summary choices. All content remains illustrative, with no PDF reading or API calls.

---

## Concept Preferences – Round 1

### 1. Preferred Concept: Notatkort

My preferred concept is **Notatkort**.

I particularly like:

- The soft, minimalist and modern appearance.
- The rounded corners on cards, buttons and other elements.
- The comfortable, readable typography.
- The spacious layout with plenty of breathing room.
- The calm and welcoming atmosphere, which feels suitable for studying.
- The simple and intuitive navigation between Summary, Flashcards and Quiz.

I want AI Study Buddy to feel professional and visually appealing without being overly complicated or distracting.

### 2. Elements to Borrow from Atlas

Although Notatkort is my preferred concept, I like how **Atlas displays the answer options in the Quiz section**.

Each answer option has its own clearly separated box, with more spacing between the alternatives. This makes the quiz easier to read and navigate.

I would like to combine this layout with Notatkort's softer visual style:

- Separate answer boxes with generous spacing.
- **Rounded corners** instead of rectangular boxes.
- Subtle borders and clear selection states.
- Comfortable padding and readable text.
- Styling that feels consistent with the rest of the application.

### 3. Colour Palette – Explore Further

I like the soft sage-green palette used in Notatkort, but I am not completely decided on the final colours.

I would like to explore giving each learning function its own subtle pastel colour:

- **Summary:** Soft sage green.
- **Flashcards:** Light pastel yellow.
- **Quiz:** Light pastel blue.

The colours should complement each other and create a cohesive, calm and harmonious design.

I do not necessarily want the entire background to change colour between functions. Instead, the colours could be incorporated into active navigation tabs, cards, buttons, subtle backgrounds and other relevant interface elements.

The overall interface should maintain a consistent typography, spacing, rounded corners and visual identity.

I would like to see different colour variations before making a final decision.

### 4. Overall Concept Direction

My preferred direction is to use **Notatkort as the main concept foundation**, combined with selected elements from Atlas.

The concept should prioritise:

- Simplicity and intuitive navigation.
- Soft colours and rounded elements.
- Clear visual hierarchy and readability.
- Generous spacing without unnecessary empty space.
- A consistent and pleasant studying experience.
- A desktop-first layout that also adapts to smaller screens.

I want to avoid cluttered interfaces, excessive animations, harsh contrasts and overly playful or childish concept elements.

### 5. Next Steps

These are **preliminary concept preferences, not final decisions**.

I would like to explore a refined concept that combines:

1. Notatkort's overall layout, typography and rounded appearance.
2. Atlas's clearly separated quiz answer options, adapted with rounded corners.
3. A cohesive pastel colour system that distinguishes Summary, Flashcards and Quiz.

I want to review the combined concept visually before making final decisions about the concept direction.

## Concept Preferences – Round 2: Function-coloured Backgrounds

For the next visual comparison, the **full content-area background** should change with the active learning function:

- **Summary:** Soft, very light sage green.
- **Flashcards:** Warm, very light pastel yellow.
- **Quiz:** Soft, very light pastel blue.

The colours should remain calm, harmonious and unobtrusive. Keep content cards and the separate Atlas-inspired quiz answer boxes **white or nearly white**, with rounded corners, generous spacing and readable contrast.

The active navigation tab must clearly identify the current learning function. Use a soft, subtle background-colour transition when switching functions, respecting reduced-motion preferences.

Show the three function screens together for comparison, while retaining Notatkort's layout, typography and soft visual identity, with desktop-first and responsive behaviour.

For this round, this replaces the neutral content-canvas treatment explored previously. The other Round 1 preferences continue to guide the concept.

These are still **preliminary UX preferences for visual exploration**, not a final palette or overall concept approval. This changes the proposed visual presentation only; functional requirements and product scope continue to follow the existing PRD.

## Concept Preferences – Round 3: Controls, Reading and Startup

These preferences refine the current Notatkort-based concept and preserve the earlier rounds for reference. The overall concept and exact colours remain **preliminary**, pending visual review.

### Function-themed Navigation and Buttons

- Replace the dark brown active Flashcards tab with a **lighter, warm muted yellow** that harmonises with its pastel-yellow canvas. Keep the active function clearly identifiable through more than colour alone.
- Retain a visible keyboard focus indicator, with its colour adapted to the current function and sufficient contrast.
- Buttons follow the active function: **soft greens for Summary**, **warm muted yellows for Flashcards** and **soft blues for Quiz**. Avoid applying pale green controls across every function.
- Enabled primary actions, such as **Confirm answer**, need clear colour and readable contrast after a choice is made. Before a choice, the disabled action may be white.
- Secondary actions, such as **Previous** and **Next**, may remain white with subtle function-coordinated borders.
- Disabled controls use a neutral, subdued treatment. Keep rounded corners, readable labels and consistent construction across the application.

### Longer Summaries

- Give **Detailed** summaries a comfortable reading measure, a clear heading hierarchy and generous paragraph spacing.
- Preserve the established typography and calm layout; avoid unnecessarily wide lines or dense blocks of long text.

### Startup Screen Before Upload

Explore a simple, first-time-user startup screen in the same visual style, containing:

- A clear, intuitive way to select one PDF.
- Output-language choices: **Norwegian Bokmål** or **English**.
- Summary-level choices: **Brief** or **Detailed**.
- A clear action to begin generation.
- Short, visible information about external AI processing and the required active acknowledgement.

The startup flow must follow the revised PRD, including its session and processing boundaries. It must not imply that all learning functions generate automatically.

### Preview and Scope

Make the startup screen, Summary, Flashcards and Quiz available for review in a browser. Retain the soft Notatkort foundation, function-coloured pastel canvases, white content cards and separate rounded Atlas-inspired quiz options.

This is continued **UX exploration**, not final concept approval or a change to the PRD's functional requirements. Review the updated screens before further concept decisions.

## Concept Preferences – Round 4: Clear Startup and English Interface

### Interface Language and Study Material Language

- The **entire v1 interface is in English**: startup, navigation, buttons, help, status, errors, confirmations and accessibility labels. There is no interface-language switch in v1.
- Use the canonical labels **Summary**, **Flashcards**, **Quiz**, **Norwegian Bokmål**, **English**, **Brief** and **Detailed**. The output-language option must read **Norwegian Bokmål**, not only Bokmål.
- The language selector controls **AI-generated study material**, not the interface. Students still choose Norwegian Bokmål or English before generation for Summary, Flashcards and Quiz, under the existing PRD session rules.
- Selected Norwegian study material, original source excerpts and filenames keep their appropriate original language. Fixed interface labels, such as result status and source controls, remain English.

### Startup Layout and Upload Area

- Keep the startup canvas **light neutral grey**. Introduce the green, yellow and blue pastel families when entering the learning functions.
- Give the startup card more visual weight and balance its content against surrounding whitespace, while preserving the soft, rounded, readable Notatkort foundation.
- Make PDF selection immediately recognisable with a prominent upload symbol, a dashed rounded outline and a clear English file-selection action. This refines the existing upload interaction without adding product functionality.
- Shorten and simplify help text, particularly below the generation action. Retain visible external-AI processing information, material-sharing restrictions, an active acknowledgement and the temporary-session message. Do not add unsupported privacy guarantees.

### Headline Exploration

Consider these short English alternatives before selecting a final headline:

1. **Turn your PDF into study tools**
2. **Create a Summary, Flashcards and Quiz**
3. **Your PDF. Your study toolkit.**

The first option is a provisional preview headline while the alternatives are reviewed; no final headline has been chosen.

**Update after feedback:** The user's preferred headline is **Make studying easier**. Use it in the revised preview, with a short supporting line that explains the PDF-to-Summary/Flashcards/Quiz workflow. The overall visual concept remains under review.

### Scope and Review

Preserve the existing learning-function canvases, themed controls, comfortable reading measure and separate rounded quiz answers. These refinements add no functions and do not change PRD behaviour. The English-interface choice applies to v1; the visual layout, headline and final concept still await review.

## Concept Preferences – Round 5: Front-page Visual Reference

Use the user-supplied [front-page reference](imports/front-page-reference.png) to bring the existing startup preview as close as practical to its composition, illustrations, typography and visual depth. This continues the same UX exploration; it does not approve a final concept or restart the process.

### Visual Treatment to Explore

- Keep the light grey page canvas, dark green typography, soft pastel palette and rounded elements.
- Use a broad top bar with the product mark/name and a softly highlighted Home indicator, with the three learning-function names arranged horizontally on desktop.
- Centre **Make studying easier** at a larger, more prominent scale, with a short explanatory subtitle beneath it.
- Give the central white upload/settings card generous rounding, clear spacing and a soft, offset shadow.
- Echo the reference's PDF illustration on the left and its stacked green Summary, yellow Flashcards and blue Quiz illustrations on the right. Use quiet pastel corner shapes and restrained depth, without decorative animation.
- At smaller widths, simplify the decoration and stack the form fields so the upload action, choices and acknowledgement stay readable and usable.

For this preview, the reference's pastel illustrations and green startup accents refine Round 4's colour restriction: the startup **canvas remains light grey**, while these local accents may introduce the function colours. The full learning-function backgrounds and their themed controls remain as previously explored.

### PRD Boundaries Remain Authoritative

The reference is visual guidance rather than a source of new product behaviour or privacy promises. Preserve the separate study-material language and Summary-level choices, English interface, active unchecked acknowledgement and temporary-session information. Keep the material-sharing restrictions and the explanation that extracted PDF text is sent to an external AI service; do not repeat the reference's unsupported storage guarantee.

The startup action remains **Generate Summary**, without implying automatic generation of all three functions. Describe the existing click-to-choose PDF interaction accurately. Home is a startup location indicator, and the illustrated learning cards are decorative. No new functions, processing capabilities or changes to PRD requirements are introduced.

Review the revised preview visually before further concept decisions. All earlier rounds remain recorded above.

## Session Checkpoint — 14 November 2026

UX work is paused for today at the user's request. **The latest illustrated Round 5 preview is the starting point for the next session.** This confirms the working baseline only: the concept is **not finally approved**, and the UX phase remains open. DESIGN.md and EXPERIENCE.md retain `status: draft`.

Continue the Notatkort foundation with the selected Atlas-inspired rounded, separate Quiz answers. The current startup has a light grey canvas, the **Make studying easier** heading, a raised white upload card and illustrations of PDF, Summary, Flashcards and Quiz. Learning-function canvases remain green, yellow and blue. English UI, separately selected study-material language, desktop priority and responsive mobile behaviour remain in place under the existing PRD.

### Saved Continuation Point

- Editable latest preview: [.working/study-preview.html](.working/study-preview.html).
- Browser version and restart instructions: [.working/browser-preview/index.html](.working/browser-preview/index.html) and [README](.working/browser-preview/README.md).
- Visual reference: [imports/front-page-reference.png](imports/front-page-reference.png).
- Latest checked views: [desktop](.working/review-round-5/startup-desktop.png), [mobile](.working/review-round-5/startup-mobile.png) and [inspection results](.working/review-round-5/inspection.json).
- Existing [DESIGN.md](DESIGN.md), [EXPERIENCE.md](EXPERIENCE.md), [.memlog.md](.memlog.md), earlier preference rounds and earlier sketches are preserved.

Next time, reopen this preview and review the latest startup and learning screens with the user before making further concept decisions. Continue the outstanding detail flows, keyboard/state coverage and usability checks from this baseline. Do not restart discovery or treat this checkpoint as approval or UX completion. No new concept work is part of today's closing checkpoint.

## Concept Preferences – Round 6: One Navigation and Refined Startup

On 19 November 2026, the user confirmed that the latest illustrated direction is the preferred basis for further refinement. The overall concept is **still provisional**, pending another visual review.

- Make **Make studying easier** somewhat smaller and use black or near-black text, retaining clear, modern typography.
- Use **one shared, clickable Home / Summary / Flashcards / Quiz menu inside the application**, at the top, on all four screens. Remove the separate preview selector and duplicate navigation.
- Retain the PDF illustration on the left and the three pastel learning cards on the right. Give them enough separation from the headline, subtitle and important form content to prevent overlap.
- Make the upload icon clearer and explore a slightly shorter upload area, while keeping generous spacing and an obvious PDF-selection action.
- Simplify or hide decorative illustrations on smaller screens; keep navigation and the form readable and accessible.
- Preserve the light grey startup canvas, pastel colours, rounded forms, soft shadows, function-themed learning views and separate Atlas-inspired Quiz answers.

### Prototype Navigation and Production Boundaries

Menu actions in this concept preview display **prewritten example screens**; they do not upload, generate or regenerate content. Home opens the startup screen for inspection and does not discard example practice state. Returning to Flashcards retains the position and shows its front; Quiz answers remain intact. This replaces Round 5's static Home indicator and disabled startup function links **for preview navigation only**.

The PRD continues to govern real study sessions. Navigation alone does not generate content. Changing PDF, study-material language or Summary detail still requires confirmed New session and fresh startup; Clear still requires confirmation. Active acknowledgement remains required before external processing for the current upload. The prototype's clickable screen menu introduces no production function or new session rule.

Continue in the existing [.working/study-preview.html](.working/study-preview.html), with [Round 5's source](.working/study-preview-round-5.html) preserved for reference. Update the browser preview and review the result before adopting any final design. Earlier rounds and the 14 November checkpoint remain historical records.

The revised preview and [browser export](.working/browser-preview/index.html) are ready for review. Checked views are saved under [.working/review-round-6](.working/review-round-6/): [startup desktop](.working/review-round-6/startup-desktop.png), [startup mobile](.working/review-round-6/startup-mobile.png), [Summary](.working/review-round-6/summary-desktop.png), [Flashcards](.working/review-round-6/flashcards-desktop.png), [Quiz](.working/review-round-6/quiz-desktop.png) and [inspection results](.working/review-round-6/inspection.json). This is evidence for the prototype only, not production functionality or final approval.

## Concept Preferences – Round 7: Neutral Home and Three-colour Brand Mark

The user requests a more neutral identity for Home while preserving the latest illustrated layout. These colours are **provisional** and must be reviewed visually before final approval.

- Give the active **Home** tab a rounded neutral grey treatment, rather than Summary green. The preview uses `#e1e5e9`, a `#737e8b` border and dark grey text, with neutral hover/focus. Keep the active location clear through shape, border, weight and `aria-current` as well as colour.
- Use muted grey-blue **`#788CA7`** for the upload cloud/arrow icon and the decorative arrow beside the PDF illustration.
- Preserve Summary green, Flashcards yellow and Quiz blue for the learning views.
- Preserve the existing three-layer logo shape and assign the upper layer to Summary green, the middle layer to Flashcards yellow and the lower layer to Quiz blue. Use the existing theme-border tones for the thin outlines so the logo stays visible against the light header:

| Logo layer | Existing colour role | Preview colour |
|---|---|---|
| Upper | Summary border | `#6c8a76` |
| Middle | Flashcards border | `#8e783e` |
| Lower | Quiz border | `#62809c` |

- Keep these three logo colours fixed across all screens. Use the same dark grey **`#343a40`** for **AI Study Buddy** and **Upload your PDF**.
- Leave layout, typography, illustration shapes/positions, soft shadows, upload dimensions, other controls and prototype behaviour unchanged. The existing pastel backgrounds and illustrative learning cards remain unchanged.

This refines visual colour roles only. It introduces no functions, production implementation or PRD changes. [Round 6's source](.working/study-preview-round-6.html) is preserved for comparison; continue reviewing the existing [.working/study-preview.html](.working/study-preview.html) before adopting these colours.

The colour preview is available in the [browser export](.working/browser-preview/index.html), with checked [desktop](.working/review-round-7/startup-desktop.png) and [mobile](.working/review-round-7/startup-mobile.png) views and [colour/contrast inspection](.working/review-round-7/inspection.json). The logo shape, layout and prototype behaviour are unchanged. Final colour approval is still pending.

## Concept Exploration – Round 8: Independent Warm Cream Home Concept

The user requests a **new Home concept variant for comparison**, with a warmer, livelier appearance. **The existing Round 7 prototype remains unchanged and is not replaced.** No new concept is approved, and this alternative is not adopted as the default in DESIGN.md.

### Warm Home Variant

- Use warm cream **`#F7F3EB`** for the Home canvas, retaining the white upload/settings card. The upload area is also white so the requested taupe icon remains distinct.
- Test warm taupe **`#9B9188`** on the upload cloud and decorative PDF arrow, with a warm neutral upload outline and soft shadow.
- Keep Home neutral, using a warm grey/greige active treatment rather than green. Preserve the menu, typography, rounded forms, dimensions and example interactions.
- Preserve the three original logo paths and use **the exact illustration-card fills**, rather than the darker border tones from Round 7: upper green `#d7e9da`, middle yellow `#f9e8b3`, lower blue `#dceff8`. Slightly stronger strokes and a subtle soft shadow separate the light pastel mark from the header. The visible product name remains dark grey `#343a40`.
- Keep the three large organic corner forms, the left PDF illustration and the right learning cards. The corner forms reuse the illustration pastels against the cream canvas, with their positions and responsive hiding unchanged.
- Restrict every variant override to **Home/startup only**. Summary, Flashcards and Quiz retain their original appearance, content and behaviour, including the original logo treatment on those screens.

### Comparison and Preservation

- Existing prototype: [.working/study-preview.html](.working/study-preview.html) and [existing browser export](.working/browser-preview/index.html), both preserved byte for byte.
- New independent concept: [.working/home-warm-cream.html](.working/home-warm-cream.html), with [Home-only colour overrides](.working/home-warm-cream.css), and [interactive browser export](.working/browser-preview/home-warm-cream.html).
- Side-by-side comparison from actual prototype captures: [.working/home-colour-comparison.html](.working/home-colour-comparison.html) and [browser comparison](.working/browser-preview/home-comparison.html).
- Checked warm views: [desktop](.working/review-home-warm-cream/startup-desktop.png), [mobile](.working/review-home-warm-cream/startup-mobile.png) and [inspection results](.working/review-home-warm-cream/inspection.json).

The pastel logo is decorative and paired with the high-contrast product name; its soft shadow separates edges without changing the colours' measured contrast. This is a visual experiment only. PRD requirements and production functionality remain unchanged; review both Home versions before selecting a direction.

## Concept Preferences – Round 9: Retain Grey Home and Strengthen the Shared Logo

The user chooses to continue with the **original light-grey Home**, rather than the cream or warm-neutral alternative. This confirms the working basis; it is **not final approval of the complete concept**. Preserve all earlier concepts for comparison.

### Shared Brand Mark on Every Screen

Keep the existing three-layer icon form and the dark-grey **AI Study Buddy** wordmark. Use one shared set of fixed, more saturated logo colours on Home, Summary, Flashcards and Quiz:

| Layer | Function family | Preview colour |
|---|---|---|
| Upper | Summary green | `#4f9f6f` |
| Middle | Flashcards yellow | `#e0ae26` |
| Lower | Quiz blue | `#4b9bc8` |

These stronger hues coordinate with the Home illustration-card colours while making the layers distinct, especially the yellow. The same shared header/logo definition is used on every screen; colours do not change with the active function. Keep the original paths, stroke, size rules and positioning.

### Home Upload and PDF Arrow

Use **`#f9e8b3`** for both the upload cloud and the decorative arrow beside the PDF illustration. This value is taken directly from the existing Flashcards illustration-card background, not approximated. Keep both shapes, sizes and positions unchanged.

### Preservation and Review

Only four CSS colour values change in the current prototype: the three shared logo colours and the upload/PDF-arrow accent. Keep the Home canvas `#edeef2`, neutral active Home tab, original bubbles, illustrations, white upload card, typography, layout, navigation, content and behaviour. Summary, Flashcards and Quiz change only in the shared logo colours.

The current prototype remains [.working/study-preview.html](.working/study-preview.html) with [its browser export](.working/browser-preview/index.html). The previous neutral version is saved as [Round 7 source](.working/study-preview-round-7.html) and [browser archive](.working/browser-preview/neutral-home-round-7.html); the independent warm Home concept and previous comparison captures remain unchanged. Review the result before final colour/design approval. No functional or PRD changes are introduced.

Checked [desktop](.working/review-round-9/startup-desktop.png) and [mobile](.working/review-round-9/startup-mobile.png) views and [inspection results](.working/review-round-9/inspection.json) are saved. The browser check confirms the same three logo colours on all four screens and that both Home icons exactly match the Flashcards-card fill. The pale icons remain decorative beside visible action text; no icon-only action is introduced.

## Concept Decision – Round 10: Preferred Home Concept and Final Two Icon Adjustments

The user identifies the existing light-grey Home with the three-colour logo as the **preferred Home concept**, with only these two adjustments:

- **PDF illustration arrow:** dark grey `#343a40`, reusing the existing brand-text colour.
- **Upload cloud:** golden yellow `#e0ae26`, bound directly to the shared logo's Flashcards-yellow variable so the colours remain identical.

Keep the logo exactly as it is: upper green `#4f9f6f`, middle yellow `#e0ae26`, lower blue `#4b9bc8`, with unchanged form, stroke, sizes and dark-grey wordmark on all four screens. Preserve the light-grey canvas, pastel corner forms, illustration cards, white upload card, navigation, typography, layout, content and interactions.

Only two CSS declarations change in this refinement. [The previous source](.working/study-preview-round-9.html) and all earlier concept variants remain preserved. Continue from the existing [.working/study-preview.html](.working/study-preview.html) and [browser preview](.working/browser-preview/index.html).

This records the user's preferred **Home** direction. It does **not** mark the complete UX phase as finished, approve every remaining screen/state or change the PRD. DESIGN.md and EXPERIENCE.md remain drafts; the outstanding UX work continues from this Home concept.

Checked [desktop](.working/review-round-10/startup-desktop.png) and [mobile](.working/review-round-10/startup-mobile.png) views and [inspection results](.working/review-round-10/inspection.json) are saved. Browser inspection confirms the upload cloud exactly matches the logo's yellow, the PDF arrow matches the dark-grey wordmark, and all four screens retain the same unchanged logo colours. An exact source comparison confirms that only the two requested colour declarations changed.

## Concept Selection — Round 11: Four-screen Baseline and Documentation Checkpoint

The user confirms the latest Home, Summary, Flashcards and Quiz as the **selected concept**, extending Round 10's Home preference to all four screens. No visual or functional changes are requested in this checkpoint; only concept terminology, documentation and quality/Source Control review are updated.

Keep the illustrated grey Home, current headline/type/layout/navigation, the identical shared three-colour logo, exact golden-yellow upload cloud and dark-grey PDF arrow. Keep Summary green, Flashcards yellow and Quiz blue, white content cards, function-themed controls and separate rounded Quiz answer boxes. Minor refinements can be reviewed later without reopening the entire concept exploration.

The 54 initial Source Control changes were reviewed: 52 UX artifacts and two log files. Preserve source, browser exports, reference, concept history and QA evidence. No exact duplicates or disposable temporary files were found, and no files are deleted. The [artifact guide](README.md) records their roles; historical comparisons are labelled accordingly. Private test PDFs remain ignored and outside the commit.

Updated DESIGN.md and EXPERIENCE.md record the current baseline and explicit outstanding UX coverage. PRD/addendum, required BMAD filenames, existing skills and configuration remain unchanged. The user now requests commit and push of this documentation/concept checkpoint; this supersedes the earlier local-only/no-automatic-push instruction for this publication. No UX completion or next phase is authorised.

Fresh [selected-concept checks and captures](.working/review-selected-concept/) cover all four menu choices, eight desktop/mobile widths, startup acknowledgement gating, card/Quiz state preservation, source-panel return and visible keyboard focus, with no script exceptions. The [inspection record](.working/review-selected-concept/inspection.json) includes static integrity and colour checks. These are prototype checks, not completed production, AI-quality or full usability validation.

## Concept Exploration — Round 12: Compare Session Actions on Desktop and Mobile

The user chooses to **see both placement options before selecting one**:

- **Session menu:** a discrete Session disclosure beside the document context, containing New session and Clear.
- **Visible actions:** two directly visible New session and Clear buttons in the same document area.

Compare placement, discoverability, number of interactions and responsive behaviour using the same saved example content, existing Home/Summary/Flashcards/Quiz navigation, shared logo, function themes, typography and rounded controls. Both are separate concept sketches; neither replaces the selected concept or establishes the final placement.

The [comparison](.working/session-actions-round-12/session-actions-comparison.html) offers Desktop and Mobile preview widths. Desktop keeps each app at readable width, stacked for comparison; Mobile places the two narrow apps alongside each other when space permits, otherwise stacks them. Individual sources are [Session menu](.working/session-actions-round-12/session-menu.html) and [Visible actions](.working/session-actions-round-12/session-buttons.html). [Browser preview instructions](.working/browser-preview/README.md) link the standalone exports.

Both concepts use the same proposed English confirmation copy and PRD behaviour. Cancel or Escape preserves the current session and practice state. Confirming either action removes the current session's working state and returns to empty ordinary startup; the original file on the device is unaffected. A cancelled/rejected later file selection cannot restore the ended session. Fresh startup requires a PDF, output choices and active acknowledgement before the saved example is displayed. No PDF contents are read and no AI calls occur.

New session expresses the intent to begin with another PDF, language or Summary detail; Clear expresses the intent to empty the session. They do not have different confirmed cleanup outcomes. The concepts do not claim provider-side deletion or completed production/session-isolation tests.

The selected [.working/study-preview.html](.working/study-preview.html), its [main browser export](.working/browser-preview/index.html), earlier concepts and PRD remain unchanged. Review both placements and confirmation wording before adopting an option. DESIGN.md and EXPERIENCE.md remain drafts and UX stays open.

Checked captures: [Session menu desktop](.working/review-session-actions/session-menu-desktop.png), [open menu](.working/review-session-actions/session-menu-open-desktop.png), [visible actions desktop](.working/review-session-actions/visible-actions-desktop.png), [paired mobile views](.working/review-session-actions/mobile-comparison.png), [New session on mobile](.working/review-session-actions/new-session-mobile.png) and [Clear on mobile](.working/review-session-actions/clear-mobile.png). [Inspection results](.working/review-session-actions/inspection.json) record navigation, six responsive widths, cancellation/confirmation, fresh acknowledgement, focus containment/return, source return and empty-session guards. These checks do not select a concept or establish actual usability outcomes.

For the placement review, note that these actions are next to the document context on learning screens. Active Home inspection keeps settings locked and explains how to return to a learning tab for New session. Direct access from active Home remains open for assessment; no extra Home controls are adopted here. Dialog descriptions include both the loss warning and the next-step paragraph for assistive technology.

## Concept Decision — Round 13: Keep Only New session

The user agrees that New session and Clear duplicate the same confirmed outcome and create confusion. **Keep only New session** as the explicit session-ending action. Remove the separate Clear command from the current concepts and active product requirements.

Cancel or Escape keeps the current PDF, choices, acknowledgement, generated material and practice progress unchanged. Confirming New session removes the current working state and returns to empty Home, with the original device file unaffected. **The student may stop there**; choosing a new PDF/settings and acknowledging external processing is required only when starting again. A cancelled/rejected later file choice never restores the ended session. Late results and provider-retention rules retain their existing protections.

The PRD retires **FR-16** without renumbering IDs and folds its protections into FR-15/shared acceptance rules. PRD/addendum and Product Brief/addendum are aligned with this simplification. Previously final PRD status remains unchanged; this scoped requirement update does not complete UX or start the next BMAD phase.

The [current comparison](.working/session-actions-comparison.html) now compares a **Session menu containing New session** with **one visible New session button**. Navigation, logo, pastel themes and baseline styling are unchanged. The user has chosen the action, **not its final placement**. Both remain reviewable on desktop and mobile, with the one New session confirmation. The selected main prototype remains unchanged until a placement is adopted.

Round 12 sources, shared authoring parts and browser exports are preserved in [.working/session-actions-round-12/](.working/session-actions-round-12/); its existing two-action captures remain historical evidence. Current one-action checks and captures are recorded separately in [.working/review-new-session/](.working/review-new-session/). No files are deleted.

The current [desktop menu](.working/review-new-session/session-menu-desktop.png), [desktop button](.working/review-new-session/visible-button-desktop.png), [mobile comparison](.working/review-new-session/mobile-comparison.png), [open menu](.working/review-new-session/session-menu-open-desktop.png) and [mobile confirmation](.working/review-new-session/new-session-mobile.png) are saved with [inspection results](.working/review-new-session/inspection.json). Checks confirm exactly one New session action per concept, no Clear command, retained navigation, responsive layout, cancellation/focus preservation, empty Home and fresh-start acknowledgement. These are concept checks, not full production or usability validation.

## Concept Decision — Round 14: Select Visible button

The user chooses **Visible button**. Adopt **one directly visible New session button beside the document information** on Summary, Flashcards and Quiz. It sits alongside the document context at desktop width and wraps below it on mobile, using the already reviewed white rounded control and function-themed borders/hover colours. Do not use a Session disclosure or reintroduce Clear in the selected main preview.

The selected [.working/study-preview.html](.working/study-preview.html) and [main browser export](.working/browser-preview/index.html) now include this placement and the existing confirmed reset. Keep the illustrated empty Home entry point, navigation, logo, function canvases, typography, content cards and practice/source interactions. The prior main source is preserved as [.working/study-preview-round-11.html](.working/study-preview-round-11.html). Comparison sources and earlier alternatives remain available for traceability; their shared builder now uses that frozen baseline rather than the newly promoted main.

Before the first example startup/reset, the prototype may open labelled prewritten examples through its learning menu, preserving the previously requested inspection experience. Once New session is confirmed, navigation or restored presentation choices cannot resurrect that ended example: Home stays empty until fresh PDF metadata, language, Summary level and acknowledgement are supplied. This remains a UX preview without PDF-content reading or AI calls, not a production-session policy change.

Selecting this button does not settle direct access from active Home, which still shows locked settings and directs the student to a learning screen. Final copy, full state coverage and actual user walkthrough remain open. The New session requirement from Round 13 is unchanged; no additional PRD/brief revision is required for placement alone. DESIGN.md and EXPERIENCE.md remain drafts, with no UX completion or next BMAD phase.

Current main-preview checks are saved under [.working/review-visible-button/](.working/review-visible-button/): [Home desktop](.working/review-visible-button/home-desktop.png), [Home mobile](.working/review-visible-button/home-mobile.png), [visible button desktop](.working/review-visible-button/flashcards-desktop.png), [visible button mobile](.working/review-visible-button/flashcards-mobile.png), [confirmation mobile](.working/review-visible-button/new-session-mobile.png) and [inspection](.working/review-visible-button/inspection.json). They cover empty illustrated Home, initial example navigation, selected action on learning screens, cancellation/focus, confirmed empty restart, rejection/acknowledgement guards and blocked old-screen restoration. Original Home markup/styles are preserved, and authoring builds reproduce the same main/comparison sources. This is prototype evidence, not final UX or production validation.

## Preview Verification — Round 15: Fresh Visible button Entry

The user reports that the selected New session button is missing **in the chat preview**. Inspection finds the button present in the current source and exact browser export; no screen-specific rule hides it on Summary, Flashcards or Quiz. A stale chat copy or earlier presentation state is possible, but the exact cause is not established.

Provide a [fresh review fragment](.working/study-preview-visible-button-r15.html) and [browser entry](.working/browser-preview/visible-button-r15.html) with a new path, isolated presentation-state key and Summary initially open with labelled example content. This shows the chosen control immediately. The app styling, placement and behaviour remain the selected Round 14 concept; the canonical main still opens the illustrated empty Home. This is a review entry, not another concept or new production route.

Actual browser checks verify visible, enabled, hit-testable New session controls within the document-information row on **Summary, Flashcards and Quiz at 1536, 390 and 320px**, in both the canonical main and fresh review: 18 explicit cases. Each opens the confirmation and focuses Cancel. The fresh review ignores earlier main-preview presentation keys. Six top-of-screen captures and [inspection](.working/review-preview-visibility/inspection.json) are saved under [.working/review-preview-visibility/](.working/review-preview-visibility/). No layout changes, PRD changes, UX completion, commit or push are part of this verification.

## Concept Exploration — Round 16: Home with an Active Study Session

The user asks to resolve Home during an active session before continuing other UX work. Without an active session, retain the existing PDF upload and settings. With an active session, show the document name, selected study-material language and Summary detail as read-only information, a way to continue studying, and New session with confirmation. Language and detail cannot be changed inside an active session.

The [new separate concept](.working/home-active-session-review.html) opens Home with labelled prewritten `Studieteknikk.pdf` example content, Norwegian Bokmål and Detailed. [Open the browser export](.working/browser-preview/home-active-session.html) to inspect Desktop/Mobile widths. Continue studying initially opens Summary; after visiting another learning function it returns there. Card position and Quiz answers/feedback are preserved, while returning to Flashcards still shows the retained card's front. Continue moves keyboard focus to the visible destination navigation button. This destination treatment and all new wording are proposed for review, not final decisions.

New session on Home uses the same confirmation and cleanup rules as the selected learning-screen button. Cancel/Escape keeps the session and returns focus to the Home trigger. Confirmation removes the example session and reveals the original empty Home; the student can stop without uploading again. Starting later requires fresh PDF metadata, language/detail and acknowledgement. Rejected file selection cannot restore the ended example. The review uses metadata and saved example text only, reads no PDF contents and makes no AI calls. Reloading the concept deliberately starts its labelled fixture again; it does not recover a real session or persist study data.

The grey Home canvas, white raised card, neutral active Home tab, shared three-colour logo, typography, pastel corner forms, left PDF and right learning illustrations are preserved. Settings and actions stack on mobile and decorations remain hidden. The selected Summary, Flashcards and Quiz content/interactions are reused without new features. [Desktop](.working/review-active-home/active-home-desktop.png), [mobile](.working/review-active-home/active-home-mobile.png), [mobile confirmation](.working/review-active-home/home-new-session-mobile.png) and [empty Home after reset](.working/review-active-home/empty-home-mobile.png) are saved for comparison.

The editable [concept source](.working/home-active-session.html), literal source parts and preview-width shell are reproduced by `.working/home-active-session-build.py`. They do not overwrite [.working/study-preview.html](.working/study-preview.html), its [main browser export](.working/browser-preview/index.html), the fresh Round 15 entry or earlier concepts. PRD/addendum and reference image remain unchanged. DESIGN.md and EXPERIENCE.md stay draft; the next step is the user's visual review of this concept before adoption. No production implementation, new BMAD phase, UX completion, commit or push is included.

Actual browser checks at 1536, 1280, 1024, 768, 390 and 320px pass without page/control overflow or illustration/card collision. Continue destination, card/Quiz preservation, Cancel/Escape/focus containment and return, confirmed empty Home, rejected-file protection, fresh acknowledgement and locked new choices pass with no script exceptions. A source review identified a hidden-focus risk after Continue; moving focus to the visible destination tab resolves it and the browser check verifies that handoff. [Inspection results](.working/review-active-home/inspection.json) include syntax, unique ID/ARIA links, exact export, draft status and unchanged protected main/PRD/reference files. These are targeted concept checks, not full accessibility, production or usability validation. Impeccable's installed craft guidance was used under the previously documented unavailable-engine fallback; no skills/configuration were changed.

## Concept Refinement — Round 17: Balanced Active Home Actions

The user likes the active Home concept and asks to refine **only Continue studying and New session** before approval. Both now share 56px height, 16px text at weight 500, 15px corner radius and 14px spacing. Desktop uses equal-width columns; mobile uses equal-width stacked buttons with the same gap. Continue retains the existing green primary fill with less bold text and 14px between label and arrow. New session remains secondary with a light neutral `#f2f3f5` fill and neutral hover treatment.

Review the [updated desktop/mobile concept](.working/home-active-session-buttons-review.html), [desktop capture](.working/review-home-buttons/home-buttons-desktop.png) and [mobile capture](.working/review-home-buttons/home-buttons-mobile.png). The existing [browser entry](.working/browser-preview/home-active-session.html) is updated. [Round 16 source, CSS and export](.working/home-active-session-round-16/) are preserved; its earlier captures remain unchanged.

Only active-Home action CSS changes: markup, JavaScript, copy, behaviour and all other styling remain identical. The selected main prototype, learning screens, PRD and reference are unchanged. [Targeted browser checks](.working/review-home-buttons/inspection.json) verify equal geometry/type/radius, spacing and responsive arrangement at 1536/1024/768/540/390/320px without overflow. Real pointer clicks verify Continue/focus and New session/Cancel/focus return; no script exceptions. Independent visual review confirms the requested balance. The updated concept still awaits user approval, and UX remains open. No commit or push is included.

**User feedback after Round 17 — 20 November 2026:** “Det var bra” confirms retaining this revised button treatment for the active Home concept. Record the buttons as selected. This acknowledgement does not close the UX phase or promote the separate active Home concept into the main prototype; broader state/copy review remains open. No further visual changes are made.


## Concept Decision — Round 18: Adopt Active Home and Both Session Flows

The user approves the active Home concept and the two study-session flows. Adopt it in [.working/study-preview.html](.working/study-preview.html) and [the main browser export](.working/browser-preview/index.html), retaining the selected Round 17 button treatment and all other established visual components. The main still opens the illustrated empty Home. Once the preview has an active example or metadata-only session, Home shows filename, fixed study-material language and Summary detail, Continue studying and direct New session.

**Continue studying** returns to the last visited learning tab, preserving existing content and practice progress. If no learning tab has yet been visited, it opens Summary. Returning to Flashcards preserves the card position and shows its front under the existing rule; Quiz answers and feedback remain intact.

**New session** uses the existing confirmation dialog from Home and the learning screens. Cancel/Escape preserves the complete working session and returns focus to its invoking control. Confirmation clears the working session and returns to empty Home; the original local file is unaffected and the student may stop there. Starting later requires fresh PDF metadata/settings and active acknowledgement. The approved flow does not change the PRD's real processing, cleanup or late-result protections.

The [fresh active Home entry](.working/study-preview-active-home-r18.html) and [browser export](.working/browser-preview/active-home-r18.html) open the labelled prewritten fixture for review. The prior main is preserved as [.working/study-preview-round-17.html](.working/study-preview-round-17.html) and [home-before-active-r17.html](.working/browser-preview/home-before-active-r17.html). The separate Round 16/17 concepts remain historical exploration; the [Round 15 diagnostic entry](.working/study-preview-visible-button-r15.html) stays frozen and is no longer the current review link.

This remains a metadata-only UX prototype with prewritten study examples, no PDF-content processing or AI calls, and no real-session restoration across reloads. DESIGN.md and EXPERIENCE.md remain `status: draft`; loading/error/coverage states, remaining learning/source flows, broader keyboard/state checks and actual usability review remain open. No PRD change, production implementation, UX completion, next BMAD phase, commit or push is authorised by this adoption.


[Round 18 checks and captures](.working/review-active-home-selected/) cover both the main and fresh review at 1536/1280/1024/768/390/320px without overflow or decoration collisions. They verify empty/active Home, Continue destination and retained card/Quiz state, Cancel/Escape/focus, confirmed empty Home, fresh-start guards and blocked restoration of ended examples, with no script exceptions. JavaScript, ID/ARIA references, exact exports and reproducible builds pass; protected PRD/reference/earlier concepts remain unchanged and private test PDFs stay ignored. These are targeted prototype checks, not production validation or a full accessibility/usability audit.


## Concept Exploration — Round 19: Processing, PDF Problem and AI Failure

The user agrees to three separate visual sketches before selecting their presentation: [processing](.working/status-loading.html), [PDF problem](.working/status-pdf-problem.html) and [AI failure](.working/status-ai-error.html). [Compare all three](.working/processing-states-comparison.html) or use the [browser comparison](.working/browser-preview/processing-states.html). Retain the selected Notatkort styling, shared navigation/logo, function colours and existing session rules. This is visual exploration, not adoption or a change to the selected main.

- **Processing:** default to **Generating summary**. A labelled preview-only selector exposes exactly **Checking PDF**, **Extracting text**, **Generating summary**, **Generating flashcards** and **Generating quiz**. Do not invent percentages, time estimates or automatic completion.
- **PDF problem:** show a password-required PDF on the neutral canvas, with no Summary available. Do not add password unlocking or retry; recovery uses the existing confirmed New session flow.
- **AI failure:** show failed Flashcards generation on the yellow function canvas while preserving valid Summary. Summary navigation stays available and output choices remain locked. Manual **Try again** opens **Generating flashcards** and stays pending, without an automatic result or retry.

The `processing-states-build.py`, `-parts.html`, `-styles.css` and `-logic.js` files author these separate sketches and comparison. Their labels and prewritten examples describe simulated states only: no PDF contents are read and no AI/API call is made. Existing source and coverage rules, processing restrictions, confirmation/cleanup and late-result protections remain governed by the PRD/addendum. The selected main, Round 18 entries and PRD remain unchanged.

Review the three presentations on desktop/mobile before adopting or refining them. These examples do not complete the remaining processing/error/coverage, source or learning flows. DESIGN.md and EXPERIENCE.md stay `status: draft`; UX remains open, with no production implementation, next BMAD phase, UX completion, commit or push included.


[Round 19 checks and captures](.working/review-processing-states/) record all three sketches at six widths (1536/1280/1024/768/390/320px), the 390px-wide mobile comparison, five exact operation labels and pending-only processing. Checks verify manual Try again, preserved Summary/navigation, no password/unlock action, and Cancel/confirmed empty Home in each sketch, with no overflow or script exceptions. ID/ARIA references, exact exports and reproducible builds pass; no API/timer/storage behaviour is introduced, and protected main/Round 18/PRD/reference files remain unchanged. This is targeted prototype evidence, not production validation or a full accessibility/usability audit.

## Concept Decision and Continued Review — Round 20: Select Status Patterns and Cover Remaining UX

On 24 November 2026, the user explicitly approves **all three Round 19 status concepts on desktop and mobile** and asks to continue the remaining UX against the PRD. This supersedes Round 19's pending-selection wording, while preserving that round and its checks as history. Keep the established Home/Summary/Flashcards/Quiz appearance, English interface, fixed Norwegian Bokmål/English study-material language and Brief/Detailed Summary detail.

Adopt the processing, password-required PDF and Flashcards AI-failure presentations into the selected [main concept](.working/study-preview.html) and [browser index](.working/browser-preview/index.html). Preserve the previous main in [study-preview-round-19.html](.working/study-preview-round-19.html) and [main-before-statuses-r19.html](.working/browser-preview/main-before-statuses-r19.html). The [fresh Round 20 status review](.working/study-preview-status-r20.html) / [browser entry](.working/browser-preview/statuses-r20.html) provides a current inspection entry; scenario/operation controls stay outside the app and are labelled preview-only.

The selected processing pattern names exactly the operation represented, with no artificial percentage or automatic completion. Password-required PDFs offer no unlocking/password workflow; the existing confirmed New session returns to empty Home. The selected Flashcards AI-error presentation retains valid Summary and locked choices; manual Try again opens pending Generating flashcards without inventing a successful result. Selection of these patterns does not establish real extraction, generation, provider deletion, source validity or late-result isolation.

Continue the remaining review through [remaining-ux-review.html](.working/remaining-ux-review.html) / [remaining-ux.html](.working/browser-preview/remaining-ux.html). The separate [reliability concept](.working/reliability-review.html) proposes other PDF/coverage outcomes, reduced/invalid source results, setup/service failures and saved-demo/live-action explanation. The separate [learning/source concept](.working/learning-flows-review.html) proposes complete card/Quiz practice, results/review/restart and multiple-reference inspection. **All of these new presentations and copy remain pending review and are not adopted into the main.** They reuse existing requirements; they add no app settings, product modes or numeric upload limits.

The [PRD coverage matrix](.working/ux-coverage-review.md) distinguishes selected examples, proposed review coverage, actual remaining usability work and production/evaluation limits. Use the PRD's existing UJ-1 for the walkthrough. Camilla states on 24 November that her preferred study order is Summary → Quiz → Flashcards; a proposed walkthrough can follow that order after normal startup and include source inspection/session ending as applicable. This records her stated preference, not an observed usability result. Prototype inspection is not evidence of completed real-user research, live AI quality or a full accessibility audit. Open parser/provider/resource/cleanup choices remain technical handoff work rather than reasons to stop reviewing the UX presentations.

Both UX contracts remain `status: draft`. Review the new presentations on desktop/mobile, resolve findings, complete systematic keyboard/state checks and record actual walkthrough evidence before any separate decision to finish UX. This scope includes no production implementation, PRD change, UX completion, next BMAD phase, automatic commit or push.

[Round 20 inspection and captures](.working/review-ux-continuation/) now record passing targeted checks: main/session flows at six widths; 12 selected-status layouts; 17 reliability scenarios at three widths plus nine manual retry branches; both study languages and the complete 6/8 = 75% Quiz/card/source flows; and nine combined-review layouts. Explicit confirmation/locking, draft/function resumption, same-set restarts, multiple sources, source/focus return, Cancel/Escape/reset and keyboard arrow-key selection without feedback pass, with no script exceptions. Final refinements retain soft green/red answer feedback with explicit labels, aligned/wrapping locked wrong-question review and student-facing **Live generation not available** setup copy without service-key details. The [report](.working/review-ux-continuation/inspection.json) includes five exact exports, valid IDs/ARIA/links and draft status, ten reproducible fragments and 20 unchanged protected artifacts; 22 captures are saved. Independent PRD/source/contract and 15-capture review finds no material issue. These checks do not constitute a full keyboard/accessibility audit, actual user walkthrough or live content-quality validation. New reliability/learning presentations remain pending user review and UX stays open/draft.

## Concept Refinement — Round 21: Reusable Reliability Feedback and Mobile Alignment

On 24 November, the user asks whether all 17 reliability cases belong in a realistic solo-project v1, asks for a few reusable UI patterns, and requests simpler student messages and centred mobile content/actions. Assess the cases against the existing PRD/addendum. All 17 are relevant requirements or test fixtures; they do not become 17 independent product features, custom screens or student-selectable scenarios. No formal new features or advanced PDF detection are introduced.

Reuse four outcome presentations — **document error**, **generation error**, **usable-content notice** and **demo information** — together with the existing operation-specific **pending** card. The internal classification is 13 blocking errors, three notices with usable content and one demo-information state. Blocking applies to the rejected PDF or attempted output; it does not invalidate valid material elsewhere in the active session. The [internal scenario mapping](.working/reliability-scenarios.md) retains all reason IDs, publication/state rules and detection/test prerequisites. Keep those technical distinctions in development/review evidence; they are not app settings or student error wording.

Student messages explain what could not be read/created, what material remains and the available next action. They avoid malformed-structure, reference-validation and provider-key jargon. A reduced set remains usable with its actual count and a short notice; demo information labels saved playback rather than suggesting failure. Internal checks still reject malformed replies as a whole, withhold a whole new Summary with any invalid reference and omit whole affected cards/questions only from otherwise valid sets. Zero valid items produces an error, not an empty scored Quiz. No automatic retry, repair or refill is introduced.

Flashcards/Quiz failure and pending states retain valid Summary, other existing content and practice progress. Retrying the failed function must not clear another function's material, card position or Quiz answers. Existing function-return rules still apply. These fixtures represent the intended retained-state behaviour; real request cancellation, cleanup, late-result isolation and all production state combinations require implementation verification.

Use one shared mobile rule at app widths up to 540px for centred Flashcards/Quiz card/question/option/help/feedback/result/end/count text, notices and action content/groups, including empty-generation cards. Centre shared loading/error box headings, body/support text and recovery controls, with the status icon above the heading. Summary reading prose/notices, the source excerpt reader, header/navigation/document information and desktop layout retain their established treatment. This refines the selected visual system rather than establishing a new concept.

The [fresh Round 21 chat-review fragment](.working/remaining-ux-review-r21.html) avoids relying on an earlier embedded copy; the stable [combined source](.working/remaining-ux-review.html) and [browser entry](.working/browser-preview/remaining-ux.html) continue. Additional reliability and complete learning/source presentations remain pending user review. Plain-English status copy and shared mobile alignment also refine the selected main and current Round 20 status entry. The [prior Round 20 browser exports](.working/round-20-before-simplification/) preserve the version before these refinements. The separate Round 19 sketches, prior main and Round 18 entries remain historical copies.

PDF loss/uncertainty/omission examples represent PRD FR-40/FR-41 outcomes, not an implemented detector. Architecture must verify observable extraction signals and stop criteria; no fixture, empty/nonempty page or location match establishes complete coverage or factual support. A specific omitted figure may only be named when detected; the synthetic fixture is not evidence that the app can detect it. OCR, repair and advanced diagram interpretation stay excluded. The [coverage review](.working/ux-coverage-review.md) separates these handoff facts from the reusable UX.

Round 20 checks remain evidence of their recorded version, not verification of this refinement. DESIGN.md and EXPERIENCE.md remain draft, and UX remains open. Review the revised presentation/copy and complete remaining keyboard/usability work before a separate completion decision. This round changes no PRD requirement, starts no next BMAD phase, implements no production pipeline and includes no commit or push.

[Round 21 inspection and captures](.working/review-v1-error-simplification/) record passing targeted prototype checks: all 17 cases at 1280/390/320px, nine manual retries, valid Summary and locked Quiz answers retained across four Flashcards failures, and Flashcards position retained across three Quiz failures. Main-state preservation, both study-material languages, complete learning/source flows and the combined review also pass, with no script exceptions. The 22 captures and [report](.working/review-v1-error-simplification/inspection.json) bind evidence to current source hashes. Existing product CSS is unchanged except for one mobile-only rule; five exact exports, valid IDs/references/JavaScript and four reproducible builders pass. PRD, imported references, earlier frozen concepts and installed skills remain unchanged. These are synthetic prototype checks, not PDF-detector, live-AI, production-state or actual-user validation. UX remains open/draft.


## Planning Completion — Round 22: Selected Concept and Consolidated Check

On 24 November 2026, the user says the refined concept looks good and requests a final combined PDF-upload → Summary/Flashcards/Quiz → New session check, including sources, error handling, mobile and PRD conformity. The user authorises completion for the planning phase if no critical gaps remain, with no architecture, commit or push. This supersedes the earlier instruction to keep the UX planning phase open; earlier round wording is historical.

The consolidated check finds **no critical or high UX planning gaps**. Select the latest illustrated grey Home, shared identity, full learning/source flows, four reliability outcomes plus processing and Round 21 mobile rules as one concept. Minor refinements remain possible during implementation. DESIGN.md and EXPERIENCE.md now have `status: final` and `planning_status: complete`; final means UX planning complete, not production/evaluation complete.

Five reviewed exports are copied unchanged into [mockups/](mockups/), preserving all working sources, references and old concepts. The basic shell's one-question example remains a partial illustration; the complete learning reference defines full Quiz/cards/source behaviour. The [final coverage inventory](.working/ux-coverage-review.md) maps every IA surface. No new product functionality, layout or PRD requirement is introduced.

[Final walkthrough evidence](.working/review-final-ux/inspection.json) records three complete sequences at 1280/390/320px, both study languages and Summary levels across the runs, fresh acknowledgement, fixed choices, multiple original sources, explicit confirmation/locked review, actual 7/8 = 87.5%, Home resume and Cancel/confirmed empty reset. Nine layouts and 12 captures pass without overflow/script exceptions. The unchanged Round 21 source hashes retain the prior 17-case/nine-retry/state-preservation evidence. Independent PRD, contract and 16-capture mobile/desktop reviews find no critical/high blocker.

Before closure, three medium documentation issues were resolved: stale pending/status wording, a named/numbered UJ-1 with failure branches and explicit contrast targets. Inspiration/reference inventory was completed and four small wording clarifications from structural/prose review applied. Real extraction/source/structure enforcement, valid reduced outputs, production isolation/cleanup, provider configuration, permitted FR-42 demo sets/quality, full accessibility and observed student walkthroughs remain implementation/evaluation obligations. They are not falsely claimed as completed UX tests.

[The consolidated report](validation-report.md) and [HTML twin](validation-report.html) distinguish resolved documentation issues and nonblocking follow-up. The PRD, imported reference, existing concept sources, BMAD skills/configuration and private PDF exclusions are unchanged. No files are deleted or moved. Architecture has not started, and nothing is staged, committed or pushed.


## Post-finalisation Requirements Alignment — 26 November 2026

The user explicitly approves revised PRD FR-40/FR-41 and corresponding brief/addendum/UX alignment. Generate study material from readable, source-verifiable PDF text despite uninterpretable images, figures or tables. Where observable evidence indicates content may not have been included, use the existing nonblocking notice surface and name only the known limitation and affected physical pages where known. Never infer excluded information or imply complete-PDF coverage.

Stop only when insufficient usable text remains for meaningful source-grounded study material, or concrete extraction failures make retained main text unusable or its meaning unreliable, alongside the PRD's detected file errors. Missing graphical/table content, unknown full-PDF coverage, generic parser warnings and plain/layout differences alone do not require whole-PDF rejection. Explain a detected blocking problem and offer applicable manual retry or another PDF through New session. Architecture must verify operational criteria; detection of every omission is not promised.

This approved policy supersedes earlier incidental-only notices and blanket material-loss/uncertain-coverage blocking wording in this history and the preserved prototype fixtures. [EXPERIENCE.md](EXPERIENCE.md), the [current scenario mapping](.working/reliability-scenarios.md), [coverage matrix](.working/ux-coverage-review.md) and [derived constraint extract](.working/prd-ux-constraints.md) carry the revised implementation meaning. Legacy fixture/reason IDs remain traceable; their names are not rejection rules.

Reuse the selected document-error, generation-error, usable-content notice, demo and pending presentations. No redesign, prototype HTML/JavaScript/CSS/mockup change or browser-test rerun is part of this documentation alignment. The original 17-case/13-error classification and Rounds 20–22 checks remain prior-scope evidence. The selected visual identity, fixed English UI, output choices, sources, session and preservation rules are unchanged.

Accuracy/source-validation rules and the agreed 9/10/all-smaller-set thresholds are unchanged. Review generated material against original-PDF readable text within the declared scope and record visual/table omissions separately; locating an excerpt is not proof of factual support. No OCR, advanced figure/table interpretation, automatic retry/repair/refill or new detector is introduced. The [validation report](validation-report.md) and [HTML twin](validation-report.html) record this post-finalisation scope note separately from the original UX verdict.
