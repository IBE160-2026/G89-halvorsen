# AI Study Buddy – arkitektur

## 2026-11-26 kl. 09:47 — Camilla Halvorsen

### Oppgave

Starte `/bmad-architecture` for AI Study Buddy med technology.md som foretrukket, tilpasset teknisk referanse og ferdig PRD/UX som grunnlag.

### Plan

- Lese arkitekturskill, løse konfigurasjon/tilpasninger og kontrollere eksisterende artefakter og kode.
- Hente gjeldende PRD-/UX-beslutninger, innhente en uavhengig skrivebeskyttet vurdering og registrere arvede føringer i beslutningsloggen.
- Avklare veiledet løp eller hurtigløp og om beslutningsdokumentet er eneste leveranse før arkitekturutkast.

### Resultat

- Skill aktivert for create. Konfigurasjon og workflow-tilpasninger er løst med uv-cache i `/private/tmp`; ingen aktiveringshooks eller ekstra persistente workflow-fakta er konfigurert. Norsk samtale/engelske dokumenter følger tidligere eksplisitt brukerføring.
- Ingen eksisterende arkitekturløp eller appkode funnet. Den uttrykkelige arkitekturinstruksen erstatter tidligere UX-økters avgrensning mot oppstart av neste fase. Eksisterende AGENTS.md-endring med teknologipreferansen er beholdt.
- Opprettet `_bmad-output/planning-artifacts/architecture/architecture-G89-halvorsen-2026-11-26/.memlog.md` gjennom felles memlog-hjelper, med kildegrunnlag, brukerens referansepreferanse, arvede v1-/UX-/sikkerhets-/validerings-/økt-/demo-regler og åpne arkitekturspørsmål. Ingen konkrete teknologi- eller versjonsvalg er vedtatt.
- Brukeren har uttrykkelig valgt veiledet løp og ett strukturert arkitekturdokument: teknisk grunnlag for Codex/KI-agenter, forståelig for Camilla og foreleseren, med korte begrunnelser for viktige valg/avvik. Enkelhet, gjennomførbarhet og vedlikehold prioriteres. En senere numerisk skjemabesvarelse er behandlet som tvetydig opp mot den tydelige friteksten; lagt veiledet løp til grunn og sagt dette til brukeren.
- Oppdatert beslutningsloggens formål og opprettet ARCHITECTURE-SPINE.md som første stillas fra skillens mal med avklart målgruppe, omfang og kilder. Teknologivalg og endelige AD-regler skrives etter den veiledede avklaringen; dokumentet er fortsatt draft og ikke klart for implementering.
- Første tema er frontend/backend og startoppsett. Primærkilder er kontrollert: offisiell Vite react-ts-startmal og statisk bygg, FastAPIs minimale oppsett/statiske frontendservering, Next.js create-next-app/Route Handlers og full FastAPI-startmal. Forslag, ikke vedtak: React/TypeScript med Vite og liten FastAPI-backend; sammenlignes med Next.js/FastAPI og Next.js alene. Referansens Python/React-prinsipper kan beholdes med mindre frontendrammeverk; full database-/konto-/e-postmal vurderes som unødvendig for gjeldende v1.
- Uavhengig motvurdering bekrefter at forslaget er forsvarlig, men presiserer at Next.js også støtter statisk eksport uten Node ved kjøring. Begrunn avviket med færre rammeverkskonsepter, ikke at Next alltid krever en ekstra server. Vites startmal avgjør ikke økt/API-/feil-/testregler; dette følges videre i arkitekturen. Ingen pakker er installert, versjoner låst, modell/parser valgt eller stakk vedtatt. Primærkildelenker og avveiinger finnes i beslutningsloggen.
- PRD, UX, technology.md og kode er uendret. Ingen app-/prototype-/KI-tester er gjennomført. Bare sesjonslogg og issues.md committes lokalt etter prosjektregelen; arkitekturloggen er lagret i arbeidskopien, ingen push.

### Åpne punkter

- Ta første veiledede valg om frontend/backend/startoppsett; deretter følge opp økteierskap, PDF-/kildeløp, KI, grenser/opprydding og demo/oppstart med kildeverifisering før teknologibinding. Arbeidsform og målgruppe er avklart. Eksisterende arkitekturpunkt i issues.md er oppdatert; øvrige PRD-/evalueringspunkter består.
