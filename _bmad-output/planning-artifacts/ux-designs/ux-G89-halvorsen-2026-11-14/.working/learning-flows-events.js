      root.addEventListener('click', event => {
        const button = event.target.closest('button'); if (!button || !root.contains(button) || button.disabled) return;
        if (button.hasAttribute('data-use-learning-sample')) {
          if (state.active) return;
          state.file = { name: learningSourceFilename, pdf: true, example: true }; fileInput.value = ''; acknowledgement.checked = false; renderForm(); return;
        }
        if (button.hasAttribute('data-choose-pdf')) { fileInput.click(); return; }
        if (button.hasAttribute('data-start')) { startExample(); return; }
        if (button.dataset.preview) { setView(button.dataset.preview, true); savePresentation(); return; }
        if (button.dataset.view) { setView(button.dataset.view); return; }
        if (button.dataset.generate) { state.ready[button.dataset.generate] = true; render(); return; }
        if (button.hasAttribute('data-flip')) { state.flipped = !state.flipped; state.source = null; }
        else if (button.hasAttribute('data-card-step')) { state.card = Math.max(0, Math.min(content[state.language].cards.length - 1, state.card + Number(button.dataset.cardStep))); state.flipped = false; state.cardComplete = false; state.source = null; }
        else if (button.hasAttribute('data-card-finish')) { state.cardComplete = true; state.flipped = false; state.source = null; render(); root.querySelector('#card-end-title').focus({ preventScroll: true }); return; }
        else if (button.hasAttribute('data-card-return')) { state.cardComplete = false; state.flipped = false; }
        else if (button.hasAttribute('data-card-restart')) { state.card = 0; state.flipped = false; state.cardComplete = false; state.source = null; }
        else if (button.dataset.source) {
          sourceReturn = { trigger: button, x: window.scrollX, y: window.scrollY };
          state.source = button.dataset.source; render(); positionLearningSource();
          root.querySelector('[data-close-source]').focus({ preventScroll: true }); return;
        }
        else if (button.hasAttribute('data-close-source')) { closeSource(true); return; }
        else if (button.hasAttribute('data-confirm')) { confirmQuizAnswer(); render(); root.querySelector('[data-feedback]').focus({ preventScroll: true }); return; }
        else if (button.hasAttribute('data-quiz-step')) { stepQuiz(Number(button.dataset.quizStep)); return; }
        else if (button.hasAttribute('data-quiz-finish')) { if (!allQuizConfirmed()) return; state.quizComplete = true; state.quizResult = true; render(); root.querySelector('#quiz-result-title').focus({ preventScroll: true }); return; }
        else if (button.hasAttribute('data-quiz-review')) { if (!state.quizComplete) return; state.quizIndex = Number(button.dataset.quizReview); state.quizResult = false; render(); focusQuizQuestion(); return; }
        else if (button.hasAttribute('data-quiz-results')) { state.quizResult = true; render(); root.querySelector('#quiz-result-title').focus({ preventScroll: true }); return; }
        else if (button.hasAttribute('data-quiz-restart')) { resetQuizAttempt(); state.source = null; render(); focusQuizQuestion(); return; }
        else return;
        render();
      });
      root.addEventListener('change', event => { if (event.target.matches('input[name="preview-quiz-answer"]')) chooseQuizAnswer(Number(event.target.value)); });
      root.addEventListener('keydown', event => {
        if (!state.source) return;
        if (event.key === 'Escape') { event.preventDefault(); closeSource(true); }
        else if (event.key === 'Tab') { event.preventDefault(); root.querySelector('[data-close-source]').focus({ preventScroll: true }); }
      });
