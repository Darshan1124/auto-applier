---
name: auto-applier
description: Tailor a strict one-page LaTeX resume (and optional cover letter) to a specific job posting from the user's saved base resume, verify it in Overleaf, save the .tex file, and drive the job application in Chrome. Use when the user wants to apply to a job, tailor or refresh a resume, set up their base resume, or gives a job URL or job description.
---

# auto-applier

Turns a job posting into a tailored, one-page, ATS-keyword-dense LaTeX resume (plus a cover letter if the job asks for one), then helps submit the application. The resume format is fixed. Only the content changes.

Detail lives in `references/`. Read the matching file before each phase:

| Phase | Read |
|---|---|
| First-time setup, accounts, credentials | `references/setup.md` |
| Writing or tailoring the resume | `references/resume-rules.md` |
| Compiling, checking, downloading in Overleaf | `references/overleaf-workflow.md` |
| Filling the application form in Chrome | `references/apply-workflow.md` |
| Cover letter | `references/cover-letter.md` |

Templates and helper script: `templates/base_resume.tex` and `templates/base_cover_letter.tex` (dummy data, the exact formats to copy), `scripts/measure_width.py` (line-width checker).

## Hard rules (never relax these)

1. **One page.** Confirmed by a real compile (Overleaf shows `1 / 1`), never assumed.
2. **Same format as the base resume.** Do not touch the preamble, margins, custom commands, section order or spacing. Change content only.
3. **Every bullet and every skills row fits on one line.** No bullet may wrap, not even by one word, because a wrapped word costs a whole extra line. Use `scripts/measure_width.py`, then verify in the compiled PDF.
4. **No wasted space.** The page ends within about one line of the bottom margin. If there is room, add bullets and keywords until it is full. If it overflows, trim by the order in `resume-rules.md`.
5. **Keyword dense.** Mirror the job description's exact terms wherever they are true for the user.
6. **Never fabricate** employers, job titles, dates, degrees, certificates, metrics, security clearances or work-eligibility. This holds in both modes.
7. **Keep file types apart.** Only `.tex` goes in `resume/` and `cover letter/`. PDFs downloaded from Overleaf go in `resume_pdf/` and `cover letter_pdf/`. The single base resume lives in the main folder, not in any subfolder.
8. **Claude never creates accounts or types passwords**, never solves CAPTCHAs, and never answers legal or eligibility declarations. The user does those. Claude stops before the final Submit and asks first.

## Workspace layout (create if missing, in the user's working folder)

```
<workdir>/
  base_resume.tex        the ONE base resume (main folder, never inside a subfolder)
  base_cover_letter.tex  the ONE base cover letter (main folder)
  resume/                <First>_resume_<Company>.tex       .tex only, one per application
  cover letter/          <First>_CL_<Company>.tex           .tex only, when requested
  resume_pdf/            <First>_resume_<Company>.pdf       PDFs downloaded from Overleaf
  cover letter_pdf/      <First>_CL_<Company>.pdf           PDFs downloaded from Overleaf
```

`<Company>` is the company name with spaces replaced by `-` (for example `Acme-Corp`). Create any missing folder at the start of the first run.

## Phase 0: one-time setup (skip if `base_resume.tex` exists in the main folder)

1. Check Claude in Chrome tools are available (see `setup.md`). If not, tell the user how to connect it and wait.
2. The **user creates their own accounts** wherever one is required (Overleaf first, and later any job portal) and signs in in Chrome. Claude cannot do this part. Ask them to say when they are signed in.
3. Ask for their existing resume (PDF, Word, LaTeX or pasted text) and read it.
4. Build `base_resume.tex` **in the main folder** by pouring their content into `templates/base_resume.tex`. Also build `base_cover_letter.tex` in the main folder from `templates/base_cover_letter.tex`, using the same personal details. Keep every format rule. Use the dummy file as the reference for bullet length and section shape.
5. Collect missing details in ONE batch of questions (phone, email, links, dates, locations, degrees, certificates). Never guess a missing fact.
6. Create the Overleaf project (or ask the user to) with three files: `main.tex` (base), `companyvise.tex` (per-job resume), `coverletter.tex`. Paste the base into `main.tex`.

## Phase 1: per job

1. **Get the job description.** Open the URL, or accept pasted text. Read it fully. Note title, company, location, requirements, nice-to-haves, repeated keywords.
2. **Eligibility pre-check.** Flag blockers before doing any work: nationality or citizenship limits, security clearance, work-permit, location, closing date. Tell the user and let them decide.
3. **Ask the mode** with a question (options below). Always ask. Never default silently.
4. **Tailor** `base_resume.tex` into `resume/<First>_resume_<Company>.tex` following `resume-rules.md`.
5. **Verify** with the QA loop (below) until every check passes.
6. **Cover letter** only if the posting asks for one or the user wants it. Tailor `base_cover_letter.tex` into `cover letter/<First>_CL_<Company>.tex` following `cover-letter.md`, same QA.
7. **Apply.** Follow `apply-workflow.md`. Download the final PDF from Overleaf into `resume_pdf/` (and `cover letter_pdf/`) and upload from there. Stop before Submit.

### Modes

- **Normal**: use only skills and experience that are in the base resume. Re-order, re-word and emphasise to match the job. Keywords are limited to things the user has actually done or used.
- **Lethal**: maximum alignment. Everything in Normal, plus aggressive keyword coverage: pull every adjacent or transferable skill forward, use the job's exact phrasing, and **propose** extra skills the job requires that are not in the base resume. Show the user the proposed list first. Add each one only if the user confirms they can speak to it in an interview. Skills the user declines are dropped. Lethal still never invents employers, titles, dates, degrees, certificates, metrics, clearance or eligibility.

## QA loop (repeat until all pass)

1. Run `python scripts/measure_width.py <file>.tex`. Fix every line marked `TOO LONG`.
2. Paste into Overleaf, set the main document, compile. Page counter must read `1 / 1`.
3. Download the PDF and view it. Check: no bullet or skills row wraps, format identical to the base, no stray blank gap, bottom whitespace at most about one line.
4. Too much blank space: add bullets or keywords from the reserve list and recompile. Overflow: trim in the documented order and recompile.
5. Check keyword coverage against the job description once more.
6. Save the final `.tex` to `resume/` and the final PDF to `resume_pdf/`.

## When information is missing

Ask the user. Do not guess a phone number, date, employer, grade or certificate. Batch questions.
