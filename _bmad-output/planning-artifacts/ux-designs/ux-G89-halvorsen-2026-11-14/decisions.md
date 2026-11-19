# AI Study Buddy — UX concept decisions

## Current selection — 19 November 2026

**Selected concept — UX in progress.** The user has selected the latest **Home, Summary, Flashcards and Quiz** together as the concept for continued UX work. Use [.working/study-preview.html](.working/study-preview.html) and [the current browser export](.working/browser-preview/index.html). The selected Home includes Round 10: light-grey canvas, unchanged green/yellow/blue logo, golden-yellow upload cloud `#e0ae26` and dark-grey PDF arrow `#343a40`. The learning views retain their existing function-themed pastels, Notatkort foundation and separate rounded Atlas-inspired Quiz answers.

Minor refinements remain possible. Selection does not complete the UX phase or approve every remaining interaction/state. DESIGN.md and EXPERIENCE.md retain `status: draft`. Complete loading/error/coverage, New session/Clear and remaining learning/source states, systematic keyboard/state checks and actual usability review before a separate UX-completion decision. Do not start the next BMAD phase.

Use **concept** for preliminary sketches and variants. BMAD filenames/structure remain unchanged. Earlier rounds below preserve what was preferred, pending or superseded at that time; their historical status is not the current selection. See [the artifact guide](README.md) for current versus historical files.

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
