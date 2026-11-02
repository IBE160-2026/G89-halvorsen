# Håndtering av opplastet materiale – research

## 2026-11-02 kl. 15:15 — Camilla Halvorsen

### Oppgave

Gjennomføre godkjent BMAD Deep Recon om håndtering av opplastede PDF-er som forberedelse til PRD for AI Study Buddy. Dekke lokal behandling, ekstern KI-overføring, lagring/sletting, personvern og test-/demorettigheter med et overkommelig IBE160-omfang. Kommunisere på norsk, skrive research på engelsk og bevare Product Brief uten å starte PRD.

### Plan

- Følge [godkjent researchbrief](../../_bmad-output/planning-artifacts/research/technical-uploaded-material-handling-2026-11-02/brief.md), forankret i oppdatert produktgrunnlag, begge tidligere researchrapporter og issues.md.
- Innhente offisielle leverandør-, myndighets-, avtale- og lisenskilder via to avgrensede researchassistenter og lokal kildeinnhenting.
- Skille dokumenterte funn, prosjektanbefalinger og åpne spørsmål; kontrollere sitater, ferskhet, struktur og språk.

### Resultat

- Opprettet egen standardmappe med [engelsk rapport](../../_bmad-output/planning-artifacts/research/technical-uploaded-material-handling-2026-11-02/research.md), brief, digests/, tom imports/, .memlog.md, dated-claims.json, staleness.json og quality-check.md.
- Foreslått lokal behandling og én aktiv kilde i minne, eksplisitt ekstern generering og lokal Clear, uten automatisk dokumenthistorikk. Lagringsoversikten skiller brukerens original, aktive data, midlertidige filer, logger, leverandørkopier og bevisst lagret test/demo.
- Gemini er fortsatt kandidat. Skilt EØS-betalingskrav fra databruksvilkår, 55-dagers misbruksretensjon fra valgfrie prosjektlogger, og 48-timers Files-utløp fra sletting av alle kopier. Nye prosjekters loggstandard fra 2026-10-26 og frivillig deling må kontrolleres før bruk.
- Anbefalt egenlaget eller tydelig lisensiert ikke-sensitivt materiale; skilt privat tilgang, ekstern KI-bruk, sensors demo og offentlig deling. Materialregister omfatter også kildeutdrag, lagrede svar og skjermbilder. Faktiske PDF-er og rettigheter er ikke valgt/klarert.
- Mekanisk BMAD-referansekontroll bestått for 16 kilder uten manglende/foreldreløse oppføringer. Frisk semantisk kontroll gjenhentet 11 utvalgte primærsider; presisert GDPR-anvendelse og usikkert 2025-år i regjeringens genererte kildehenvisning. Øvrige fem kilder har opprinnelig innhentingsgrunnlag, uten ny full gjenkontroll. Struktur-/språkgjennomgang innarbeidet.
- Maskinberegnet ledger: 0 uavhengig bekreftet, 16 primærkildestøttede påstander merket unverified for uavhengig utgiverbekreftelse. Dette betyr ikke at de mangler kildestøtte. Ferskhetsberegning: 6 av 10 daterte poster utenfor konservative vinduer; tidligste historiske kontroll 2023-10-27, neste fremtidige 2026-12-14. Kildene er hentet nå; datoene er kontrollflagg, ikke rettslig utløp.
- Ingen Product Brief/addendum-endringer, PRD, implementering, leverandørinnstillinger, modellkall, PDF-overføring eller applikasjons-/slettetester. Bare denne loggen og issues.md inngår i lokal loggcommit; ingen push. BMAD-katalogen peker på bmad-prd senere i ny kontekst når brukeren er klar.

### Åpne punkter

- Presisere eksisterende PRD-/materialpunkter med beslutninger om lokal nettleser/backend-behandling, Clear/utskifting og pågående kall, dokumentgrenser og testet opprydding; bekrefte API-leverandørens EØS-/betalings-/aldersvilkår, logger/deling/retensjon før første reelle opplasting. Registrere tillatelser for lokale/API-/demo-/repo-bruk av faktiske PDF-er og avledede utdrag/svar/skjermbilder, institusjonsregler og tilgang/slettedato for evalueringsevidens. Ved personopplysninger eller bredere hosting må roller, behandlingsgrunnlag/avtaler og overføringsvilkår avklares. Gjennomføre foreslåtte nettverk-/lagrings-/slettekontroller; forslagene er ikke vedtatte krav. Dette utdyper eksisterende åpne PRD-, test-/demo- og arkitekturpunkter; ingen av dem lukkes av researchen.
