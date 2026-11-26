# AI Study Buddy – arkitektur

## 2026-11-26 kl. 09:59 — Camilla Halvorsen

### Oppgave

Starte `/bmad-architecture` for AI Study Buddy med technology.md som foretrukket, tilpasset teknisk referanse og ferdig PRD/UX som grunnlag.

### Plan

- Lese arkitekturskill, løse konfigurasjon/tilpasninger og kontrollere eksisterende artefakter og kode.
- Hente gjeldende PRD-/UX-beslutninger, innhente en uavhengig skrivebeskyttet vurdering og registrere arvede føringer i beslutningsloggen.
- Avklare veiledet løp eller hurtigløp og om beslutningsdokumentet er eneste leveranse før arkitekturutkast.

### Resultat

- Skill aktivert for create. Konfigurasjon og workflow-tilpasninger er løst med uv-cache i `/private/tmp`; ingen aktiveringshooks eller ekstra persistente workflow-fakta er konfigurert. Norsk samtale/engelske dokumenter følger tidligere eksplisitt brukerføring.
- Ingen eksisterende arkitekturløp eller appkode funnet. Den uttrykkelige arkitekturinstruksen erstatter tidligere UX-økters avgrensning mot oppstart av neste fase. Eksisterende AGENTS.md-endring med teknologipreferansen er beholdt.
- Opprettet `_bmad-output/planning-artifacts/architecture/architecture-G89-halvorsen-2026-11-26/.memlog.md` gjennom felles memlog-hjelper, med kildegrunnlag, brukerens referansepreferanse, arvede v1-/UX-/sikkerhets-/validerings-/økt-/demo-regler og åpne arkitekturspørsmål. Etter sammenligning er brukerens første teknologivalg dokumentert som AD-1 nedenfor; konkrete versjoner er fortsatt åpne.
- Brukeren har uttrykkelig valgt veiledet løp og ett strukturert arkitekturdokument: teknisk grunnlag for Codex/KI-agenter, forståelig for Camilla og foreleseren, med korte begrunnelser for viktige valg/avvik. Enkelhet, gjennomførbarhet og vedlikehold prioriteres. En senere numerisk skjemabesvarelse er behandlet som tvetydig opp mot den tydelige friteksten; lagt veiledet løp til grunn og sagt dette til brukeren.
- Oppdatert beslutningsloggens formål og opprettet ARCHITECTURE-SPINE.md som første stillas fra skillens mal med avklart målgruppe, omfang og kilder. Teknologivalg og endelige AD-regler skrives etter den veiledede avklaringen; dokumentet er fortsatt draft og ikke klart for implementering.
- Første tema var frontend/backend og startoppsett. Primærkilder er kontrollert: offisiell Vite react-ts-startmal og statisk bygg, FastAPIs minimale oppsett/statiske frontendservering, Next.js create-next-app/Route Handlers og full FastAPI-startmal. Sammenlignet React/Vite med liten FastAPI-backend, Next.js/FastAPI og Next.js alene. Full database-/konto-/e-postmal vurderes som unødvendig for gjeldende v1.
- Uavhengig motvurdering bekrefter at forslaget er forsvarlig, men presiserer at Next.js også støtter statisk eksport uten Node ved kjøring. Begrunn avviket med færre rammeverkskonsepter, ikke at Next alltid krever en ekstra server. Vites startmal avgjør ikke økt/API-/feil-/testregler; dette følges videre i arkitekturen. Ingen pakker er installert, versjoner låst eller modell/parser valgt. Primærkildelenker og avveiinger finnes i beslutningsloggen.
- Brukeren har nå vedtatt alternativ 1: React/TypeScript med Vite og Python/FastAPI, med enkel og gjennomførbar v1. AD-1 er registrert som adopted i memlog og arkitekturdokumentet, med Binds/Prevents/Rule, kort begrunnelse, referanseavvik og primærkilder. Eksakte kompatible runtime-/pakkeversjoner gjenstår før implementering avhenger av dem; øvrige tjenester er ikke automatisk vedtatt.
- Neste tema er data-/økteierskap. Skrivebeskyttet motvurdering og React/FastAPI/MDN-kilder er brukt til å sammenligne midlertidig backend-arbeidsområde med gjentatt opplasting/uttrekk per generering. Anbefaling, ikke vedtak: React-minne for visning/læringsinnhold/fremdrift og én lokal backendprosess med gjenbrukbart sideuttrekk, låste valg/bekreftelse og ugjennomsiktig økt-ID. Opplastingskopier kan være midlertidige diskfiler; nettleserlukking er ikke pålitelig slettesignal, og fetch-avbrudd erstatter ikke vern mot sene svar. Oppryddingsfrist, fornyelse, kapasitetsgrenser og mekanismer er fortsatt åpne; ingen tall eller lagringsmodell er vedtatt.
- PRD, UX, technology.md og kode er uendret. Ingen app-/prototype-/KI-tester er gjennomført. Bare sesjonslogg og issues.md committes lokalt etter prosjektregelen; arkitekturloggen er lagret i arbeidskopien, ingen push.

### Åpne punkter

- Avklare foreslått midlertidig data-/økteierskap og gjenbruk av ett tekstuttrekk; deretter PDF-/kildeløp, KI, versjoner, grenser/opprydding og demo/oppstart med kildeverifisering. Arbeidsform, målgruppe og AD-1 teknologifamilier er avklart. Eksisterende arkitekturpunkt i issues.md er oppdatert; øvrige PRD-/evalueringspunkter består.
