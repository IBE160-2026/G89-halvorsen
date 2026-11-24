      // Internal review fixtures, not PDF detection or production acceptance rules.
      // Reason codes stay here; the product renders one of four reusable patterns.
      // Pending is the existing, separate processing pattern. No API, timer or storage.
      const reliabilitySelect = root.querySelector('[data-reliability-scenario]');
      const reliabilityHelp = root.querySelector('[data-reliability-help]');
      const reliabilityInitialHelp = reliabilityHelp.textContent;
      const reliabilityStatus = root.querySelector('[data-status-view]');
      const reliabilityHeading = root.querySelector('[data-status-heading]');
      const reliabilityRetry = root.querySelector('[data-reliability-retry]');
      const reliabilitySummaryAction = root.querySelector('[data-reliability-summary]');
      const reliabilityFilename = 'Studieteknikk.pdf';
      const reliabilityPatterns = {
        'blocking-document-error': { blocking: true, alert: true },
        'retryable-generation-error': { blocking: false, alert: true },
        'usable-content-notice': { blocking: false, alert: false },
        'demo-info': { blocking: false, alert: false }
      };
      const reliabilityScenarios = {
        unsupported: {
          pattern: 'blocking-document-error', reason: 'unsupported_file_type',
          view: 'startup', summary: false, filename: 'Study notes.docx',
          heading: 'This file is not a PDF',
          body: 'Choose a text-based PDF to create study material.',
          support: 'Choose New session, then select a PDF.'
        },
        damaged: {
          pattern: 'blocking-document-error', reason: 'pdf_open_failed',
          view: 'startup', summary: false,
          heading: 'This PDF could not be opened',
          body: 'The file could not be read. No study material has been created.',
          support: 'Choose New session, then select another PDF.'
        },
        'no-text': {
          pattern: 'blocking-document-error', reason: 'no_usable_extracted_text',
          view: 'startup', summary: false,
          heading: 'No usable text was found',
          body: 'This PDF has no text that the app can use. No study material has been created.',
          support: 'Choose New session, then select a PDF with readable text.'
        },
        'material-loss': {
          pattern: 'blocking-document-error', reason: 'material_extraction_loss',
          view: 'startup', summary: false, retry: 'extracting',
          heading: 'This PDF could not be used',
          body: 'An important part of the PDF could not be read. No study material has been created.',
          support: 'Try again, or choose another PDF through New session.'
        },
        'uncertain-extraction': {
          pattern: 'blocking-document-error', reason: 'extraction_coverage_uncertain',
          view: 'startup', summary: false, retry: 'extracting',
          heading: 'This PDF could not be used',
          body: 'The app could not check whether important text was missed. No study material has been created.',
          support: 'Try again, or choose another PDF through New session.'
        },
        'incidental-omission': {
          pattern: 'usable-content-notice', reason: 'known_nonessential_omission',
          view: 'summary', summary: true, content: true, notice: 'summary'
        },
        'reduced-flashcards': {
          pattern: 'usable-content-notice', reason: 'flashcards_source_filtered_subset',
          view: 'flashcards', summary: true, content: true, cards: true, notice: 'cards'
        },
        'reduced-quiz': {
          pattern: 'usable-content-notice', reason: 'quiz_source_filtered_subset',
          view: 'quiz', summary: true, content: true, quiz: true, notice: 'quiz'
        },
        'zero-flashcards': {
          pattern: 'retryable-generation-error', reason: 'flashcards_source_filter_empty',
          view: 'flashcards', summary: true, quiz: true, answer: 1, retry: 'flashcards',
          body: 'No flashcards could be kept from this attempt.'
        },
        'zero-quiz': {
          pattern: 'retryable-generation-error', reason: 'quiz_source_filter_empty',
          view: 'quiz', summary: true, cards: true, card: 1, retry: 'quiz',
          body: 'No questions could be kept from this attempt.'
        },
        'invalid-flashcards': {
          pattern: 'retryable-generation-error', reason: 'flashcards_schema_invalid',
          view: 'flashcards', summary: true, quiz: true, answer: 1, retry: 'flashcards',
          body: 'The new study material could not be used.'
        },
        'invalid-quiz': {
          pattern: 'retryable-generation-error', reason: 'quiz_schema_invalid',
          view: 'quiz', summary: true, cards: true, card: 1, retry: 'quiz',
          body: 'The new study material could not be used.'
        },
        'invalid-summary': {
          pattern: 'retryable-generation-error', reason: 'summary_source_match_failed',
          view: 'summary', summary: false, retry: 'summary',
          body: 'The new Summary could not be used.'
        },
        'saved-demo': {
          pattern: 'demo-info', reason: 'saved_demo_live_boundary',
          view: 'summary', summary: true, content: true, demo: true, cards: true, quiz: true,
          filename: 'Studieteknikk — demo.pdf'
        },
        'missing-setup': {
          pattern: 'retryable-generation-error', reason: 'live_setup_missing',
          view: 'flashcards', summary: true, quiz: true, answer: 1, setup: true,
          body: 'This version is not set up to create new study material.'
        },
        'service-unavailable': {
          pattern: 'retryable-generation-error', reason: 'generation_service_unavailable',
          view: 'flashcards', summary: true, quiz: true, answer: 1, retry: 'flashcards',
          body: 'The AI service is unavailable.'
        },
        timeout: {
          pattern: 'retryable-generation-error', reason: 'generation_timeout',
          view: 'quiz', summary: true, cards: true, card: 1, retry: 'quiz',
          body: 'The request took too long.'
        }
      };
      const reliabilityOperations = {
        extracting: { label: 'Extracting text', view: 'summary', body: 'Reading the PDF text before preparing your study material.' },
        summary: { label: 'Generating summary', view: 'summary', body: 'Your summary is being prepared from the PDF text.' },
        flashcards: { label: 'Generating flashcards', view: 'flashcards', body: 'Your flashcards are being prepared from the PDF text.' },
        quiz: { label: 'Generating quiz', view: 'quiz', body: 'Your quiz is being prepared from the PDF text.' }
      };
      let reliabilityScenario = 'unsupported';
      let reliabilityPending = null;
      let reliabilityFailedView = 'startup';
      let reliabilityEnded = false;
      const reliabilityBaseRender = render;
      const reliabilityBaseSetView = setView;

      function reliabilityMessage({ pattern, heading, body, support, pending = false, retry = false, summary = false }) {
        reliabilityStatus.dataset.reliabilityPattern = pattern;
        reliabilityHeading.textContent = heading;
        root.querySelector('[data-status-body]').textContent = body;
        root.querySelector('[data-status-support]').textContent = support;
        root.querySelector('[data-status-pending]').hidden = !pending;
        root.querySelector('[data-status-error]').hidden = pending;
        root.querySelector('[data-status-announcement]').textContent = pending ? heading : '';
        root.querySelector('[data-status-recovery]').hidden = !(retry || summary);
        reliabilityRetry.hidden = !retry;
        reliabilitySummaryAction.hidden = !summary;
        reliabilityStatus.setAttribute('aria-busy', String(pending));
        if (reliabilityPatterns[pattern]?.alert) reliabilityStatus.setAttribute('role', 'alert');
        else reliabilityStatus.removeAttribute('role');
      }

      function loadReliabilityScenario(id) {
        if (reliabilityEnded || !reliabilityScenarios[id]) return;
        const scenario = reliabilityScenarios[id];
        reliabilityScenario = id;
        reliabilityPending = null;
        reliabilityFailedView = scenario.view;
        // Only this external review selector loads a fresh fixture. Product
        // navigation and retry never reset these saved contents or practice values.
        state.active = true;
        state.view = scenario.view;
        state.language = 'en';
        state.level = 'detailed';
        state.file = { name: scenario.filename || reliabilityFilename, pdf: id !== 'unsupported', example: true };
        state.selectedName = state.file.name;
        state.ready = { summary: scenario.summary, flashcards: Boolean(scenario.cards), quiz: Boolean(scenario.quiz) };
        state.card = scenario.card ?? 0;
        state.flipped = false;
        state.answer = scenario.answer ?? null;
        state.confirmed = false;
        state.source = null;
        sourceReturn = null;
        summaryKey = '';
        lastStudyView = scenario.view === 'startup' ? 'summary' : scenario.view;
        languageInput.value = state.language;
        levelInput.value = state.level;
        acknowledgement.checked = true;
      }

      render = () => {
        reliabilityBaseRender();
        reliabilityStatus.hidden = true;
        root.querySelectorAll('[data-reliability-notice]').forEach(notice => notice.hidden = true);
        delete app.dataset.reliabilityNeutral;
        if (!state.active) reliabilityEnded = true;
        reliabilitySelect.disabled = reliabilityEnded;
        if (reliabilityEnded) {
          reliabilityHelp.textContent = 'This synthetic example session has ended. Home is empty. Reload this review to inspect another fixture; the ended material cannot be restored by navigation.';
          return;
        }
        reliabilityHelp.textContent = reliabilityInitialHelp;
        const scenario = reliabilityScenarios[reliabilityScenario];
        const pattern = reliabilityPatterns[scenario.pattern];
        root.querySelector('.doc-name').textContent = state.file.name;
        root.querySelector('.session-meta').textContent = 'English · Detailed · fixed for this session';
        root.querySelector('.sample-note').textContent = scenario.demo
          ? 'Demo session · saved study material · no PDF processing'
          : 'Saved example · no PDF processing';
        root.querySelector('.source-file').firstChild.textContent = `${state.file.name} · physical page `;
        root.querySelector('.source-note').textContent = 'Example source text. Finding a passage does not confirm that it supports the answer.';
        if (!state.ready.summary) {
          root.querySelector('#preview-summary-copy').replaceChildren();
          summaryKey = '';
        }
        if (scenario.notice) root.querySelector(`[data-reliability-${scenario.notice}-notice]`).hidden = false;
        if (scenario.notice === 'cards') root.querySelector('[data-card-count]').textContent = `Card ${state.card + 1} of 3`;
        if (scenario.notice === 'quiz') {
          root.querySelector('[data-ready="quiz"] > .item-count').textContent = 'Question 1 of 1';
          root.querySelector('[data-quiz-restart]').textContent = 'Restart the same quiz';
        }
        if (scenario.demo) root.querySelector('[data-reliability-demo-notice]').hidden = state.view === 'startup';

        const operation = reliabilityPending ? reliabilityOperations[reliabilityPending] : null;
        const pendingHere = operation && state.view === operation.view;
        const noSummaryError = !state.ready.summary && !operation;
        const errorHere = !scenario.content && !operation && (noSummaryError || pattern.blocking || state.view === reliabilityFailedView);
        if (pendingHere || errorHere) {
          reliabilityStatus.hidden = false;
          root.querySelectorAll('[data-panel]').forEach(panel => panel.hidden = true);
          if (noSummaryError) {
            app.dataset.reliabilityNeutral = 'true';
            activeHomeCard.hidden = true;
            root.querySelector('.doc-context').hidden = false;
          }
          if (pendingHere) {
            reliabilityMessage({
              pattern: 'pending', heading: operation.label, body: operation.body,
              support: state.ready.summary ? 'Your existing study material and progress are still available.' : 'Keep this session open while processing continues.',
              pending: true, summary: state.ready.summary && state.view !== 'summary'
            });
          } else {
            const generationError = scenario.pattern === 'retryable-generation-error';
            reliabilityMessage({
              pattern: scenario.pattern,
              heading: generationError ? `${learningNames[reliabilityFailedView]} could not be created` : scenario.heading,
              body: scenario.body,
              support: state.ready.summary
                ? `${scenario.retry ? 'Try again when you are ready. ' : ''}Your existing study material and progress are still available.`
                : scenario.support || 'Try again, or choose another PDF through New session.',
              retry: Boolean(scenario.retry), summary: state.ready.summary
            });
          }
        }
        root.querySelectorAll('[data-preview]').forEach(button => {
          button.disabled = !state.ready.summary && button.dataset.preview !== 'startup' && (!operation || button.dataset.preview !== operation.view);
        });
        root.querySelectorAll('[data-generate]').forEach(button => button.disabled = Boolean(operation));
        reliabilityRetry.disabled = Boolean(operation);
        if (state.view === 'startup' && !noSummaryError) {
          startupHeading.textContent = operation && !state.ready.summary ? 'Your study session is in progress' : 'Continue your study session';
          startupDescription.textContent = operation
            ? `${operation.label}. ${state.ready.summary ? 'Your existing study material and progress are available.' : 'Continue to see the current status.'}`
            : 'Your available study material and progress are ready when you are.';
          root.querySelector('.active-session-example').textContent = scenario.demo ? 'Demo session · saved study material' : 'Saved example · no PDF processing';
          if (scenario.demo) startupDescription.textContent = 'Saved study material is ready. Your own PDFs and fresh generation require the live version.';
        }
      };

      setView = (view, direct = false) => {
        if (!reliabilityEnded && state.active) {
          const operation = reliabilityPending ? reliabilityOperations[reliabilityPending] : null;
          if (!state.ready.summary && view !== 'startup' && (!operation || view !== operation.view)) return;
          // Opening a tab never publishes a failed or ungenerated response.
          reliabilityBaseSetView(view, false);
          return;
        }
        reliabilityBaseSetView(view, direct);
      };

      function beginReliabilityRetry(operation) {
        if (reliabilityPending || reliabilityEnded || !reliabilityOperations[operation]) return;
        reliabilityPending = operation;
        const target = reliabilityOperations[operation].view;
        // A new attempt has no accepted result yet. Preserve every existing ready
        // flag, Summary, card position and Quiz answer until acceptance can occur.
        state.view = target;
        state.source = null;
        sourceReturn = null;
        lastStudyView = target;
        render();
        reliabilityHeading.setAttribute('tabindex', '-1');
        reliabilityHeading.focus({ preventScroll: true });
      }

      root.addEventListener('click', event => {
        const widthButton = event.target.closest('button[data-reliability-width]');
        if (widthButton && root.contains(widthButton)) {
          root.dataset.reliabilityWidth = widthButton.dataset.reliabilityWidth;
          root.querySelectorAll('[data-reliability-width]').forEach(button => button.setAttribute('aria-pressed', String(button === widthButton)));
          return;
        }
        if (!state.active || reliabilityEnded) return;
        const button = event.target.closest('button');
        if (!button || button.disabled || !root.contains(button)) return;
        if (button.hasAttribute('data-reliability-retry') || button.hasAttribute('data-generate')) {
          event.preventDefault();
          event.stopImmediatePropagation();
          if (reliabilityScenarios[reliabilityScenario].setup) {
            reliabilityFailedView = button.dataset.generate || reliabilityFailedView;
            state.view = reliabilityFailedView;
            lastStudyView = state.view;
            render();
            reliabilityHeading.setAttribute('tabindex', '-1');
            reliabilityHeading.focus({ preventScroll: true });
            return;
          }
          const operation = button.hasAttribute('data-reliability-retry') ? reliabilityScenarios[reliabilityScenario].retry : button.dataset.generate;
          beginReliabilityRetry(operation);
        } else if (button.hasAttribute('data-reliability-summary')) {
          event.preventDefault();
          event.stopImmediatePropagation();
          setView('summary');
          root.querySelector('[data-preview="summary"]').focus({ preventScroll: true });
        }
      }, true);

      reliabilitySelect.addEventListener('change', () => {
        if (reliabilityEnded || sessionDialogOpen) return;
        loadReliabilityScenario(reliabilitySelect.value);
        render();
      });
      loadReliabilityScenario(reliabilityScenario);
