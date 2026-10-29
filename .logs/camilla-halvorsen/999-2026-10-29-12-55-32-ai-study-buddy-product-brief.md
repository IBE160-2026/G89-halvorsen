# AI Study Buddy – Product Brief

## 2026-10-29 kl. 12:55 — Camilla Halvorsen

### Oppgave

Revidere eksisterende Product Brief etter faglærerens tilbakemelding med BMAD, samordne støttedokumentene og dokumentere beslutninger og videre arbeid.

### Plan

- Lese brief, [faglærerens tilbakemelding](../../_bmad-output/planning-artifacts/briefs/brief-G89-halvorsen-2026-09-26/tilbakemelding-product-brief.md), beslutningshistorikk og relevante skills.
- Gjennomgå forslag med brukeren, oppdatere eksisterende dokumenter og kontrollere samsvar uten å utvide omfanget.

### Resultat

- Oppdatert [product-brief.md](../../_bmad-output/planning-artifacts/briefs/brief-G89-halvorsen-2026-09-26/product-brief.md) på engelsk med eksisterende struktur: konkret studiesituasjon med omtrent 40 lysark og primærbruker som bachelorstudent i IT-relaterte emner ved Høgskolen i Molde.
- Vedtatt kun tekstbaserte PDF-er i v1; ingen .txt eller OCR. Kildevisning bruker filnavn, PDF-siderekkefølge fra 1, utdrag og «View source». Utdragskontroll gir advarsel, uten garanti om faglig korrekthet.
- Vedtatt bokmål/engelsk uavhengig av kildespråk. Brief/Detailed gjelder bare sammendrag. T1–T3 er kategorier, ikke valgte dokumenter; planlagt 12 sammendragskombinasjoner og separate flashcard-/quiztester.
- Konkretisert planlagte kvalitetskrav med 9 av 10 for flashcards, quizfasit og støttende referanser, manuell sammendragskontroll og forståelige feil ved ugyldige filer eller skannede PDF-er uten uttrekkbar tekst.
- Vedtatt merket demo med lagrede studiehjelpemidler uten privat API-nøkkel og separat testing av ekte API-generering. Gemini 2.5 Flash er foreløpig kandidat; fremdriftslagring er valgfri fase 2.
- Samordnet [.memlog.md](../../_bmad-output/planning-artifacts/briefs/brief-G89-halvorsen-2026-09-26/.memlog.md) og [addendum.md](../../_bmad-output/planning-artifacts/briefs/brief-G89-halvorsen-2026-09-26/addendum.md). Tidligere loggoppføringer er bevart; gjeldende beslutninger, åpne spørsmål og ikke-vedtatte anbefalinger er skilt.
- BMAD-gjennomgangen vurderte briefen som tilstrekkelig grunnlag for PRD. Dokument- og formateringskontroller er gjennomført; ingen applikasjonstester eller dokumenterte tidsbesparelser foreligger. Ingen applikasjonskode er endret. De tre BMAD-dokumentene er ikke committet i denne økten; bare sesjonsloggen og issues.md inngår i loggcommiten. Ingen push.

### Åpne punkter

- PRD: konkretisere testtilfeller, utvalg, sammendragsvurdering, quizretting, dokumentgrenser, feilmeldinger, demo og håndtering/sletting av opplastet materiale.
- Avklare vurderingsforslag: samlet kontroll av fasit og støttende referanse på samme element, utdragskontroll på oppgitt side og gjenbruk av quizflyt for spørsmål etter sammendrag. Dette er ikke vedtatte krav.
- Før testing: velge konkrete T1–T3-PDF-er, delbart demodokument og manuelle sammenligningsoppgaver; avklare delingsrettigheter og gjennomføre planlagte tester.
- Architecture/README: velge modell og PDF-bibliotek, planlegge kostnad, sikker nøkkelhåndtering, .env.example, demoimplementasjon og lokal oppstart.
- Etter testet kjerne: vurdere valgfri fase-2-fremdriftslagring. Bekrefte eksakt innleveringsdato.
