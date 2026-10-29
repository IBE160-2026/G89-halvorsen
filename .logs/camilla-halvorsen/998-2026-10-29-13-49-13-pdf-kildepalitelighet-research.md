# PDF-kildepålitelighet — research før PRD

## 2026-10-29 kl. 13:49 — Camilla Halvorsen

### Oppgave

Gjennomføre avgrenset teknisk research med `bmad-deep-recon` om PDF-tekstuttrekk, sidetilknytning, kildehenvisninger, sitatkontroll og uleselige filer som grunnlag for PRD i AI Study Buddy. Product Brief skal ikke endres, og PRD skal ikke opprettes.

### Plan

- Lese gjeldende brief, åpne punkter og research-workflow; følge [researchplanen](../../_bmad-output/planning-artifacts/research/technical-pdf-source-reliability-2026-10-29/brief.md).
- Innhente offisiell dokumentasjon, bevare kildegrunnlag i digests og skille dokumenterte funn fra løsningsforslag og anbefalinger.
- Kontrollere referanser, struktur og språk, og oppsummere beslutningsbehov for PRD.

### Resultat

- Lagret [research.md](../../_bmad-output/planning-artifacts/research/technical-pdf-source-reliability-2026-10-29/research.md), researchbrief, to kildedigests, egen BMAD-memlog, datert claimgrunnlag, staleness.json og quality-check.md i BMADs standardmappe.
- Undersøkt pypdf og PDF.js som betingede kandidater; ingen bibliotek- eller modellbeslutning tatt. Rapporten foreslår appstyrt fysisk sidenummer, opprinnelig kildespråk i utdrag og kontroll bare på sitert side.
- Skilt mellom funnet utdrag, korrekt tekstuttrekk og faglig støtte. Foreslått konservativ normalisering og tydelige feil-/dekningsmeldinger uten å innføre OCR eller større arkitektur.
- Mekanisk referansekontroll bestått for ni kilder. Separat semantisk kildekontroll fant ingen avvik i sentrale påstander. Struktur- og språkgjennomgang gjennomført. Seks hovedpåstander i ledger: tre uavhengig bekreftet og tre dokumentert med autoritativ enkeltkilde; ingen applikasjonstester eller modellkall.
- Product Brief, addendum og briefens memlog er uendret. Ingen PRD opprettet. Bare sesjonslogg og issues.md inngår i lokal loggcommit; researchfilene inngår ikke. Ingen push.

### Åpne punkter

- Diskutere forslag til PRD: normalisering, kilde-/utdragsstatus, delvis lesbare dokumenter og eventuell passordstøtte. Forslagene er ikke vedtatte krav.
- Eksisterende åpne punkter består: velge faktiske T1–T3- og demofiler med riktige delingsrettigheter; gjennomføre PDF-/referansetester og bestemme testede grenser og utdragslengde før Architecture velger bibliotek.
- Revalidere udaterte API-dokumenter ved bibliotekvalg og datert KI-API-kilde senest 2027-01-21 dersom prosjektet fortsetter da.
