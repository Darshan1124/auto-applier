# auto-applier

### Tired of applying to jobs and answering the same questions again and again?

**This is the solution.** From making a job-specific resume to filling in the application, `auto-applier` does the repetitive work for you. You just give it **the link to the job description**, and it takes care of the rest. You only step in to sign in, answer the legal questions, and press Submit.

---

A [Claude Code](https://claude.com/claude-code) skill that turns a job posting into a **tailored, strictly one-page LaTeX resume** (and a cover letter when the job asks for one), checks it with a real compile in Overleaf, saves the files in a tidy folder layout, and helps you submit the application in Chrome.

You give it a job link. It reads the job description, asks whether to go **Normal** or **Lethal**, rewrites your base resume for that job, verifies the result, and gets the application ready for you to review and submit.

---

## Contents

1. [What it does](#what-it-does)
2. [The strict rules it enforces](#the-strict-rules-it-enforces)
3. [Requirements](#requirements)
4. [Install](#install)
5. [First-time setup](#first-time-setup)
6. [How to use it](#how-to-use-it)
7. [Normal vs Lethal mode](#normal-vs-lethal-mode)
8. [Folder layout and file names](#folder-layout-and-file-names)
9. [Repo contents](#repo-contents)
10. [What Claude will and will not do](#what-claude-will-and-will-not-do)
11. [Passwords and accounts](#passwords-and-accounts)
12. [Troubleshooting](#troubleshooting)
13. [Customising](#customising)
14. [Publishing your own copy](#publishing-your-own-copy)

---

## What it does

1. **Sets up once:** builds a single `base_resume.tex` (and `base_cover_letter.tex`) from your existing resume, asking you for anything missing.
2. **Per job:** reads the job description, tailors the resume to it, and compiles it in Overleaf to prove it is one page with no wrapped lines.
3. **Saves** the `.tex` source and the downloaded PDF into separate folders.
4. **Applies:** opens the application in Chrome, uploads the PDF and fills the form from your base resume, then stops before **Submit** so you stay in control.
5. **Cover letter** (only when the job asks for one or you want one) goes through the same process.

## The strict rules it enforces

These apply to every resume it produces:

- **One page only.** Confirmed by a real compile (Overleaf must show `1 / 1`), never assumed.
- **Same format as your base resume.** Only the content changes. The preamble, margins, section order and spacing are never touched.
- **One line per bullet and per skills row.** A bullet that wraps even by one word costs a whole extra line, so none may wrap.
- **No wasted space.** The page ends within about one line of the bottom margin. If there is room, it adds bullets and keywords. If it overflows, it trims in a fixed order.
- **Keyword dense.** It mirrors the job description's own terms wherever they are true for you.
- **Never fabricates** employers, titles, dates, degrees, certificates, metrics, security clearances or work eligibility, in either mode.

## Requirements

| Requirement | Why |
|---|---|
| [Claude Code](https://claude.com/claude-code) (CLI, desktop app or IDE extension) | Runs the skill |
| **Claude in Chrome** extension (Chrome Web Store), signed in with the same Claude account | Lets Claude work in your real Chrome with your sign-ins |
| Google Chrome, running while you use the skill | Browser for Overleaf and job portals |
| A free **Overleaf** account (you create it) | The real LaTeX compiler used to prove one page |
| Your current resume (PDF, Word, LaTeX or pasted text) | Source for the base resume |
| Python 3 (optional) | Only for `scripts/measure_width.py`, a pre-compile line-width checker |

You do **not** need LaTeX installed locally. Compiling happens in Overleaf.

## Install

### Option A: easiest way, ask Claude to install it

Open Claude Code and say:

> I want the skill from this repo: https://github.com/Darshan1124/auto-applier

Claude will download the repo and put it in your skills folder (`~/.claude/skills/auto-applier`, on Windows `C:\Users\<you>\.claude\skills\auto-applier`) for you. Then start a new session and continue with [First-time setup](#first-time-setup).

### Option B: clone straight into your skills folder

Windows (PowerShell):

```powershell
git clone https://github.com/Darshan1124/auto-applier.git "$env:USERPROFILE\.claude\skills\auto-applier"
```

macOS / Linux:

```bash
git clone https://github.com/Darshan1124/auto-applier.git ~/.claude/skills/auto-applier
```

The folder must be named `auto-applier` and contain `SKILL.md` at its top level.

### Option C: clone anywhere, then copy

```bash
git clone https://github.com/Darshan1124/auto-applier.git
```

Copy the whole cloned folder to `~/.claude/skills/auto-applier` (Windows: `C:\Users\<you>\.claude\skills\auto-applier`), renaming it to `auto-applier`. The folder must contain `SKILL.md` at its top level.

### Option D: project-level install

Put the folder in your project at `.claude/skills/auto-applier` to make the skill available only in that project.

### Verify

Start a new Claude Code session. Type `/` and look for `auto-applier`, or just ask: "use the auto-applier skill". If it is not listed, check that `SKILL.md` sits directly inside the `auto-applier` folder and restart the session.

To update later, run `git pull` inside the skill folder, or ask Claude to "update the auto-applier skill from its repo".

## First-time setup

Do this once, in the folder where you want your job-application files to live (your **working folder**).

1. **Install and connect Claude in Chrome.** Install the extension, sign in, keep Chrome open, and restart your Claude session (or run `/mcp`) so the Chrome tools appear. Allow each site (Overleaf, job portals) the first time it asks.
2. **Create your Overleaf account yourself** and sign in in Chrome. Claude cannot create accounts or type passwords. Tell Claude when you are signed in.
3. **Start the skill** in your working folder and give it your existing resume. Claude will:
   - build **`base_resume.tex`** from `templates/base_resume.tex`, keeping the exact format;
   - build **`base_cover_letter.tex`** from `templates/base_cover_letter.tex`;
   - ask you **one batch of questions** for anything missing (phone, email, links, dates, locations, degrees, certificates). It never guesses a missing fact;
   - create the working folders (below);
   - create an Overleaf project with `main.tex` (base), `companyvise.tex` (per-job resume) and `coverletter.tex`.

After this, setup is finished and every job takes one request.

## How to use it

In your working folder, give Claude a job:

```
/auto-applier apply to https://example.com/jobs/12345
```

or in plain words:

> Use auto-applier to tailor my resume for this job and apply: https://example.com/jobs/12345

You can also paste the job description text if the page needs a login.

What happens next:

1. **Reads the job description** (title, requirements, nice-to-haves, repeated keywords).
2. **Eligibility check.** It warns you about blockers before doing any work: nationality or citizenship limits, security clearance, location, closing date.
3. **Asks Normal or Lethal** (see below).
4. **Tailors** `base_resume.tex` into `resume/<First>_resume_<Company>.tex`.
5. **Pre-checks** every line with `scripts/measure_width.py`.
6. **Compiles in Overleaf**, confirms `1 / 1`, downloads the PDF into `resume_pdf/`, and inspects it for wrapped bullets and blank space. It loops (add bullets or trim) until everything passes.
7. **Cover letter** if requested, with the same checks, into `cover letter/` and `cover letter_pdf/`.
8. **Applies** in Chrome: cookie banner declined, upload from `resume_pdf/`, form filled from your base resume.
9. **Stops** before Submit, shows you a summary, and asks for your approval.

You only step in for: account creation and sign-in, passwords and verification codes, CAPTCHAs, legal or eligibility declarations, and final approval to submit.

## Normal vs Lethal mode

Claude asks every time.

| | Normal | Lethal |
|---|---|---|
| Uses only skills in your base resume | Yes | Yes, plus more |
| Re-orders, rewords and emphasises to match the job | Yes | Yes |
| Pulls every adjacent or transferable skill forward | No | Yes |
| Uses the job's exact phrasing aggressively | Where true | Everywhere true |
| **Proposes extra skills the job needs that are not in your resume** | No | **Yes, but only after you confirm each one** |

In **Lethal** mode Claude shows you the list of proposed skills and adds each one only if you confirm you can speak to it in an interview. Skills you decline are dropped. This is deliberate: skills you cannot back up tend to surface in interviews. In both modes Claude never invents employers, titles, dates, degrees, certificates, numbers, clearances or eligibility.

## Folder layout and file names

Created in your working folder (not inside this repo):

```
<working folder>/
  base_resume.tex        your ONE base resume (main folder, not in a subfolder)
  base_cover_letter.tex  your ONE base cover letter (main folder)
  resume/                tailored .tex files, one per application
  cover letter/          tailored cover letter .tex files
  resume_pdf/            PDFs downloaded from Overleaf
  cover letter_pdf/      PDFs downloaded from Overleaf
```

File names (`<Company>` has spaces replaced with `-`):

| File | Name |
|---|---|
| Resume source | `resume/<First>_resume_<Company>.tex` |
| Resume PDF | `resume_pdf/<First>_resume_<Company>.pdf` |
| Cover letter source | `cover letter/<First>_CL_<Company>.tex` |
| Cover letter PDF | `cover letter_pdf/<First>_CL_<Company>.pdf` |

Example: `resume/Alex_resume_Acme-Corp.tex`.

## Repo contents

```
SKILL.md                         entry point: workflow and hard rules
references/
  setup.md                       Chrome, Overleaf, credentials, publishing
  resume-rules.md                format rules, one-line limits, keyword strategy, modes, trim and add order
  overleaf-workflow.md           pasting, compiling, checking, downloading
  apply-workflow.md              Chrome application flow, stop points, edge cases
  cover-letter.md                cover letter rules and layout
templates/
  base_resume.tex                resume format to copy (dummy data)
  base_cover_letter.tex          cover letter format to copy (dummy data)
scripts/
  measure_width.py               estimates whether bullets and skills rows will wrap
.gitignore                       keeps PDFs, personal folders and build files out of git
```

Everything in `templates/` is **dummy data** (Alex Morgan, Example Corp, Example University). Replace it only in your own working folder, never in the repo.

### Using the width checker yourself

```bash
python scripts/measure_width.py path/to/resume.tex
```

It reports each bullet, skills row and project heading with an estimated width in points, and flags lines over 525 pt as `TOO LONG (will wrap)` and very short lines as wasted space. It is an estimate. The real compile in Overleaf is the final check.

## What Claude will and will not do

**Will:** read job postings, tailor and write LaTeX, compile and inspect in Overleaf, save files, upload your PDF, fill application fields from your base resume, decline non-essential cookies.

**Will not (you do these):**

- create accounts, choose or type passwords, enter 2-factor codes
- solve CAPTCHAs
- answer legal or eligibility declarations (right to work, nationality, security clearance, criminal record, sponsorship, terms and consent)
- answer equal-opportunity or voluntary self-identification questions
- upload identity documents unless you clearly ask for that exact file
- press **Submit** without your explicit approval

## Passwords and accounts

- **There is no default password** in this skill. A shared default password in a repo is a security risk, and Claude does not type passwords on websites.
- Create a **strong, unique password** for each site yourself.
- To avoid forgetting it, let **Google Password Manager** (built into Chrome) save it when Chrome offers "Save password?". Turn on the password manager and sync in Chrome settings. Claude cannot perform or guarantee the saving.
- If a password-manager credential tool is available in your session, Claude may request sign-in details through it. You approve each item and Claude never sees the secret.
- Never put passwords in files, notes, commits or messages.

## Troubleshooting

| Problem | Fix |
|---|---|
| `auto-applier` not listed after install | `SKILL.md` must be directly inside the `auto-applier` folder. Restart the Claude session. |
| Claude says Chrome tools are not available | Install and sign in to the Claude in Chrome extension, keep Chrome open, restart the session or run `/mcp`. |
| A site is blocked or Claude is waiting | Approve the site in the extension prompt. Claude will not work around a refusal. |
| Overleaf preview shows the old PDF after switching files | The first Recompile after changing the main document can be stale. Wait 8 to 10 seconds and press Recompile again. |
| Resume spills onto page 2 | A small overflow can push the whole Projects section over. Claude trims bullets in its fixed order and recompiles. |
| Large blank gap at the bottom | Claude adds bullets and keywords from its reserve list and recompiles. |
| A bullet wraps by a word or two | Claude shortens it. Run `scripts/measure_width.py` to find it. |
| PDF upload rejected by the portal's file picker tool | Keep PDFs in `resume_pdf/` inside the working folder, or upload that one file by hand. |
| Job posting needs login | Sign in yourself in Chrome, or paste the job description text. |
| Browser stops responding | A JavaScript dialog may be open. Dismiss it manually in Chrome. |

## Customising

- **Different resume style:** edit `templates/base_resume.tex` (and the matching rules in `references/resume-rules.md`). The skill's rules assume single-line bullets and one page, so keep those.
- **Different width limit:** change the default cap in `scripts/measure_width.py` (525 pt, calibrated on the dummy template) or pass `--cap <points>`.
- **Different page-fit order:** edit the trim and add order in `references/resume-rules.md`.

## Publishing your own copy

1. Make sure nothing personal is inside the repo: search for your name, phone, email, employers and schools.
2. `.gitignore` already excludes PDFs, `resume/`, `cover letter/`, `resume_pdf/`, `cover letter_pdf/` and `base_resume_personal.tex`.
3. Then:

```bash
git init
git add .
git commit -m "Add auto-applier skill"
git branch -M main
git remote add origin https://github.com/Darshan1124/auto-applier.git
git push -u origin main
```

Pick a license before making the repo public if you want others to reuse it.

---

Use this tool to apply honestly. A tailored resume should present your real experience in the best light, not replace it.
