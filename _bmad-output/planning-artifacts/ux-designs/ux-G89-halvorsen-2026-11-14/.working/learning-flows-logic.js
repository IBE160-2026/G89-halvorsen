      function resetQuizAttempt() {
        state.quizIndex = 0;
        state.quizDrafts = learningQuestions.map(() => null);
        state.quizAnswers = learningQuestions.map(() => null);
        state.quizComplete = false;
        state.quizResult = false;
      }
      function resetLearningFlows() {
        resetQuizAttempt();
        state.cardComplete = false;
      }
      function quizConfirmed(index = state.quizIndex) { return state.quizAnswers[index] !== null; }
      function allQuizConfirmed() { return state.quizAnswers.every(answer => answer !== null); }
      function renderCards() {
        const cards = content[state.language].cards, card = cards[state.card];
        root.querySelector('[data-card-count]').textContent = state.cardComplete ? `${cards.length} cards · sample set` : `Card ${state.card + 1} of ${cards.length} · sample set`;
        root.querySelector('[data-card-practice]').hidden = state.cardComplete;
        root.querySelector('[data-card-complete]').hidden = !state.cardComplete;
        root.querySelector('.card-prompt').textContent = card[0]; root.querySelector('.card-prompt').hidden = state.flipped;
        root.querySelector('.card-answer').textContent = card[1]; root.querySelector('.card-answer').hidden = !state.flipped;
        root.querySelector('.card-prompt').lang = state.language; root.querySelector('.card-answer').lang = state.language;
        root.querySelector('.flip-hint').textContent = state.flipped ? 'Show question' : 'Show answer';
        root.querySelector('[data-flip]').setAttribute('aria-pressed', String(state.flipped));
        root.querySelector('[data-flip]').setAttribute('aria-label', state.flipped ? 'Show card question' : 'Show card answer');
        root.querySelector('[data-flip]').setAttribute('aria-describedby', state.flipped ? 'preview-card-answer' : 'preview-card-prompt');
        const cardSource = root.querySelector('[data-source="card"]'), references = learningCardSources[state.card];
        cardSource.hidden = !state.flipped;
        cardSource.textContent = references.length > 1 ? `View sources · ${references.length} passages` : `View source · page ${learningSources[references[0]].page}`;
        root.querySelector('[data-card-step="-1"]').disabled = state.card === 0;
        root.querySelector('[data-card-step="1"]').hidden = state.card === cards.length - 1;
        root.querySelector('[data-card-finish]').hidden = state.card !== cards.length - 1;
      }
      function renderQuiz() {
        const question = learningQuestions[state.quizIndex], text = question[state.language];
        const confirmed = quizConfirmed(), answer = confirmed ? state.quizAnswers[state.quizIndex] : state.quizDrafts[state.quizIndex];
        const confirmedCount = state.quizAnswers.filter(value => value !== null).length;
        root.querySelector('[data-quiz-practice]').hidden = state.quizResult;
        root.querySelector('[data-quiz-result]').hidden = !state.quizResult;
        root.querySelector('[data-quiz-count]').textContent = `Question ${state.quizIndex + 1} of ${learningQuestions.length} · ${confirmedCount} confirmed${state.quizComplete ? ' · review' : ''}`;
        root.querySelector('[data-quiz-question]').textContent = text.question;
        root.querySelector('.quiz-options').lang = state.language;
        root.querySelectorAll('[data-quiz-option]').forEach(option => option.textContent = text.options[Number(option.dataset.quizOption)]);
        root.querySelectorAll('input[name="preview-quiz-answer"]').forEach(input => {
          const index = Number(input.value), label = input.closest('label');
          input.checked = index === answer; input.disabled = confirmed;
          label.removeAttribute('data-answer-state');
          let status = '';
          if (confirmed && index === question.correct) { label.dataset.answerState = 'correct'; status = index === answer ? 'Your answer · correct answer' : 'Correct answer'; }
          else if (confirmed && index === answer) { label.dataset.answerState = 'incorrect'; status = 'Your answer · incorrect'; }
          root.querySelector(`[data-option-state="${index}"]`).textContent = status;
        });
        root.querySelector('[data-confirm]').disabled = answer === null || confirmed;
        root.querySelector('[data-confirm]').hidden = confirmed;
        root.querySelector('#quiz-answer-help').textContent = confirmed ? 'Answer confirmed and locked for this attempt.' : 'Select one answer, then confirm to see feedback.';
        const feedback = root.querySelector('[data-feedback]'); feedback.hidden = !confirmed; feedback.lang = 'en'; feedback.replaceChildren();
        if (confirmed) {
          appendText(feedback, 'strong', answer === question.correct ? 'Correct.' : 'Incorrect.');
          const correctLine = appendText(feedback, 'p', 'Correct answer: '), correctText = appendText(correctLine, 'span', text.options[question.correct]); correctText.lang = state.language;
          const explanation = appendText(feedback, 'p', text.explanation); explanation.lang = state.language;
        }
        const sourceButton = root.querySelector('[data-source="quiz"]'); sourceButton.hidden = !confirmed;
        sourceButton.textContent = question.sources.length > 1 ? `View sources · ${question.sources.length} passages` : `View source · page ${learningSources[question.sources[0]].page}`;
        root.querySelector('[data-quiz-step="-1"]').disabled = state.quizIndex === 0;
        root.querySelector('[data-quiz-step="1"]').hidden = state.quizIndex === learningQuestions.length - 1;
        root.querySelector('[data-quiz-step="1"]').disabled = !confirmed;
        root.querySelector('[data-quiz-finish]').hidden = state.quizComplete || state.quizIndex !== learningQuestions.length - 1;
        root.querySelector('[data-quiz-finish]').disabled = !allQuizConfirmed();
        root.querySelector('[data-quiz-results]').hidden = !state.quizComplete;
        const correctCount = state.quizAnswers.reduce((count, value, index) => count + (value === learningQuestions[index].correct ? 1 : 0), 0);
        root.querySelector('[data-quiz-score]').textContent = state.quizComplete ? `${correctCount}/${learningQuestions.length} correct (${100 * correctCount / learningQuestions.length}%)` : '';
        const wrongList = root.querySelector('[data-quiz-wrong-list]'); wrongList.replaceChildren();
        if (state.quizComplete) state.quizAnswers.forEach((value, index) => {
          if (value === learningQuestions[index].correct) return;
          const item = document.createElement('li'); item.value = index + 1;
          const button = appendText(item, 'button', learningQuestions[index][state.language].question); button.type = 'button'; button.className = 'quiz-review-link cursor-interaction'; button.dataset.quizReview = String(index); button.lang = state.language;
          wrongList.appendChild(item);
        });
        root.querySelector('[data-quiz-no-wrong]').hidden = !state.quizComplete || wrongList.children.length !== 0;
      }
      function sourceReferences() {
        if (state.source === 'card') return learningCardSources[state.card];
        if (state.source === 'quiz') return learningQuestions[state.quizIndex].sources;
        if (state.source === 'summary-repetition') return [2, 3, 5, 6];
        return [0, 1, 4];
      }
      function renderLearningSources() {
        const open = state.source !== null, panel = root.querySelector('.source-panel');
        panel.hidden = !open;
        root.querySelectorAll('[data-source]').forEach(button => button.setAttribute('aria-expanded', String(open && button.dataset.source === state.source)));
        root.querySelectorAll('.app-brandbar, .app-main').forEach(element => element.inert = open);
        const list = root.querySelector('[data-source-reference-list]'); list.replaceChildren();
        if (!open) return;
        sourceReferences().forEach((sourceIndex, index) => {
          const source = learningSources[sourceIndex], section = document.createElement('section'); section.className = 'source-reference';
          appendText(section, 'h3', `Reference ${index + 1} of ${sourceReferences().length}`);
          const file = appendText(section, 'p', `${learningSourceFilename} · physical page ${source.page}`); file.className = 'source-file';
          const quote = document.createElement('blockquote'), mark = appendText(quote, 'mark', source.text); mark.lang = 'nb'; section.appendChild(quote); list.appendChild(section);
        });
      }
      function positionLearningSource() {
        const panel = root.querySelector('.source-panel'), appTop = app.getBoundingClientRect().top;
        const visibleTop = Math.max(16, appTop);
        app.style.setProperty('--source-offset', `${Math.max(0, visibleTop - appTop)}px`);
        panel.style.maxHeight = `${Math.max(220, window.innerHeight - visibleTop - 16)}px`;
        panel.scrollTop = 0;
      }
      function focusQuizQuestion() { root.querySelector('[data-quiz-question]').focus({ preventScroll: true }); }
      function stepQuiz(amount) {
        if (amount > 0 && !quizConfirmed()) return;
        state.quizIndex = Math.max(0, Math.min(learningQuestions.length - 1, state.quizIndex + amount)); state.source = null; render(); focusQuizQuestion();
      }
      function confirmQuizAnswer() {
        if (quizConfirmed() || state.quizDrafts[state.quizIndex] === null) return;
        state.quizAnswers[state.quizIndex] = state.quizDrafts[state.quizIndex];
      }
      function chooseQuizAnswer(value) {
        if (quizConfirmed() || !Number.isInteger(value) || value < 0 || value > 3) return;
        state.quizDrafts[state.quizIndex] = value; render();
      }
      resetLearningFlows();
