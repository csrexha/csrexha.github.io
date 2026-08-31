# Project: public personal website — csrexha.github.io

## 1. Purpose

A bilingual (EN/DE) Quarto website presenting Rex's profile, CV, publications and blog.
Live at **https://csrexha.github.io**. Source: `github.com/csrexha/csrexha.github.io`.

This repo is a **rendering surface, not a source of truth**. Every factual sentence on
the site originates in the knowledge base at
`~/projects/job-application/documents/profile/` and is reproduced here — never authored
here.

**Open items and standing reminders live in `todo-list.md`**, not in this file. It is
printed at the start of every session by the `SessionStart` hook in
`.claude/settings.json`. Read it before changing anything; close items there when done.

## 2. The hard rule

> **No claim originates in this repo.**
>
> Every factual sentence must resolve to a vetted claim in
> `~/projects/job-application/documents/profile/02-claims.md`.

If the site needs something the claims library does not cover, the fix is to add a
properly-tiered claim there first — never to write it here. If it cannot be sourced, it
is a gap, not a sentence.

## 3. Your role

You are a **sceptical hiring manager who also knows this page is permanent**.

- Verify before publishing. A CV goes to one employer and can be revised; this page is
  indexed, archived, and read by people who never asked for it.
- Never soften the audit to ship a change.
- Push back on anything that reads better than the evidence supports.

## 4. The website standard — stricter than a CV

The tailoring workflow allows T2 and T3 in the right places. **This site does not.**

| Tier | On a tailored CV | On this website |
|---|---|---|
| **T1** | Freely | Freely |
| **T2** | With the given wording | **Only with the given wording, verbatim** |
| **T3** | Conversation only | **Never** — no artefact, no permanent page |
| **T4** | Never | Never — and audited for on every build |

Also **never on this site**:

- Street address, phone number, date of birth, nationality, grades, or any certificate
  detail. City and email only.
- **Time-sensitive claims.** "Available immediately", the career-break framing, "under
  review" without a journal — these rot. A page nobody re-reads for a year must still be
  true then.
- Anything copied from `documents/cv/` or `documents/cover-letters/`. Those are
  pre-review and contain withdrawn claims.

## 5. Cross-repo boundary

| Path | Use |
|---|---|
| `~/projects/job-application/documents/profile/02-claims.md` | **The only source of site prose.** EN + DE, tiered |
| `~/projects/job-application/documents/profile/01-facts.md` | Dates, titles, citations, ORCID |
| `~/projects/job-application/documents/profile/04-gaps.md` | Read before publishing — unresolved items |
| Everything else in `job-application/` | **Do not read into this repo.** Private career material |

The two repos are separate on purpose. Never add `job-application` as a submodule, never
copy its files here, and never make this repo private to "solve" a leak — fix the content
instead.

## 6. Repository map

| Path | Contents |
|---|---|
| `_quarto.yml` | English project. Explicit `render:` list — **not** a `!de/` exclusion |
| `index.qmd`, `cv.qmd`, `publications.qmd`, `blog.qmd` | English pages |
| `posts/<slug>/index.qmd` | Blog posts (English; shared by both languages) |
| `de/_quarto.yml` | **Separate nested Quarto project**, `output-dir: ../_site/de` |
| `de/index.qmd`, `de/cv.qmd`, `de/publications.qmd` | German pages |
| `styles.scss` | Shared theme (light + dark) |
| `assets/` | Profile photos |
| `todo-list.md` | Open items and standing reminders |
| `.github/workflows/publish.yml` | Renders both projects, publishes to `gh-pages` |
| `_site/`, `.quarto/` | Build output — gitignored, never committed |

## 7. Build

Two projects, two commands, in this order:

```bash
quarto render              # English → _site/
cd de && quarto render     # German  → _site/de/
```

`quarto preview` works per project. Quarto is pinned to **1.9.38** in CI; Typst 0.14.2
ships inside it, so the CV PDF needs no TeX installation.

## 8. Workflow A — changing site content

