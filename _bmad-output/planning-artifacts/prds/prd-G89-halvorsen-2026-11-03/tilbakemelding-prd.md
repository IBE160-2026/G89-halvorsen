# Tilbakemelding på PRD

| | |
|---|---|
| **Gruppe** | G89 – G89-halvorsen |
| **PRD vurdert** | `_bmad-output/planning-artifacts/prds/prd-G89-halvorsen-2026-11-03/prd.md` (status `final`, sist endret 2026-11-03, commit 858f328) |
| **Dato** | 2026-11-12 |
| **Type** | Formativ tilbakemelding, ikke karakter |

## 1. Samlet inntrykk

Dette er en gjennomarbeidet og eid PRD med tydelig tese: kildeforankret kvalitet foran antall, og konservativ feilhåndtering når PDF-en ikke kan leses pålitelig. Avgrensning, personvern, KI-kontroll og testplan er uvanlig godt dekket for et studentprosjekt. Risikoen ligger i størrelsen: 46 tett formulerte FR-er med mange innbyrdes henvisninger er mye for ett semester og én person, og FR-ene mangler eksplisitte, enkeltstående testkonsekvenser. Det gjør story-oppdeling og testskriving tyngre enn nødvendig.

## 2. Dette fungerer godt

- **Ærlig scope og tydelige valg.** «V1 boundaries» lister hva som er utelatt (OCR, kontoer, adaptiv læring m.m.), og «The defining tradeoffs are a temporary study session without recovery after reload, source-grounded quality over item count» navngir hva som er valgt bort.
- **KI-kontroll og testbar kvalitet.** FR-36/FR-37 («omit an entire item if any reference remains unverifiable»), NFR-1–NFR-3 (prompt injection, inert visning, validering av strukturerte svar) og SM-2–SM-4 (minst 9 av 10 riktige svar og støttede referanser, per case) gjør KI-innholdet etterprøvbart. Dette følger opp det dere skrev i briefen.
- **Kjørbar for sensor.** FR-42 gir en merket nøkkelfri demo med lagrede sammendrag, kort og quiz på begge språk, og skiller demo-kvalitet fra live-kvalitet. «These are planned checks, not completed results» er riktig holdning.

## 3. Oversikt per dimensjon

| Dimensjon | Vurdering | Kort begrunnelse |
|---|---|---|
| Beslutningsklarhet – er valg og avveininger synlige? | god | Avveininger er navngitt, men åpne punkter er spredt (Validation plan, Handoff, addendum) og samles ikke. |
| Substans – er innholdet fortjent, eller «pynt»? | sterk | Ingen pynte-personas eller boilerplate-NFR-er; kravene bærer preg av reelle valg og forskning. |
| Strategisk sammenheng – har PRD-en en tese som funksjonene tjener? | god | Tydelig tese om kildeforankring, men «less time» (kjerneløftet) har ingen målbar SM (SM-6 uten terskel). |
| Testbarhet – vet man når hvert FR er ferdig? | god | Mange konkrete tall og grensetilfeller, men ingen «Consequences» per FR, og flere terskler skyves til arkitekturen. |
| Scope og avgrensning – er utelatelser eksplisitte? | god | Utelatelser er tydelige; det mangler heller en prioritering innenfor v1, gitt 46 FR-er. |
| Brukbarhet for neste fase – kan UX, arkitektur og stories hente fra den? | god | Ryddige og sammenhengende FR-ID-er, men ingen glossar, bare én UJ og ingen FR-til-UJ-henvisninger. |
| Formtilpasning – passer PRD-formen produktet? | god | Kapasitetsspesifikasjon passer et solo-verktøy; livssyklusreglene er mer formelle enn produktet trenger. |

## 4. Viktigste forbedringer

### 4.1 FR-ene har ikke avgrensede, testbare konsekvenser
- **Alvorlighet:** høy
- **Hvor:** §Features, f.eks. FR-1: «show an understandable message explaining the problem and next step»; FR-41: «adequate reliable main-text coverage»; FR-36: «within a finite limit»
- **Problem og hvorfor det betyr noe:** Enkeltkrav inneholder flere forhold i én dyp setning, og ord som «understandable», «adequate» og «finite» kan ikke bli testtilfeller uten at noen tolker dem. Story-oppdeling og QA bygger på FR-ene, ikke på «Boundary checks»-avsnittene.
- **Forslag:** Gi hvert FR 2–4 punkter «Consequences». Eksempel: *FR-43: Brukeren kan ikke starte generering med en passordbeskyttet PDF. – Meldingen inneholder teksten «passord» og et forslag om en annen fil. – Eksisterende økt, kort og quiz er uendret etter avvisningen. – Ingen tekst fra filen er sendt til KI-tjenesten.* Sett konkrete tall (f.eks. maks 3 forsøk) som foreløpige verdier merket «[ASSUMPTION]» i stedet for å utsette alt til arkitekturen.

