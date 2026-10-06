# Tilbakemelding på product brief

| | |
|---|---|
| **Gruppe** | G89 – G89-halvorsen |
| **Product brief** | `_bmad-output/planning-artifacts/briefs/brief-G89-halvorsen-2026-09-26/product-brief.md` (commit `39b5049`) |
| **Tilbakemelding fra** | Faglærer i IBE160 (utarbeidet med KI-støtte) |
| **Dato** | 2026-10-06 |

## Samlet vurdering

- **Godt utgangspunkt med justeringer.** Gruppen kan gå videre og innarbeide punktene under.

**Det som er bra:**

1. Briefen har en tydelig idé som skiller den fra et generisk oppsummeringsverktøy: kildehenvisninger til det opplastede materialet, og at et feil svar på en flervalgsquiz leder studenten tilbake til riktig avsnitt med en fyldigere forklaring. Det gjør KI-innholdet etterprøvbart, slik dere selv vektlegger.
2. Dere er ærlige og nøkterne. NotebookLM og Quizlet er nevnt som overlappende verktøy, dere påstår ikke at funksjonene er unike, og avgrensningene er tydelige (ingen innlogging, ingen synkronisering, ingen læringsplan, ingen vurdering av skriftlige svar).

**De viktigste endringene:**

1. Fyll inn det som står som åpent i suksesskriteriene: «Specific test materials, supported options, and acceptance thresholds remain to be defined». Bestem hvilke språk og detaljnivåer som støttes, velg to–tre konkrete testdokumenter fra egne emner, og sett terskler, for eksempel «minst 9 av 10 quizspørsmål har riktig fasit og en henvisning som peker til et avsnitt som støtter svaret».
2. Beskriv hvordan kildehenvisningene skal fungere. Skal de peke til side, avsnitt eller et utdrag av teksten? Det avgjør hvor vanskelig PDF-lesingen blir, og hvordan dere kan teste at henvisningene stemmer.
3. Planlegg hvordan sensor kan kjøre appen uten deres API-nøkkel til språkmodellen, for eksempel med en testmodus som bruker lagrede svar for ett eksempeldokument.

## Vanskelighetsgrad og gjennomførbarhet

### Vurdert vanskelighetsgrad

- **Enkel**

**Sammenlignbart med:** 1) AI Study Buddy (enkel), kombinert med 8) Foredragsnotater – sammendrag og quizgenerator (enkel). Kildehenvisninger og tilbakekobling fra feil svar gjør prosjektet litt mer krevende enn grunnforslaget, men det ligger fortsatt i kategorien enkel.

**Begrunnelse:**

| Faktor | Nivå (lav / middels / høy) | Kommentar |
|---|---|---|
| Domenelogikk – hvor mange og hvor kompliserte regler og beregninger må stemme? | Lav | Quizretting, valg av språk og detaljnivå, og kobling fra feil svar til kilde. Oversiktlige regler. |
| Datamodell – antall entiteter og relasjoner mellom dem | Lav | Dokument, avsnitt/kilde, sammendrag, flashcard, quizspørsmål med svar og henvisning. Ingen brukerkontoer. |
| Brukere, roller og innlogging | Lav | Bevisst ingen innlogging i v1. |
| KI-funksjonalitet i appen, f.eks. kall til språkmodell, prompts i koden og håndtering av usikre svar | Middels | Tre typer generert innhold, og krav om at hvert svar skal ha en kildehenvisning som faktisk støtter det. Det krever strukturerte svar fra modellen. |
| Integrasjoner og eksterne tjenester, f.eks. API-er, betaling og e-post | Lav | Én språkmodell. Leverandør er ikke valgt ennå. |
| Sanntid, samtidighet eller flere brukere som påvirker hverandre | Lav | Ingen. |
| Filhåndtering, f.eks. opplasting, PDF-lesing og eksport | Middels | Opplasting og tekstuttrekk fra PDF, med behov for å holde på side- eller avsnittsinformasjon for henvisningene. |
| Sikkerhet og personvern | Lav | Ingen kontoer eller personopplysninger. Kursmateriale sendes til en ekstern språkmodell – det kan nevnes. |

**Hva vanskelighetsgraden betyr for dere:**

- _Enkel:_ Et enkelt prosjekt gir stor sjanse for å bli ferdig. Vanskelighetsgraden inngår likevel i vurderingen, så for å nå helt opp må dere vise mer i gjennomføringen. Det betyr særlig et gjennomarbeidet design, grundig testing, en tydelig dokumentert prosess og en README som virker. Kildehenvisningene er deres beste mulighet til å vise kvalitet – gjør dem pålitelige og testbare.

