# Kvalitet og evaluering – research

## 2026-11-02 kl. 13:30 — Camilla Halvorsen

### Oppgave

Gjennomføre godkjent BMAD Deep Recon om faglig korrekthet og kvalitet i sammendrag, flashcards og quiz som forberedelse til PRD for AI Study Buddy. Kommunisere på norsk, skrive rapport på engelsk og bevare Product Brief uten å opprette PRD. Ved avslutningen: kontrollere at funn, foreløpige anbefalinger og åpne spørsmål fra forklaringene og navnejusteringen er bevart i dokumentasjonen og denne eksisterende dagsseksjonen.

### Plan

- Følge [godkjent researchbrief](../../_bmad-output/planning-artifacts/research/technical-quality-evaluation-2026-11-02/brief.md), lese oppdatert produktgrunnlag, tema 1 og relevante åpne punkter.
- Innhente primærkilder gjennom avgrensede researchassistenter; skille dokumenterte funn, anbefalinger og åpne spørsmål.
- Utforme et overkommelig testforslag og kontrollere kilder, struktur, språk og BMAD-metadata.
- Sammenholde rapportens §§2–6, kildedigests og quality-check.md med øktens forklaringer; samordne eksisterende logg og issues.md uten ny logg eller nye produktkrav.

### Resultat

- Opprettet egen standardmappe for tema 2 med [engelsk researchrapport](../../_bmad-output/planning-artifacts/research/technical-quality-evaluation-2026-11-02/research.md), brief, imports/ (tom), digests/, .memlog.md, dated-claims.json, staleness.json og quality-check.md.
- Ni rapportkilder; skilt faglig korrekthet, sitatforekomst, semantisk støtte, dekning og oppgavekvalitet. Foreslått manuell rubrikk og repeterbart testopplegg for 12 sammendrag, seks flashcardsett og seks quizsett; eksisterende 9/10-kriterier beholdes som grunnlag.
- Samlet svar-/referansekontroll rapporteres på samme utvalg. Foreslåtte sammendragsterskler, utvalgsregler og eventuell felles terskel er ikke vedtatte krav. Fremhevet at 9/10 separat kan gi 8/10 samlet.
- BMADs mekaniske referansekontroll bestått: ni referanser, ingen manglende eller foreldreløse oppføringer. Uavhengig semantisk kildekontroll fant ingen vesentlige avvik. Struktur-/språkgjennomgang gjennomført og konkrete forbedringer innarbeidet.
- Maskinberegnet ledger: én uavhengig bekreftet generell påstand og åtte med autoritativ enkeltkildestøtte, merket unverified for uavhengig bekreftelse. Historiske kilder og utløpt ferskhetsvindu er tydelig oppgitt; ingen påstander om dagens modellkvalitet eller appens læringseffekt.
- Ingen Product Brief/addendum-endringer, PRD, kode, valgte PDF-er eller gjennomførte applikasjons-/modelltester. Bare logg og issues.md inngår i lokal loggcommit; ingen push.


- Avsluttende dokumentasjonskontroll 2026-11-02 kl. 14:35: hovedfunn, foreløpige anbefalinger og åpne spørsmål fra samtalen finnes allerede i rapportens §§2–6. Ingen faglige rapportendringer var nødvendige. Manuell kontroll mot original-PDF anbefales sammen med automatiske struktur-/plasseringstester; korrekthet, dekning, språk, kilde-/sitatkontroll og oppgavekvalitet vurderes separat.
- Presisert i gjennomgangen hvordan funnene brukes: sammendrag kontrolleres for korrekte påstander og nøkkelpunkter; flashcards for avgrenset spørsmål og korrekt svar; quiz for én forsvarlig fasit, alternativer og kildebasert feiltilbakemelding. Begge språk vurderes separat. Terskler for nøkkelpunkter og samlet svar-/kildekvalitet er fortsatt forslag. Kjente feil rettes og testes på nytt selv om 9/10 er nådd.
- Forklart kildearbeidet med søk etter primærforskning/offisiell veiledning fra ACL Anthology, NeurIPS, NIST, NBME, forfatterlaboratoriet ved Purdue og originalt studiesammendrag i PubMed. Kildedigests dokumenterer leste kilder og relevante avsnitt; ikke alle assistentenes nøyaktige søkestrenger er lagret. Historiske studier, engelsk-/oppgavebegrensninger og abstract-only-grunnlag gir ikke dokumentasjon på dagens modellkvalitet, Bokmål eller appens læringseffekt. Separat gjenlesing kontrollerer kildegjengivelsen, ikke uavhengig replikasjon.
- Navnejusteringen tidligere i økten omfattet research.md, brief.md og .memlog.md samt tittelen i denne loggen. Hovedoverskriften er «Quality and evaluation – AI Study Buddy», og loggtittelen «Kvalitet og evaluering – research». Filnavn/mappestruktur er beholdt; historisk omtale av tema 2 i resultatteksten er bevart. Loggtittelen ble committet lokalt i `682b40a`; ingen nye filer eller logger ble opprettet i navnejusteringen.
- Oppdatert eksisterende åpne punkter med vurdererkompetanse, genereringsvariasjon og omtesting ved modell-/prompt-/uttrekksendringer. Ingen nye krav vedtatt og ingen punkter lukket. Sluttkontrollen endret bare denne loggen og issues.md; Product Brief, PRD, researchfiler og andre eksisterende arbeidsendringer ble bevart. Ingen push.

### Åpne punkter

- Før endelige testkrav: diskutere sammendragsrubrikk og nøkkelpunkter, eventuell felles svar-/kildeterskel, kildegranularitet og telleregler; pilotere opplegget på faktisk T1-materiale. Dette presiserer tidligere PRD-/testpunkter uten å lukke dem. Avklare også om vurdereren kan kontrollere begge språk/fagbegreper, og om lokal genereringsvariasjon krever flere pilotkjøringer; bevare uklare vurderinger og ulike utfall. Testgrunnlaget må oppdateres og berørte tilfeller testes på nytt ved modell-/prompt-/uttrekksendringer. Ved senere bruk av automatiske kvalitetsmål/KI-dommer må metodegrunnlaget oppdateres og valideres lokalt for språk og oppgavetype. Ugyldig kildeplassering versus manglende sitattreff håndteres fortsatt som åpent spørsmål i eksisterende PDF-researchpunkt.
