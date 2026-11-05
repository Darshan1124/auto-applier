# Resume rules (strict)

These were learned the hard way from real compiles. Follow them exactly.

## 1. Format is frozen

Copy `templates/base_resume.tex`. You may edit only the **text inside** these commands:

- Header: name, phone, email, links (when the user has no links, put location and job title on line two instead).
- `\textbf{Label}{: values}` rows in Technical Skills.
- Arguments of `\resumeSubheading{Role}{Dates}{Company}{Location}`.
- `\resumeItem{...}` bullets.
- Education subheadings, the Certifications `\item`, `\resumeProjectHeading{...}{}`.

Never change: `\documentclass`, packages, margins, `\titleformat`, `\newcommand` definitions, spacing commands (`\vspace`), section order (Technical Skills, Experience, Education, Certifications, Projects).

Education has no bullets and no module lists.

## 2. One line per bullet (most common failure)

- A bullet that wraps even by one or two words costs a full extra line and breaks the page budget. Do not write wrapping bullets and do not write "long two-line" bullets. The base format is single-line bullets.
- Target length: about 95 to 117 characters (roughly 440 to 525 points). Short bullets (under about 85% of the width) waste space, so lengthen them with real detail when the page has room.
- The skills rows follow the same limit: each row is one line, about 105 to 115 characters including the bold label.
- Project headings (`bold title | italic tech list`) must also fit on one line.
- Bold text is about 15% wider. A bullet with `\textbf{...}` must be shorter.
- Check with `python scripts/measure_width.py file.tex` (cap 525pt). It is an estimate. The real compile decides.

## 3. One page, no wasted space

Rough budget, calibrated on the dummy template (fills exactly one page):

- 6 skills rows + 27 bullets = 33 body lines with 3 jobs, 2 education entries, 1 certification, 2 projects.
- Each extra job or education entry (a subheading, 2 lines tall) costs about 2.25 body lines.
- 4 jobs means about 30 body lines. 2 jobs allows about 36.

Fit procedure:

1. Draft to the budget. Compile. Read the page counter and view the PDF.
2. **Overflow:** the whole Projects section jumps to page 2 when its first block does not fit, which makes a small overflow look big. Trim, then recompile.
3. **Blank space** of more than about one line at the bottom: add bullets (from the reserve list) and recompile.

Trim order (remove first to last): extra bullets of the oldest or least relevant job, second project's extra bullets, intern or early-career bullets, then the weakest remaining bullet in each role. Never go below 3 bullets for a current role. Never remove the Education or Certifications sections.

Add order (when space remains): a keyword-rich bullet for the current role, then the second most recent role, then project bullets, then a skills-row keyword.

## 4. Keyword strategy

1. Read the whole job description. Extract: title words, hard skills, tools, standards, domain terms, soft skills, verbs. Rank by repetition and by "required" over "preferred".
2. Use the posting's exact phrase where it is true ("root-cause analysis", not "debugging" if the posting says root-cause analysis).
3. Put the highest-value keywords in: the skills rows (rename row labels to match the job's vocabulary), the first bullets of the most recent role, and project tech lists.
4. Re-order bullets so the most relevant come first in each role. Re-order skills so matches come first.
5. A bullet should carry two or three keywords naturally. Do not stuff a list of nouns.
6. Job title in the header line: if the format has one, use a truthful title aligned to the job (for example "Backend Software Engineer" for a backend role).

### Wording: plain first, jargon only when the job uses it

- The **base resume** is written in plain, everyday words: *developed, built, fixed, tested, improved, worked with, set up*. No stacked jargon (for example write "developed backend services", not a string of technical terms).
- When **tailoring**, swap in the job posting's own terms only where they are true for the person. The posting's vocabulary wins over the base resume's plain wording for those bullets.
- Do not use filler nouns or buzzwords the posting never uses.

## 5. Modes (truthfulness)

- **Normal**: only skills, tools and experience present in the base resume. Reword and emphasise.
- **Lethal**: adds job-required skills that are not in the base resume, but only those the user confirms (show the list, wait for yes/no per item). Never invent employers, titles, dates, degrees, certificates, numbers or percentages, clearances, or eligibility. If a metric is not in the base resume, do not add one.

If the user wants a skill the job demands but cannot back it up, suggest honest framing instead ("coursework in X", "exposure to Y") only when it is true.

## 6. LaTeX hygiene

- Escape specials: `\&  \%  \$  \#  \_`. Use `--` for en dash. Use `$|$` as the divider.
- No special Unicode characters. Use plain ASCII.
- Keep dates in one style across the file (`Month YYYY -- Month YYYY`).
- Do not leave `% comments` that contain personal data.

## 7. Final checks (all must pass)

- [ ] Format identical to `base_resume.tex` (diff only content lines).
- [ ] Compile shows `1 / 1`.
- [ ] No wrapped bullet, skills row or project heading in the PDF.
- [ ] Bottom whitespace is at most about one line.
- [ ] Every job requirement that is true for the user appears as a keyword.
- [ ] Nothing in the resume is untrue.
- [ ] `.tex` saved as `resume/<First>_resume_<Company>.tex` and PDF saved as `resume_pdf/<First>_resume_<Company>.pdf`.
