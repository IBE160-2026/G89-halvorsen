      // Independent, prewritten fixture. No PDF content or real study session is restored.
      const activeHomeCard = root.querySelector('[data-active-home]');
      const startupHeading = root.querySelector('#startup-title');
      const startupDescription = root.querySelector('.startup-intro p');
      const emptyHomeHeading = startupHeading.textContent;
      const emptyHomeDescription = [...startupDescription.childNodes].map(node => node.cloneNode(true));
      const activeHomeBaseRender = render;
      const activeHomeBaseSetView = setView;
      const learningNames = { summary: 'Summary', flashcards: 'Flashcards', quiz: 'Quiz' };
      let lastStudyView = 'summary';
      // Keep this concept isolated from presentation state belonging to the chosen concept.
      savePresentation = () => {};
      render = () => {
        activeHomeBaseRender();
        const activeHome = state.active && state.view === 'startup';
        form.hidden = state.active;
        activeHomeCard.hidden = !activeHome;
        if (activeHome) {
          startupHeading.textContent = 'Continue your study session';
          startupDescription.textContent = 'Your study material is ready when you are.';
          root.querySelector('[data-home-document]').textContent = state.file?.name || state.selectedName;
          root.querySelector('[data-home-language]').textContent = state.language === 'en' ? 'English' : 'Norwegian Bokmål';
          root.querySelector('[data-home-level]').textContent = state.level === 'brief' ? 'Brief' : 'Detailed';
          root.querySelector('[data-home-destination]').textContent = `Return to ${learningNames[lastStudyView]}`;
          root.querySelector('.active-session-example').textContent = 'Saved example content · no PDF processing';
        } else {
          startupHeading.textContent = emptyHomeHeading;
          startupDescription.replaceChildren(...emptyHomeDescription.map(node => node.cloneNode(true)));
        }
      };
      setView = (view, direct = false) => {
        activeHomeBaseSetView(view, direct);
        if (state.active && state.view !== 'startup') lastStudyView = state.view;
      };
      root.addEventListener('click', event => {
        const button = event.target.closest('button[data-home-continue]');
        if (!button || button.disabled || !root.contains(button) || !state.active) return;
        setView(lastStudyView);
        root.querySelector(`[data-preview="${state.view}"]`).focus({ preventScroll: true });
      });
      languageInput.value = 'nb';
      levelInput.value = 'detailed';
      acknowledgement.checked = true;
