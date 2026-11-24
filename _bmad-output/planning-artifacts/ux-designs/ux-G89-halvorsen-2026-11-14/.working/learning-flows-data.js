      // Authored synthetic study passages. No PDF is read and no factual validation is claimed.
      const learningSourceFilename = 'Studieteknikk.pdf';
      const learningSources = [
        { page: 2, text: 'Aktiv gjenhenting betyr å hente frem lært stoff uten å se i notatene først.' },
        { page: 2, text: 'Sammenlign svaret med notatene for å oppdage det som mangler eller trenger en korrigering.' },
        { page: 3, text: 'Repetisjon over flere økter innebærer å vende tilbake til det samme stoffet i ulike studieøkter.' },
        { page: 3, text: 'Hvis teksten ikke gir grunnlag for en bestemt sammenheng, bør du markere usikkerheten og undersøke videre.' },
        { page: 4, text: 'Et kildeutdrag hjelper deg å finne stedet du skal kontrollere. At et utdrag finnes på en side, avgjør ikke alene om en forklaring er riktig eller tilstrekkelig.' },
        { page: 4, text: 'Bruk slutten av økten til å samle de viktigste poengene. Skill mellom det du kan forklare selv, det du har rettet etter kildekontroll, og det du fremdeles trenger å undersøke.' },
        { page: 3, text: 'Prøv også å beskrive hvordan begrepet henger sammen med andre deler av faget. Hva forklarer det, og når kan du bruke det? Et enkelt eksempel kan gjøre en ellers generell formulering mer konkret.' }
      ];
      const learningQuestions = [
        { correct: 0, sources: [0],
          nb: { question: 'Hva er aktiv gjenhenting?', options: ['Forklare uten å se i notatene', 'Lese avsnittet en gang til', 'Markere alle overskriftene', 'Kopiere teksten ord for ord'], explanation: 'Aktiv gjenhenting er å hente frem stoffet fra hukommelsen før du ser i notatene. Å lese eller kopiere viser deg teksten i stedet.' },
          en: { question: 'What is active retrieval?', options: ['Explaining without looking at the notes', 'Reading the paragraph once more', 'Highlighting all the headings', 'Copying the text word for word'], explanation: 'Active retrieval means recalling material from memory before looking at the notes. Reading or copying shows you the text instead.' }
        },
        { correct: 1, sources: [1],
          nb: { question: 'Hvorfor sammenligne svaret ditt med notatene?', options: ['For å unngå å endre det første svaret', 'For å finne det som mangler eller må rettes', 'For å slippe å tenke på innholdet', 'For å kopiere alle sidene'], explanation: 'Sammenligningen skal avdekke mangler og behov for korrigering. Den er en kontroll av innholdet, ikke bare en gjentakelse av det første svaret.' },
          en: { question: 'Why compare your answer with the notes?', options: ['To avoid changing your first answer', 'To find missing points or statements to correct', 'To avoid thinking about the content', 'To copy every page'], explanation: 'The comparison identifies missing points and statements that need correction. It checks the content rather than simply repeating your first answer.' }
        },
        { correct: 2, sources: [2],
          nb: { question: 'Hva beskriver repetisjon over flere økter?', options: ['Å lese alle fagene samtidig', 'Å aldri åpne det samme stoffet igjen', 'Å vende tilbake til det samme stoffet i ulike økter', 'Å kopiere ett avsnitt mange ganger i én økt'], explanation: 'Repetisjon over flere økter innebærer å møte det samme stoffet ved ulike anledninger. Mange kopier i én økt er ikke flere studieøkter.' },
          en: { question: 'What describes repetition across sessions?', options: ['Reading every subject at once', 'Never opening the same material again', 'Returning to the same material in different sessions', 'Copying one paragraph many times in one session'], explanation: 'Repetition across sessions means revisiting the same material on different occasions. Making many copies in one session does not create several study sessions.' }
        },
        { correct: 3, sources: [0, 1],
          nb: { question: 'Du har forklart et begrep fra hukommelsen. Hva er neste steg i denne arbeidsmåten?', options: ['Anta at forklaringen er fullstendig', 'Slette notatene uten å lese dem', 'Velge et annet svar uten å kontrollere', 'Sammenligne forklaringen med notatene'], explanation: 'Etter gjenhenting sammenligner du svaret med notatene for å finne mangler eller feil. At du husker noe, avgjør ikke alene om forklaringen er fullstendig.' },
          en: { question: 'You have explained a concept from memory. What comes next in this approach?', options: ['Assume the explanation is complete', 'Delete the notes without reading them', 'Choose another answer without checking', 'Compare the explanation with the notes'], explanation: 'After retrieval, compare your answer with the notes to identify gaps or mistakes. Remembering something does not by itself establish a complete explanation.' }
        },
        { correct: 0, sources: [3],
          nb: { question: 'Teksten støtter ikke en sammenheng du ønsker å bruke. Hva bør du gjøre?', options: ['Markere usikkerheten og undersøke videre', 'Presentere sammenhengen som sikker', 'Finne på et eksempel som bevis', 'Fjerne alle kildehenvisninger'], explanation: 'Når teksten ikke støtter sammenhengen, skal du markere usikkerheten og undersøke videre. En antakelse eller et oppdiktet eksempel gir ikke kildegrunnlag.' },
          en: { question: 'The text does not support a connection you want to make. What should you do?', options: ['Acknowledge the uncertainty and investigate further', 'Present the connection as certain', 'Invent an example as proof', 'Remove every source reference'], explanation: 'When the text does not support a connection, acknowledge the uncertainty and investigate further. An assumption or invented example does not provide source support.' }
        },
        { correct: 1, sources: [4],
          nb: { question: 'Hva viser det at et kildeutdrag finnes på den oppgitte siden?', options: ['At alle genererte svar er riktige', 'Hvor teksten finnes, slik at du kan undersøke den', 'At hele forklaringen er fullstendig', 'At du ikke trenger å lese sammenhengen'], explanation: 'Sidetreffet viser hvor teksten finnes. Du må fremdeles vurdere sammenhengen og om teksten faktisk støtter forklaringen; plassering er ikke et bevis på riktighet.' },
          en: { question: 'What does finding an excerpt on its cited page establish?', options: ['That every generated answer is correct', 'Where the text is, so you can examine it', 'That the entire explanation is complete', 'That you need not read the context'], explanation: 'The page match locates the text. You still need to consider its context and whether it supports the explanation; location is not proof of correctness.' }
        },
        { correct: 2, sources: [5],
          nb: { question: 'Hva er et foreslått avslutningspunkt for studieøkten?', options: ['Å legge til nye antakelser uten kontroll', 'Å skjule det du fremdeles er usikker på', 'Å samle hovedpoenger, korrigeringer og åpne spørsmål', 'Å erklære alt stoffet ferdig lært'], explanation: 'Avslutningen samler hovedpoengene og skiller mellom det du kan forklare, det du har korrigert, og det du må undersøke. Den sier ikke at alt er ferdig lært.' },
          en: { question: 'What is a suggested way to end the study session?', options: ['Add new assumptions without checking', 'Hide what you are still unsure about', 'Gather key points, corrections and open questions', 'Declare that all the material is fully learned'], explanation: 'The ending gathers key points and distinguishes what you can explain, what you corrected and what needs further investigation. It does not declare everything fully learned.' }
        },
        { correct: 3, sources: [6],
          nb: { question: 'Hvordan kan du arbeide videre med en generell definisjon?', options: ['Bytte ut begrepet med et tilfeldig ord', 'Kopiere definisjonen uten å vurdere innholdet', 'Anta at begrepet gjelder alle situasjoner', 'Forklare sammenhenger og når begrepet kan brukes'], explanation: 'Du kan gå videre fra definisjonen ved å forklare sammenhenger og bruk, gjerne med et enkelt eksempel som passer til materialet. En generell definisjon gir ikke grunnlag for alle tenkelige bruksområder.' },
          en: { question: 'How can you develop your understanding of a general definition?', options: ['Replace the concept with a random word', 'Copy the definition without considering its meaning', 'Assume the concept applies to every situation', 'Explain its connections and when it can be used'], explanation: 'Develop the definition by explaining connections and use, with a simple example that fits the material. A general definition does not support every imaginable application.' }
        }
      ];
      const learningCardSources = [[0], [0, 1], [2]];