### Gjennomførbarhet med BMAD og Claude Code

Dere skal planlegge med BMAD (product brief → PRD → arkitektur → epics og stories) og implementere med Claude Code. Vurderingen under tar hensyn til at det må være tid til hele denne flyten, og til testing, retting og README til slutt.

| Spørsmål | Vurdering (OK / risiko / stor risiko) | Kommentar |
|---|---|---|
| **Tid og omfang** – kan v1 realistisk bli ferdig og stabil i løpet av semesteret, med tid til flere iterasjoner? | OK | Realistisk for en gruppe på én person, særlig fordi innlogging og fremdriftslagring er holdt utenfor. Bygg sammendrag først, deretter quiz med henvisninger, og til slutt flashcards. |
| **BMAD-flyten** – er briefen konkret nok til at PRD, arkitektur og stories kan lages uten store hull, og blir det overkommelig mange stories? | OK | Funksjonene er tydelige og avgrenset. De åpne punktene (språk, detaljnivå, terskler) bør avklares i PRD-en. |
| **Egnet for Claude Code** – bruker løsningen en vanlig, godt dokumentert teknologistakk som Claude Code håndterer godt, eller krever den nisjeteknologi, spesialmaskinvare eller mye manuell konfigurasjon? | OK | En enkel webapp med PDF-lesing og LLM-kall er godt dokumentert. Velg en enkel stakk i arkitekturen. |
| **Kontroll på KI-ens arbeid** – kan gruppen selv avgjøre om koden gjør det riktige? Krever domenet kunnskap gruppen ikke har, f.eks. avanserte beregninger eller fagregler, så er det vanskelig å kvalitetssikre. | OK | Du bruker eget kursmateriale og kan selv kontrollere fasit og henvisninger. Den manuelle sammenligningen dere beskriver, er et godt opplegg. |
| **Testbarhet** – finnes det tydelige regler og forventede resultater som tester kan skrives mot? | Risiko | Quizretting, språkvalg og at henvisninger peker til et eksisterende avsnitt kan testes automatisk. Om innholdet er faglig riktig, må testes manuelt. Tersklene mangler ennå. |
| **Kjørbar for sensor** – kan appen kjøres lokalt etter README, uten gruppens nøkler, betalte kontoer eller egen infrastruktur? | Risiko | Ikke beskrevet. Språkmodellen krever trolig en nøkkel – legg inn testmodus eller beskriv i README hvordan sensor skaffer en gratis nøkkel. |
| **Avhengigheter og kostnader** – krever løsningen betalte API-er, f.eks. språkmodeller, og finnes det en plan for kostnad, testmodus eller mock-data? | Risiko | Leverandør og kostnad er ikke nevnt. Velg modell i arkitekturen, gjerne med et gratisnivå, og planlegg mock-svar. |

**Konklusjon om gjennomførbarhet:**

- **Gjennomførbart som beskrevet.**

**Forslag til justering av omfang eller vanskelighetsgrad:**

1. Hold v1 som beskrevet, men gjør den valgfrie fremdriftslagringen i nettleseren til et tydelig trinn 2 etter at kjerneflyten er testet. Det gir en naturlig utvidelse hvis tiden tillater det.
2. Hvis dere vil løfte vanskelighetsgraden, legg til en enkel kontroll i koden som sjekker at hver kildehenvisning faktisk finnes i dokumentet (for eksempel at det siterte utdraget kan gjenfinnes i teksten), og vis en advarsel når den ikke gjør det.

## Hvorfor product brief er viktig for mappen

Product brief er utgangspunktet for PRD, arkitektur, stories og til slutt koden. Del 1 av mappen vurderes blant annet på om sensor kan følge en sporbar vei fra plan til ferdig app. Den vurderes også på om appen gjør det dere har beskrevet, om den er testet, om den er godt designet, og om den kan kjøres etter README. Et uklart, for stort eller for lite brief gjør alt dette vanskeligere senere. Det er mye enklere å rette nå enn sent i semesteret.

## 1. Gjennomgang av briefens deler

