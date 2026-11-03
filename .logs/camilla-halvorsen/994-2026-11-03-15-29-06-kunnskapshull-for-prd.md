# Kunnskapshull før PRD

## 2026-11-03 kl. 15:29 — Camilla Halvorsen

### Oppgave

Vurdere om AI Study Buddy har viktige kunnskapshull utover de tre avsluttede researchtemaene. Skille undersøkelser før PRD fra beslutninger i PRD/Architecture og temaer utenfor v1, med utgangspunkt i Product Brief, research, lærerens tilbakemelding og åpne spørsmål.

### Plan

- Lese Product Brief/addendum, lærerens tilbakemelding, alle tre researchrapportene og eksisterende issues.md.
- Vurdere manglende kunnskapsgrunnlag separat fra åpne produktvalg og manglende empiriske tester.
- Kontrollere det identifiserte nye sikkerhetstemaet mot to offisielle OWASP-sider, uten å starte en full researchrunde eller PRD.

### Resultat

- Grunnlaget støtter overgang til PRD. Ingen bred fjerde researchrapport anbefales som generell forutsetning; hovedmangelen er praktisk validering og valg, ikke flere generelle kilder. Ingen av rapportene dokumenterer appens faktiske resultater.
- Tydeligste supplerende kunnskapshull: instruksjoner i PDF-tekst (indirekte prompt injection) og trygg visning av modell-/kildetekst. Eksisterende rapporter dekker strukturerte svar, kildevalidering, opplastingsvern og logging, men ikke disse risikoene systematisk. Anbefalt kort undersøkelse før sikkerhetskravene i PRD låses: realistiske feilscenarier, forholdsmessige grenser og noen negative tester. Ikke et krav om garanti, avansert filterplattform eller omfattende penetrasjonstest. Teknisk løsning og faktiske tester hører til Architecture/implementering.
- Begrenset ekstern støtte hentet 2026-11-03: [OWASP Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) beskriver indirekte instruksjoner i dokumenter og begrensningene ved filtrering; [OWASP Improper Output Handling](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/) beskriver risiko og validering/koding av modellutdata før visning. Dette støtter temaets relevans, ikke at denne appen er testet eller sårbar.
- Praktiske avklaringer før kravene låses: identifisere T1–T3/demo og rettigheter; forberede ett lite T1-uttrekks-/evalueringspilotforsøk for å kontrollere representativitet og arbeidsmengde; kontrollere original oppgavetekst/sensorveiledning og innleveringsdato. De første punktene viderefører eksisterende research/issues. Addendum opplyser at original oppgave og full vurderingsrubrikk ikke er levert; lærerens tilbakemelding er tilgjengelig, men er ikke en erstatning for dem. Ingen modelloverføring før material-/leverandørvilkår er avklart. Full akseptansetest kreves ikke før PRD-start.
- PRD: avklare observerbar feil-/kildeatferd, sammenkoblet fasit-/referanseterskel, sammendragsrubrikk, quizflyt/antall/nytt forsøk, oppsummeringsspørsmål versus separat quiz, Clear og demo. Særlig View source og forståelse av «utdrag funnet» versus faglig støtte bør skisseres og prøves enkelt under PRD/UX; grunnleggende tastaturbruk/lesbarhet tas med. Brukerbehov og tidsgevinst er foreløpige; et konkret eget studieforløp og senere tidsmåling er tilstrekkelig for avgrenset v1.
- Architecture: enkel stakk og uttrekksvei, modell/leverandør og aktuelle vilkår, API-nøkler, kostnadsramme, kontekst-/utdatagrenser, ventetid, begrensede nye forsøk og håndtering av nettfeil/avvisning/ufullstendige svar. PRD angir forventet brukeropplevelse, Architecture fastsetter og verifiserer mekanismen. Manglende rimelig/tillatt live API-rute må gi ny scopevurdering før arkitektur låses; demomodus erstatter ikke planlagt live-integrasjon.
- Utenfor nødvendig v1-research: bred konkurranse-/markedsstudie, generaliserbar læringseffekt, stor brukerundersøkelse, egen modelltrening, omfattende modellrangering, OCR/avansert tabell- og diagramforståelse, vektordatabase uten dokumentert behov, kontoer/synk/læringsplan og drift for mange offentlige brukere. Grunnleggende sikkerhet, personvern og brukbarhet gjelder fortsatt. Utvidet utrulling eller datatyper krever ny vurdering.
- Lærerens tidligere hull om språk, detaljnivå, referanseformat og nøkkelfri demo er nå beskrevet i briefen. Konkrete filer, implementering og verifisering er fortsatt åpne. Lærerens prioritering av stabil kjerne, testing, design, sporbar KI-prosess og kjørbar README tilsier avgrensede kontroller fremfor omfangsøkning.
- Ingen PRD, ny full researchrapport, produktkrav, kode eller tester opprettet/endret. Nye oppfølgingspunkter er anbefalinger, ikke vedtatte krav. Kun denne loggen og issues.md inngår i lokal loggcommit; ingen push.

### Åpne punkter

- Vurdere en kort supplerende undersøkelse av indirekte prompt injection i PDF-tekst og trygg visning av modell-/kildetekst før sikkerhetskrav låses; konkretisere enkle negative tester i PRD/Architecture.
- Kontrollere opprinnelig oppgavetekst og full sensorveiledning mot planlagt leveranse og prosess; eksakt frist ligger allerede som åpent punkt.
- Skissere View source, kildevarsler og feil-svar-flyt under PRD/UX, og gjøre en enkel forståelsessjekk samt kontroll av grunnleggende tastaturbruk/lesbarhet.
- Eksisterende materialvalg, pilot, evalueringsregler, leverandør-/kostnadsvurdering og gjennomføringstester i issues.md består; ingen punkter er lukket av denne vurderingen.
