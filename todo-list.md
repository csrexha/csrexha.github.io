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
- [ ] 🔴 **Unblock the metabolomics manuscript.** It sits with Rex's supervisor; as of
      2026-09-20 Rex expects submission by end of 2026, still not a confirmed date. It
      no longer blocks the dissertation route (route is now monograph, see below), but
      still suppresses the publication record on its own. → `job-application/TODO.md`
- [x] ~~**Settle the dissertation route.**~~ **Done 2026-09-20 — monograph**, Rex's
      unilateral decision, no faculty agreement needed. The metabolomics manuscript is
      still submitted as a standalone paper in parallel. Plan:
      `job-application/07-dissertation/writing-plan.md`. Still no submission date on
      this site, correctly — the plan has only a first-draft target
      (2026-12-31), not a defense date.
- [ ] **Document the VAST-AF contribution.** Rex is 3rd of 4 authors in
      *American Heart Journal* 2024 and the role is unrecorded, so the page says only
      "statistical consulting" and must not say more until
      `01-facts.md#vast-af` records what he actually did. Checked 2026-09-20: the
      paper itself has no author-contributions section to verify against (unlike OHCA,
      which does and is now resolved) — still open, no new evidence found.

## Verification rules that never expire

- [ ] **Verify the publication record against PubMed before changing it.** The record
      understated itself for over a year — VAST-AF was missing entirely until
      2026-08-31. Query `Ha CSR[Author]`; the author list is the evidence, not the CV.
- [ ] **Re-derive the audit list from the current T4 table** in `02-claims.md` on every
      run. The list grows. A passing audit against a stale list is worse than no audit.
- [ ] **German connective prose needs Rex's correction pass.** The claim sentences are
      the vetted `DE:` lines; the text between them is not his own. Standing rule, never
      closes — but a pass on 2026-09-20 found and fixed four **content** errors, not
      prose (both languages): "seit 2023"/"2023 – present" and
      "berufsbegleitend"/"part-time" for the doctorate (both withdrawn on the claims
      side), "Forschungsgruppen"/"research groups" (should be "Forschungsprojekte"/
      "research projects"), and DE-only "Lehrbeauftragter" (should be "Dozent",
      corrected in the claims library 2026-09-18). Rendered, audited clean, not yet
      pushed — see next step.

## Open decisions

- [ ] **Custom domain** — undecided. Changing the URL after it is shared loses links.
- [ ] **Favicon** — none set.
- [ ] **Make the §11 audit executable** (`scripts/audit.py` + a CI step that fails the
      build). An audit that cannot block a push is decorative.

## Knowledge-base follow-ups this site created

- [x] ~~**Add VAST-AF to every CV** in `job-application/01-documents/cv/`.~~
      **Superseded 2026-09-20** — Rex declined a blanket add (per-application decision,
      not a standing one). Instead: `job-application/02-personal-wiki/profile/
      05-publications.md`, a picking-list of every manuscript for future CV/site
      decisions. IMPETUS got the same treatment.
- [x] ~~**Update every document** to the resolved email and GitHub handle.~~
      **Checked 2026-09-20** — every editable document already consistent; only
      read-only historical `.docx` files in `job-application/01-documents/` carry old
      variants, correctly untouched.
- [x] ~~**`job-application/02-personal-wiki/profile/` is untracked in git.**~~ **False,
      checked 2026-09-20** — it has full commit history (`git log` confirms). This item
      was already stale when written.
