# PDF-kildepålitelighet — research før PRD

## 2026-10-29 kl. 15:27 — Camilla Halvorsen

### Oppgave

Gjennomføre avgrenset teknisk research med `bmad-deep-recon` om PDF-tekstuttrekk, sidetilknytning, kildehenvisninger, sitatkontroll og uleselige filer som grunnlag for PRD i AI Study Buddy. Avslutte tema 1 ved å kontrollere dokumentasjonen mot diskusjonen og bevare foreløpige vurderinger og åpne spørsmål. Product Brief skal ikke endres, og PRD skal ikke opprettes.

### Plan

- Lese gjeldende brief, åpne punkter og research-workflow; følge [researchplanen](../../_bmad-output/planning-artifacts/research/technical-pdf-source-reliability-2026-10-29/brief.md).
- Innhente offisiell dokumentasjon, bevare kildegrunnlag i digests og skille dokumenterte funn fra løsningsforslag og anbefalinger.
- Kontrollere referanser, struktur og språk, og oppsummere beslutningsbehov for PRD.
- Ved avslutningen: sammenholde rapporten med diskusjonen, samordne kun vesentlige mangler og oppdatere denne eksisterende dagsseksjonen og issues.md uten ny loggfil.

### Resultat

- Lagret [research.md](../../_bmad-output/planning-artifacts/research/technical-pdf-source-reliability-2026-10-29/research.md), researchbrief, to kildedigests, egen BMAD-memlog, datert claimgrunnlag, staleness.json og quality-check.md i BMADs standardmappe.
- Undersøkt pypdf og PDF.js som betingede kandidater; ingen bibliotek- eller modellbeslutning tatt. Rapporten foreslår appstyrt fysisk sidenummer, opprinnelig kildespråk i utdrag og kontroll bare på sitert side.
- Skilt mellom funnet utdrag, korrekt tekstuttrekk og faglig støtte. Foreslått konservativ normalisering og tydelige feil-/dekningsmeldinger uten å innføre OCR eller større arkitektur.
- Mekanisk referansekontroll bestått for ni kilder. Separat semantisk kildekontroll fant ingen avvik i sentrale påstander. Struktur- og språkgjennomgang gjennomført. Seks hovedpåstander i ledger: tre uavhengig bekreftet og tre dokumentert med autoritativ enkeltkilde; ingen applikasjonstester eller modellkall.
- Gjennomgått løsningenes vanskelighetsgrad med brukeren. Enkel sitatkontroll på oppgitt side, begrenset behandling av mellomrom/linjeskift og tydelige advarsler vurderes som realistiske. Automatisk oppdagelse av all manglende eller feilordnet tekst er vanskeligere og kan ikke garanteres.
- Oppdatert kun vesentlige diskusjonspunkter i research.md: brukerens foreløpige preferanse er konservativ behandling som stopper ved tydelige uttrekksfeil. Den tidligere anbefalingen om delvis behandling etter bekreftelse er nå et alternativ. Muligheten for å vise KI-svar med ubekreftet henvisning og skillet mellom manglende sitattreff og ugyldig kildeplassering er presisert.
- Dokumentert at stoppkriterier, normalisering og eventuell delvis behandling må vurderes etter testing med representative PDF-er. Oppdatert researchens egen memlog med diskusjonsutfall og avslutning. Ingen nye kildefunn, endelige krav eller bibliotekvalg; eksisterende kildedigests og ferskhetsgrunnlag er bevart.
- Product Brief, addendum og briefens memlog er uendret. Ingen PRD opprettet. Bare sesjonslogg og issues.md inngår i lokal loggcommit; researchfilene inngår ikke. Ingen push.

### Åpne punkter

- Etter representative PDF-tester: revurdere foreløpige anbefalinger om normalisering, kilde-/utdragsstatus og konservativ behandling. Avklare konkrete stoppkriterier, blanke sider, ugyldig kildeplassering versus manglende sitattreff og eventuell passordstøtte; kontrollere at statusmeldingene forstås. Forslagene er ikke vedtatte krav.
- Eksisterende åpne punkter består: velge faktiske T1–T3- og demofiler med riktige delingsrettigheter; gjennomføre PDF-/referansetester og bestemme testede grenser og utdragslengde før Architecture velger bibliotek.
- Revalidere udaterte API-dokumenter ved bibliotekvalg og datert KI-API-kilde senest 2027-01-21 dersom prosjektet fortsetter da.
