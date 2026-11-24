      const sessionToggle = root.querySelector('[data-session-toggle]');
      const sessionPopup = root.querySelector('[data-session-popup]');
      const sessionOverlay = root.querySelector('[data-session-overlay]');
      const sessionDialog = root.querySelector('[data-session-dialog]');
      const sessionCancel = root.querySelector('[data-session-cancel]');
      const sessionConfirm = root.querySelector('[data-session-confirm]');
      let sessionAction = null;
      let sessionReturn = null;
      let inertSnapshot = [];

      function closeSessionPopup(returnFocus = false) {
        if (!sessionPopup) return;
        sessionPopup.hidden = true;
        sessionToggle.setAttribute('aria-expanded', 'false');
        if (returnFocus) sessionToggle.focus({ preventScroll: true });
      }
      function guardSessionFocus(event) {
        if (sessionAction && !sessionDialog.contains(event.target)) sessionCancel.focus({ preventScroll: true });
      }
      function guardSessionPointer(event) {
        if (sessionAction && !sessionDialog.contains(event.target)) {
          event.preventDefault(); event.stopImmediatePropagation();
        }
      }
      function guardSessionKeys(event) {
        if (!sessionAction) return;
        if (event.key === 'Escape') { event.preventDefault(); event.stopImmediatePropagation(); closeSessionDialog(true); return; }
        if (event.key === 'Tab') {
          const first = sessionCancel, last = sessionConfirm;
          if (event.shiftKey && (document.activeElement === first || !sessionDialog.contains(document.activeElement))) { event.preventDefault(); last.focus(); }
          else if (!event.shiftKey && (document.activeElement === last || !sessionDialog.contains(document.activeElement))) { event.preventDefault(); first.focus(); }
        }
      }
      function openSessionDialog(action, trigger) {
        if (!state.active || sessionAction) return;
        sessionReturn = sessionToggle || trigger;
        sessionAction = action;
        closeSessionPopup();
        root.querySelector('#session-dialog-title').textContent = action === 'new' ? 'Start a new session?' : 'Clear this session?';
        root.querySelector('#session-dialog-next').textContent = action === 'new'
          ? 'You will return to Home to choose a PDF, study material language and Summary detail again.'
          : 'You will return to an empty Home screen.';
        sessionConfirm.textContent = action === 'new' ? 'Start new session' : 'Clear session';
        const otherConcepts = [...document.querySelectorAll('[data-concept]')].filter(element => element !== root);
        inertSnapshot = [...root.querySelectorAll('.app-brandbar, .app-main, .source-panel'), ...otherConcepts].map(element => [element, element.inert]);
        inertSnapshot.forEach(([element]) => element.inert = true);
        sessionOverlay.hidden = false;
        const area = app.getBoundingClientRect(), source = sessionReturn.getBoundingClientRect(), height = sessionDialog.getBoundingClientRect().height;
        const top = Math.max(16, Math.min(source.bottom - area.top + 18, area.height - height - 20));
        app.style.setProperty('--session-dialog-offset', `${top}px`);
        document.addEventListener('keydown', guardSessionKeys, true);
        document.addEventListener('focusin', guardSessionFocus, true);
        document.addEventListener('pointerdown', guardSessionPointer, true);
        sessionCancel.focus({ preventScroll: true });
      }
      function closeSessionDialog(restoreFocus) {
        const trigger = sessionReturn;
        sessionAction = null;
        sessionOverlay.hidden = true;
        inertSnapshot.forEach(([element, previous]) => element.inert = previous);
        inertSnapshot = [];
        document.removeEventListener('keydown', guardSessionKeys, true);
        document.removeEventListener('focusin', guardSessionFocus, true);
        document.removeEventListener('pointerdown', guardSessionPointer, true);
        sessionReturn = null;
        if (restoreFocus && trigger) trigger.focus({ preventScroll: true });
      }
      function confirmSessionEnd() {
        if (!sessionAction) return;
        closeSessionDialog(false);
        state.active = false;
        state.file = null;
        state.selectedName = '';
        state.language = 'nb';
        state.level = 'brief';
        state.card = 0;
        state.flipped = false;
        state.answer = null;
        state.confirmed = false;
        state.source = null;
        state.ready = { summary: false, flashcards: false, quiz: false };
        state.view = 'startup';
        sourceReturn = null;
        summaryKey = '';
        form.reset();
        fileInput.value = '';
        languageInput.value = '';
        levelInput.value = '';
        acknowledgement.checked = false;
        render();
        root.querySelector('[data-choose-pdf]').focus({ preventScroll: true });
      }
      const sessionBaseRender = render;
      const sessionBaseSetView = setView;
      readyToStart = () => !state.active && Boolean(state.file?.pdf && languageInput.value && levelInput.value && acknowledgement.checked);
      renderForm = () => {
        root.querySelector('#generate-summary').disabled = !readyToStart();
        fileInput.disabled = state.active;
        languageInput.disabled = state.active;
        levelInput.disabled = state.active;
        acknowledgement.disabled = state.active;
        root.querySelector('[data-choose-pdf]').disabled = state.active;
        root.querySelector('#selected-file').hidden = !state.file;
        root.querySelector('#selected-file').textContent = state.file ? (state.file.pdf ? `${state.file.example ? 'Example document' : 'Selected'}: ${state.file.name}` : `Choose a PDF file instead of “${state.file.name}”.`) : 'No file selected.';
        root.querySelector('#startup-status').textContent = state.active
          ? 'Session settings are locked. Open a learning tab and choose New session to change them.'
          : readyToStart() ? 'Ready to preview. Your PDF will not be processed.' : 'Complete the options to preview saved example content.';
      };
      render = () => {
        sessionBaseRender();
        if (state.source) closeSessionPopup();
        root.querySelectorAll('[data-preview]').forEach(button => button.disabled = button.dataset.preview !== 'startup' && !state.active);
        root.querySelector('[data-session-tools]').hidden = !state.active;
        root.querySelector('.sample-note').textContent = 'Saved example content · no PDF processing or AI calls.';
        if (!state.active) {
          root.querySelector('#preview-summary-copy').replaceChildren();
          summaryKey = '';
          root.querySelector('.card-prompt').textContent = '';
          root.querySelector('.card-answer').textContent = '';
          root.querySelector('[data-card-count]').textContent = '';
          root.querySelector('[data-quiz-question]').textContent = '';
          root.querySelectorAll('[data-quiz-option]').forEach(option => option.textContent = '');
          root.querySelector('[data-feedback]').replaceChildren();
          root.querySelector('[data-excerpt]').textContent = '';
        }
      };
      setView = (view) => {
        if (!state.active && view !== 'startup') return;
        closeSessionPopup();
        sessionBaseSetView(view, false);
      };
      savePresentation = () => {};
      languageInput.value = 'nb';
      levelInput.value = 'brief';
      acknowledgement.checked = true;
      root.addEventListener('click', event => {
        const button = event.target.closest('button');
        if (!button || button.disabled || !root.contains(button)) return;
        if (button.hasAttribute('data-session-toggle')) {
          const open = sessionPopup.hidden;
          sessionPopup.hidden = !open;
          sessionToggle.setAttribute('aria-expanded', String(open));
        } else if (button.dataset.sessionAction) openSessionDialog(button.dataset.sessionAction, button);
        else if (button.hasAttribute('data-session-cancel')) closeSessionDialog(true);
        else if (button.hasAttribute('data-session-confirm')) confirmSessionEnd();
      });
      document.addEventListener('pointerdown', event => {
        if (sessionPopup && !sessionPopup.hidden && !event.target.closest('.session-tools')) closeSessionPopup();
      });
      root.addEventListener('keydown', event => {
        if (event.key === 'Escape' && sessionPopup && !sessionPopup.hidden && !sessionAction) {
          event.preventDefault(); closeSessionPopup(true);
        }
      });
      fileInput.addEventListener('change', event => {
        if (state.active) { event.stopImmediatePropagation(); return; }
      }, true);
