      // Isolated presentation fixtures. No PDF read, API call, persistence or timer.
      let statusConcept = null;
      const statusRegion = root.querySelector('[data-status-view]');
      const statusHeading = root.querySelector('[data-status-heading]');
      const statusBody = root.querySelector('[data-status-body]');
      const statusPending = root.querySelector('[data-status-pending]');
      const statusError = root.querySelector('[data-status-error]');
      const statusSupport = root.querySelector('[data-status-support]');
      const statusRecovery = root.querySelector('[data-status-recovery]');
      const statusOperations = {
        checking: { label: 'Checking PDF', view: 'summary', body: 'Checking whether this PDF can be used for your study session.' },
        extracting: { label: 'Extracting text', view: 'summary', body: 'Reading the PDF text before preparing your study material.' },
        summary: { label: 'Generating summary', view: 'summary', body: 'Your summary is being prepared from the PDF text.' },
        flashcards: { label: 'Generating flashcards', view: 'flashcards', body: 'Your flashcards are being prepared from the PDF text.' },
        quiz: { label: 'Generating quiz', view: 'quiz', body: 'Your quiz is being prepared from the PDF text.' }
      };
      let statusOperation = 'summary';
      let retryOperation = null;
      let statusFixtureEnded = false;
      const statusBaseRender = render;
      const statusBaseSetView = setView;

      function showStatusMessage(heading, body, support, pending, retry) {
        statusHeading.textContent = heading;
        statusBody.textContent = body;
        statusSupport.textContent = support;
        statusPending.hidden = !pending;
        statusError.hidden = pending;
        statusRecovery.hidden = !retry;
        root.querySelector('[data-status-announcement]').textContent = pending ? heading : '';
        statusRegion.setAttribute('aria-busy', String(pending));
        if (pending) statusRegion.removeAttribute('role');
        else statusRegion.setAttribute('role', 'alert');
      }

      render = () => {
        statusBaseRender();
        if (exampleEnded && !state.active) {
          statusFixtureEnded = true;
          root.dispatchEvent(new Event('study-preview:ended'));
        }
        const fixtureActive = statusConcept !== null && state.active && !statusFixtureEnded;
        statusRegion.hidden = true;
        delete app.dataset.status;
        if (!fixtureActive) return;
        app.dataset.status = statusConcept;
        root.querySelector('.doc-name').textContent = state.file.name;
        root.querySelector('.session-meta').textContent = `${state.language === 'en' ? 'English' : 'Norwegian Bokmål'} · ${state.level === 'brief' ? 'Brief' : 'Detailed'} · fixed for this session`;
        root.querySelector('.sample-note').textContent = 'Synthetic state sketch · no PDF processing or AI calls.';
        if (!state.ready.summary) {
          // Never expose a new Summary before its complete response is accepted.
          root.querySelector('#preview-summary-copy').replaceChildren();
          summaryKey = '';
        }

        if (statusConcept === 'loading') {
          const operation = statusOperations[statusOperation];
          const visible = state.view === operation.view;
          statusRegion.hidden = !visible;
          if (visible) root.querySelectorAll('[data-panel]').forEach(panel => panel.hidden = true);
          showStatusMessage(operation.label, operation.body, 'Keep this session open while processing continues.', true, false);
          root.querySelectorAll('[data-preview]').forEach(button => {
            button.disabled = button.dataset.preview !== 'startup' && button.dataset.preview !== operation.view;
          });
          if (state.view === 'startup') {
            startupHeading.textContent = 'Your study session is in progress';
            startupDescription.textContent = `${operation.label}. Continue to see the current status.`;
            root.querySelector('.active-session-example').textContent = 'Synthetic state sketch · processing in progress';
          }
        } else if (statusConcept === 'pdf-problem') {
          statusRegion.hidden = false;
          root.querySelectorAll('[data-panel]').forEach(panel => panel.hidden = true);
          activeHomeCard.hidden = true;
          root.querySelector('.doc-context').hidden = false;
          root.querySelectorAll('[data-preview]').forEach(button => button.disabled = button.dataset.preview !== 'startup');
          showStatusMessage(
            'This PDF needs a password',
            'We cannot read a password-protected PDF. No study material has been created.',
            'Choose New session to return to Home, then select a PDF that does not need a password.',
            false, false
          );
        } else if (statusConcept === 'ai-error') {
          const pendingHere = retryOperation === state.view;
          const visible = state.view === 'flashcards' || pendingHere;
          statusRegion.hidden = !visible;
          if (visible) root.querySelectorAll('[data-panel]').forEach(panel => panel.hidden = true);
          if (pendingHere) {
            const operation = statusOperations[retryOperation];
            showStatusMessage(operation.label, operation.body, 'Your existing study material and progress are kept. You can open other ready tabs while you wait.', true, false);
          } else {
            showStatusMessage(
              'Flashcards could not be created',
              'We could not create a usable set. Please try again.',
              'Your existing study material and progress are kept. You can open another ready tab or try again.',
              false, true
            );
          }
          root.querySelectorAll('[data-generate]').forEach(button => button.disabled = retryOperation !== null);
          root.querySelector('[data-retry]').disabled = retryOperation !== null;
          if (state.view === 'startup') {
            startupDescription.textContent = 'Your existing study material and progress are kept. Flashcards could not be created.';
            root.querySelector('.active-session-example').textContent = 'Synthetic state sketch · saved example Summary';
          }
        }
      };

      setView = (view, direct = false) => {
        if (statusConcept === null) { statusBaseSetView(view, direct); return; }
        if (state.active && !statusFixtureEnded) {
          if (statusConcept === 'pdf-problem' && view !== 'startup') return;
          if (statusConcept === 'loading' && view !== 'startup' && view !== statusOperations[statusOperation].view) return;
          // Never mark an ungenerated function ready just by opening its tab.
          statusBaseSetView(view, false);
          return;
        }
        statusBaseSetView(view, direct);
      };

      root.addEventListener('click', event => {
        if (statusConcept === null || !state.active || statusFixtureEnded) return;
        const button = event.target.closest('button');
        if (!button || button.disabled || !root.contains(button)) return;
        if (button.hasAttribute('data-retry') || button.hasAttribute('data-generate')) {
          event.preventDefault();
          event.stopImmediatePropagation();
          if (statusConcept !== 'ai-error' || retryOperation !== null) return;
          retryOperation = button.hasAttribute('data-retry') ? 'flashcards' : button.dataset.generate;
          // A rejected replacement or manual retry never removes accepted content.
          state.view = retryOperation;
          state.source = null;
          render();
          statusHeading.setAttribute('tabindex', '-1');
          statusHeading.focus({ preventScroll: true });
        }
      }, true);

      // Review-only event. The normal main preview keeps its saved-example flow.
      root.addEventListener('study-preview:status', event => {
        const kind = event.detail?.kind;
        if (!['loading', 'pdf-problem', 'ai-error'].includes(kind) || exampleEnded) return;
        const preserveSession = state.active && kind === 'ai-error' && !event.detail?.replaceFixture;
        if (!state.active) statusBaseSetView('summary', true);
        statusConcept = kind;
        statusFixtureEnded = false;
        statusOperation = statusOperations[event.detail?.operation] ? event.detail.operation : 'summary';
        retryOperation = null;
        if (!preserveSession) {
        state.file = { name: kind === 'pdf-problem' ? 'Forelesningsnotater.pdf' : 'Studieteknikk.pdf', pdf: true, example: true };
        state.selectedName = state.file.name;
        state.ready = { summary: kind === 'ai-error', flashcards: false, quiz: false };
        state.card = 0; state.flipped = false; state.answer = null; state.confirmed = false;
        }
        state.view = kind === 'pdf-problem' ? 'startup' : kind === 'ai-error' ? 'flashcards' : statusOperations[statusOperation].view;
        state.source = null;
        sourceReturn = null;
        summaryKey = '';
        lastStudyView = state.view === 'startup' ? 'summary' : state.view;
        render();
      });
