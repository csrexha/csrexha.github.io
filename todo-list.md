# Open items — csrexha.github.io

Standing reminders and unresolved work for the website. Shown at the start of every
session by the `SessionStart` hook in `.claude/settings.json`.

Keep this file short. Close items when they are done; do not let it become a log.

## 🔴 Blocking — must be settled before the affected content is trusted

- [x] ~~**Name the journal for the metabolomics manuscript.**~~ **Void 2026-09-01** —
      there is no journal. A grill session established the manuscript was **never
      submitted**; the question presupposed an event that did not happen. The site said
      "Under review, 2026" / "In Begutachtung, 2026" in both languages and now says
      **in preparation**. → `02-claims.md` T4 table
- [ ] 🔴 **Unblock the metabolomics manuscript.** It sits with Rex's supervisor with no
      foreseeable submission date. This is one problem wearing two hats: it suppresses the
      publication record *and* blocks the cumulative dissertation route, which is why the
      PhD submission date had to come off this site. Nothing on the publications page
      improves until this moves. → `04-gaps.md § C`
- [ ] **Settle the dissertation route.** Cumulative or monograph, and whether a switch
      needs faculty agreement. Until it is settled the CV pages carry no submission date,
      which is correct but weaker than a decided plan. → `04-gaps.md § C`
- [ ] **Document the VAST-AF contribution.** Rex is 3rd of 4 authors in
      *American Heart Journal* 2024 and the role is unrecorded, so the page says only
      "statistical consulting" and must not say more until
      `01-facts.md#vast-af` records what he actually did.

## Verification rules that never expire

- [ ] **Verify the publication record against PubMed before changing it.** The record
      understated itself for over a year — VAST-AF was missing entirely until
      2026-08-31. Query `Ha CSR[Author]`; the author list is the evidence, not the CV.
- [ ] **Re-derive the audit list from the current T4 table** in `02-claims.md` on every
      run. The list grows. A passing audit against a stale list is worse than no audit.
- [ ] **German connective prose needs Rex's correction pass.** The claim sentences are
      the vetted `DE:` lines; the text between them is not his own.

## Open decisions

- [ ] **Custom domain** — undecided. Changing the URL after it is shared loses links.
- [ ] **Favicon** — none set.
- [ ] **Make the §11 audit executable** (`scripts/audit.py` + a CI step that fails the
      build). An audit that cannot block a push is decorative.

## Knowledge-base follow-ups this site created

- [ ] **Add VAST-AF to every CV** in `documents/cv/` — four published papers, not three.
- [ ] **Update every document** to the resolved email (`hachungshingrex@gmail.com`) and
      GitHub handle (`csrexha`); existing files use a mix of both.
- [ ] **`documents/profile/` is untracked in git.** The single source of truth has no
      version history. For files whose purpose is catching drift, that is worth fixing.