### 4.2 Omfanget er stort, og språkbytte-reglene er spredt
- **Alvorlighet:** høy
- **Hvor:** §Output language: FR-4, FR-20–FR-23 pluss FR-31; §Study-session lifecycle FR-14–FR-18
- **Problem og hvorfor det betyr noe:** Én person skal bygge opplasting, tre læringsfunksjoner, to språk, to sammendragsnivåer, bekreftelsesdialoger, rollback ved feil, forsinkede svar (FR-18), kildepanel og demo. Språkbytte alene er fordelt på seks FR-er som refererer til hverandre. Det er vanskelig å se hva som er «må» og hva som er «bør».
- **Forslag:** Merk hvert FR som *Kjerne* eller *Utvidelse*, og sett kjerneflyten først (last opp → sammendrag → kort/quiz → kilde). Samle språkbytte i én tilstandstabell: «handling – før – etter suksess – etter feil». Vurder å la språkbytte i v1 bety «last opp på nytt» og flytt FR-20–FR-23 til utvidelsene.

### 4.3 Glossar og brukerreise-kobling mangler
- **Alvorlighet:** medium
- **Hvor:** Hele dokumentet; §User journey har bare UJ-1 uten henvisninger fra FR-ene
- **Problem og hvorfor det betyr noe:** Begrepene «aids», «learning functions», «set», «item», «reference», «source» og «excerpt» brukes om hverandre. Arkitektur og stories må gjette om «item» er et kort, et quizspørsmål eller begge. UJ-1 samler hele reisen, så ingen FR kan spores tilbake til et konkret steg.
- **Forslag:** Legg til en kort Glossary (8–10 begreper), f.eks. «**Source reference** – siden (fysisk sidenummer fra 1) og utdraget som støtter et kort eller en quiz-påstand». Del UJ-1 i to–tre reiser (første gang / revisjon / feil på kilde), og legg «Realizes UJ-n» på hvert FR.

### 4.4 Kjerneløftet «less time» har ingen målbar suksessmåling
- **Alvorlighet:** medium
- **Hvor:** §Product purpose «spend less time extracting key information»; SM-6 «Define timing tasks before full evaluation; no savings … result is established»
- **Problem og hvorfor det betyr noe:** SM-1–SM-5 måler kvalitet, men produktets løfte er tidsbesparelse. Uten en definert oppgave og en terskel vet dere ikke om tesen holder.
- **Forslag:** Sett nå en enkel måling: «Lage egne notater og 10 spørsmål fra T1-dokumentet tar X min uten appen; med appen inkl. kontroll og retting skal det ta høyst 70 % av X.» Terskelen kan justeres etter pilot, men skal stå i PRD-en.

### 4.5 Samle åpne punkter og dekk kostnad og feil i live-modus
- **Alvorlighet:** medium
- **Hvor:** §Validation plan «Actual PDFs, numeric byte/page/text/time limits and evidence remain pending»; §Handoff «Product decisions are resolved»; addendum «Choose and verify byte, page … limits»
- **Problem og hvorfor det betyr noe:** PRD-en sier at produktbeslutningene er avklart, men utestående valg (testdokumenter, grenser, frister, KI-leverandør) ligger spredt. Kostnad per generering, tidsavbrudd og hva som skjer når KI-tjenesten er utilgjengelig eller nøkkelen mangler, er ikke dekket utenom «explain failures» (FR-39).
- **Forslag:** Legg til en kort «Open Questions»-liste med eier og frist, f.eks. «1. Hvilke tre PDF-er brukes for T1–T3? (eier, dato)». Legg til en NFR: «Én generering skal ikke koste mer enn N kr / ta mer enn M sekunder; ved tidsavbrudd vises en feilmelding og siste gyldige innhold beholdes.»

## 5. Mekaniske funn

- FR-1–FR-46 er sammenhengende og unike, og krysshenvisningene jeg sjekket løser seg. Rekkefølgen i dokumentet er ikke numerisk (f.eks. FR-38 under dokumentsesjon), men det er ikke et problem.
- Ingen `[ASSUMPTION]`-merker og ingen Assumptions Index. Det er likevel antakelser i teksten (f.eks. bandene 1–10/15–25/30–40 sider).
- Kun UJ-1; SM-ene henviser til FR-er og er konsekvente. FR-44–FR-46 er ikke dekket av en egen SM.
- Én navngitt person står som brukerroller flere steder (UJ-1, addendum). Vurder en rollebeskrivelse i stedet, siden dokumentet er offentlig.

## 6. Før dere går videre

**Må avklares før UX, arkitektur og epics:**
- Kjerne mot utvidelse, så epics kan prioriteres (4.2).
- Glossar og UJ-kobling (4.3).
- Hvilke tre testdokumenter som brukes, og foreløpige grenser (4.5).

**Kan vente:** eksakte byte-, side- og tidsgrenser, retry-tak og normalisering av utdrag (som arkitekturen eier), samt vurderingsdetaljer og frist.

**Oppfølging av briefen: delvis.** Terskler (9 av 10), språk og detaljnivå, kildeformat (fysisk side + utdrag) og nøkkelfri demo (FR-42) er fulgt opp. Konkrete testdokumenter er fortsatt ikke valgt.

## 7. Refleksjonsspørsmål

1. FR-ene er svært detaljerte på grensetilfeller (FR-18, FR-23, FR-37). Hvilke av disse oppdaget dere selv ved å tenke gjennom appen, og hvilke kom fra KI-forslag som dere godtok uten å spørre om de trengs i v1?
2. Hvordan vil dere teste at et kildeutdrag faktisk støtter et svar (SM-4), og hva gjør dere hvis KI-en foreslår en henvisning som ser riktig ut, men ikke gjør det?

_Vurdert mot kvalitetsrubrikken i bmad-prd. Dette er veiledning, ikke sensur._