| Del av brief | Status | Kommentar |
|---|---|---|
| Executive Summary – er det klart hva appen er, og hvilket problem den løser? | OK | Tydelig hva appen gjør: sammendrag, flashcards og flervalgsquiz fra eget kursmateriale, med kildehenvisninger. |
| The Problem – er problemet konkret, med reelle situasjoner og brukere? | Juster | Problemet er riktig, men generelt. Gi gjerne et konkret eksempel fra et eget emne, for eksempel en forelesning med 40 lysark før en midtveiseksamen. |
| The Solution – beskriver løsningen brukeropplevelsen, ikke bare teknologi? | OK | Beskriver hva studenten gjør og opplever, inkludert hva som skjer ved feil svar. |
| What Makes This Different – er vurderingen ærlig og realistisk? | OK | Ærlig om NotebookLM og Quizlet, og et realistisk fokus på etterprøvbarhet. |
| Who This Serves – er primærbrukerne tydelige, og vet vi hva de trenger? | Juster | «University and college students» er bredt. Beskriv primærbrukeren mer konkret, for eksempel en student på et bestemt studieprogram med mye PDF-lysark, slik at designet kan bygges rundt én situasjon. |
| Success Criteria – kan kriteriene faktisk sjekkes eller testes? | Juster | Godt strukturert og nesten testbart. Fyll inn testmateriale, støttede valg og terskler, så kriteriene kan bli testtilfeller. |
| Scope – er det klart hva som er med i første versjon, og hva som ikke er det? | OK | Tydelig «In» og «Out», med valgfri fremdriftslagring tydelig merket. |
| Vision – henger visjonen sammen med resten uten å blåse opp omfanget? | OK | Kontoer, synkronisering og læringsplan er tydelig plassert etter v1. |

## 2. Utgangspunkt for del 1 av mappen

Punktene følger kriteriene i sensorveiledningen for del 1. Vektene i parentes viser hvor mye hvert kriterium teller i del 1.

| Kriterium i del 1 | Hva briefen bør legge til rette for | Status | Kommentar |
|---|---|---|---|
| **1. Prosess og KI-styring** (30 %) | Brief som er presis nok til at PRD og stories kan bygges direkte på den, slik at krav kan spores fra brief til kode. | OK | Briefen er presis og ligger i BMAD-strukturen. Lagre gjerne prompt-iterasjonene for generering og henvisninger som sporbar KI-styring. |
| **2. Funksjonalitet og omfang** (20 %) | Realistisk omfang for gruppen og semesteret: en tydelig kjerneflyt som kan bli ferdig og stabil, og nok innhold til å vise reell funksjonalitet. | OK | Tre typer studiehjelp pluss tilbakekobling til kilden gir nok funksjonalitet, med et realistisk omfang. |
| **3. Kvalitetssikring og testing** (15 %) | Suksesskriterier og funksjoner som er konkrete nok til å bli testtilfeller. | Juster | Kriteriene er gode, men mangler terskler og konkret testmateriale. |
| **4. Design og brukeropplevelse** (10 %) | Tydelige brukere og brukssituasjoner som designet kan bygges rundt, gjerne med de viktigste skjermbildene eller flytene skissert. | Juster | Skjermbildene kan utledes (opplasting, sammendrag, flashcards, quiz med tilbakemelding). Skissér særlig hvordan en kildehenvisning vises, og hva som skjer ved feil svar. |
| **5. Kodekvalitet og arkitektur** (10 %) | Teknologivalg som er begrunnet og ikke mer komplekse enn appen trenger. | OK | Ingen kontoer og ingen backend-synkronisering holder arkitekturen enkel. Begrunn valg av språkmodell og PDF-bibliotek i arkitekturen. |
| **6. README og kjørbarhet** (10 %) | Løsning som andre kan kjøre lokalt uten betalte kontoer, og uten tilgang til gruppens egne tjenester og nøkler. | Juster | Planlegg testmodus eller oppskrift for nøkkel, og legg ved et eksempeldokument sensor kan bruke. |
| **7. Ryddighet i repoet** (5 %) | En plan for hvor hemmeligheter, testdata og dokumentasjon skal ligge. | Juster | Ikke beskrevet. Bruk `.env.example` for nøkkelen, og bruk bare testdokumenter du har lov til å dele i et offentlig repo. |

## 3. Neste steg for gruppen

1. Fyll inn støttede språk og detaljnivåer, testdokumenter og terskler i «Success Criteria».
2. Bestem formatet på kildehenvisningene (side, avsnitt eller sitat) og beskriv det i Solution eller PRD.
3. Velg språkmodell i arkitekturen, og beskriv hvordan sensor kan kjøre appen uten din nøkkel.

Oppdater product brief i repoet når dere har gjort endringene, slik at historikken viser hvordan planen utviklet seg. Det er en del av prosessen sensor ser etter.
