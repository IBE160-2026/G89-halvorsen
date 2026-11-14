# Impeccable-installasjon

## 2026-11-14 kl. 14:41 — Camilla Halvorsen

### Oppgave

Undersøke offisiell installasjon av Impeccable for Codex og installere skillen prosjektlokalt uten å overskrive BMAD-skills eller konfigurasjon. Fortsette eksisterende UX-arbeid med samme DESIGN.md og EXPERIENCE.md, uten ny oppstart.

### Plan

- Bruke Codex sin `skill-installer`, lese offisielle Impeccable-kilder og la en underagent kontrollere installasjonsvalget uavhengig.
- Ta SHA-256-kontrollsummer av eksisterende BMAD-/konfig-/UX-filer; installere kun den offisielle Codex-skillmappen med kollisjonsvern og kontrollere resultatet.
- Videreføre [eksisterende UX-økt](989-2026-11-14-14-29-00-ai-study-buddy-ux.md) og registrere installasjonen i dens beslutningslogg.

### Resultat

- Offisiell [README](https://github.com/pbakaus/impeccable#installation) anbefaler `npx impeccable install`, men dokumenterer også manuell kopi av `.agents/skills/impeccable` for Codex. Manuell kopi hopper over hooks og ekstra subagenter. Denne metoden er valgt for å avgrense installasjonen til selve skillen. Se også [offisiell oppstartsveiledning](https://impeccable.style/tutorials/getting-started/).
- Installert Impeccable **4.9.1**, 67 filer, fra `pbakaus/impeccable` revisjon `1995764b4936f2bfbf4eb719cb37b384a45ceacb` til `.agents/skills/impeccable/`. Brukte `install-skill-from-github.py` med eksplisitt `--ref`, `--path .agents/skills/impeccable` og prosjektets `.agents/skills` som `--dest`. Installatøren avbryter hvis målmappen finnes; den fantes ikke.
- Gitt den nyinstallerte POSIX-launcheren kjørerettighet etter ZIP-utpakking og kontrollert med `sh -n`. Alle lokale referanser fra SKILL.md finnes; skillnavn, versjon og launcher er kontrollert. Motoren er ikke kjørt som del av filinstallasjonen.
- SHA-256-kontroll umiddelbart etter installasjon bekreftet alle 240 eksisterende beskyttede filer uendret, inkludert BMAD-skills, `_bmad`, AGENTS.md og hele UX-mappen. Ingen `.codex`-konfigurasjon, hooks, globale installasjoner eller produktfiler er lagt til eller endret.
- Deretter lagt én hendelse til eksisterende UX-`.memlog.md` via `memlog.py`: installasjonen er gjennomført og brukerens krav om å fortsette samme UX-økt skal følges. Ny kontroll bekreftet øvrige 239 beskyttede filer uendret; DESIGN.md og EXPERIENCE.md er identiske med før installasjonen.
- Ingen Impeccable `init` eller `document` er kjørt. Eksisterende UX-utkast og arbeidsmappe brukes videre. Neste avklaring er fortsatt brukerens ønsker for utseende/opplevelse og plattform; dette spørsmålet er sendt på nytt etter bekreftet installasjon. Skillen blir tilgjengelig fra neste melding.
- Ingen eksisterende sporede filer var endret før logging. Bare denne sesjonsloggen committes lokalt; ingen push.

### Åpne punkter

- Eksisterende UX-punkt i `issues.md` består. Installasjonen gir ingen nye produktoppgaver; lista er lest og beholdt uendret.