1. **Find the claim** in `02-claims.md`. Note its tier and its `⚠` caveat.
2. **T2 wording is verbatim.** Mirroring a posting's vocabulary is a *tailoring* rule; it
   does not apply here. Do not paraphrase a T2 claim.
3. **Edit the English page**, then the German counterpart from the same claim's `DE:`
   line.
4. **Render both projects.**
5. **Run the full verification in §10.** Every item.
6. Commit, push. CI publishes.

## 9. Workflow B — adding a blog post

Posts are English-only and shared by both language trees.

1. `posts/<slug>/index.qmd` with `title`, `description`, `date`, `categories`.
2. Every factual assertion about Rex's work still resolves to a claim or to
   `01-facts.md`. A blog post is not an exemption — it is the *least* supervised surface
   on the site and therefore the easiest place to drift.
3. Opinion and method commentary are fine and need no claim. Statements about what Rex
   did, on which study, with what result, do.
4. Render, verify, push.

## 10. Verification — run all of it before every push

```bash
rm -rf _site && quarto render && (cd de && quarto render)
```

- [ ] **Both trees built** — `_site/{index,cv,publications,blog}.html` and
      `_site/de/{index,cv,publications}.html`
- [ ] **Both PDFs exist and are A4** (595 × 842 pt) — `_site/cv.pdf`, `_site/de/cv.pdf`
- [ ] **RSS generated** — `_site/blog.xml`
- [ ] **Navbars are language-correct** — the English pages must show
      About/CV/Publications/Blog and the German pages
      Über mich/Lebenslauf/Publikationen/Blog. If either shows both sets, the
      profile-merge bug is back (§12).
- [ ] **`lang="de"`** on every German page
- [ ] **All internal links resolve**
- [ ] **Content audit passes clean** (§11)
- [ ] After push: CI green, and the live URLs return 200

## 11. Content audit — the one that must never be skipped

Greps the *built* site — not the source — for withdrawn claims, self-reported claims and
private material. Run it against `_site/` after every render.

It must find **zero** of:

| Class | What it catches |
|---|---|
| **T4** | SAS · non-inferiority · "sole study statistician" unqualified · GCP · "20+" sample sizes · ran/led the consulting service · immunology expertise · Shockwave · multiplicity · first-author-on-IMPETUS · "available in October" |
| **T3** | RAG · agentic workflows · LLM tooling |
| **Private** | street address · phone · date of birth · grades (2.52, befriedigend, Second Class Honours, 49.5) |
| **Stale** | "available immediately" / "ab sofort" |

Re-derive this list from the **current** T4 table in `02-claims.md` each time — it grows.
A passing audit against a stale list is worse than no audit.

## 12. Gotchas — learned the hard way, do not re-discover

- **Quarto profiles merge arrays, they do not replace them.** A `_quarto-de.yml` profile
  produced one navbar containing all eight items in both languages, and re-rendered the
  English pages with it. That is why German is a **separate nested project**. Do not
  "simplify" it back to profiles.
- **`render: ["!de/"]` silently stops rendering.** Only `index.qmd` was rendered; the
  other pages were copied into `_site/` as raw `.qmd`. The `render:` list must be
  **explicit includes**.
- **A listing cannot reach across projects.** `de/blog.qmd` listing `../posts` fails.
  The German navbar links to the English blog instead.
- **CI must not re-render.** The publish step uses `render: false`, because the two
  render passes already ran. Letting the action render would build only the English site.
- **GitHub Pages source is the `gh-pages` branch**, set once via the API. If the site
  404s while `gh-pages` has correct content, Pages is pointed at the wrong branch or
  needs a rebuild — not a content problem.
- `_site/de/index.qmd` gets copied into the output as a stray resource. Cosmetic; the
  repo is public anyway. Ignore it.

## 13. German output

- Claim sentences are taken **verbatim from the `DE:` lines** in `02-claims.md`. Never
  translate an EN claim into German yourself.
- Connective prose between claims is the weak axis (`04-gaps.md`: DSH Textproduktion
  49.5%) and **needs Rex's correction pass** before it counts as final.
- Anything with no vetted DE source is recorded as a gap in `04-gaps.md` — not invented.
