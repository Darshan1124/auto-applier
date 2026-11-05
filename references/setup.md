# One-time setup

## 1. Claude in Chrome

1. Install the **Claude in Chrome** extension from the Chrome Web Store and sign in with the same account used for Claude Code.
2. Keep Chrome open. Restart the Claude session (or run `/mcp`) and confirm the Claude in Chrome tools appear.
3. Allow each site the first time it asks (Overleaf, the job portal).
4. If tools are missing, Claude says so and waits. It does not keep retrying.

## 2. Overleaf account

The user creates the account (or signs in) in Chrome. Claude cannot create accounts or enter passwords. After that, Claude works inside the signed-in session.

## 3. Credentials policy (important)

- **There is no default password in this skill.** A shared default password stored in a repo or a skill is a security hole, and Claude does not type passwords on websites.
- The user creates a strong, unique password for each site.
- To keep them from forgetting it, the user lets **Google Password Manager** (built into Chrome) save it. Chrome shows a "Save password?" prompt after sign-up. Turn on Google Password Manager and sync in Chrome settings. Claude cannot guarantee or perform the saving.
- If a password-manager credential tool is available in the session, Claude may request sign-in details through it. The user approves each item and Claude never sees the secret.
- Never write passwords into any file, note, memory, commit or message.

## 4. Base resume

See Phase 0 in `SKILL.md`. Output: one `base_resume.tex` in the **main folder** (not inside `resume/` or `cover letter/`), built from `templates/base_resume.tex`.

Also build one `base_cover_letter.tex` in the main folder from `templates/base_cover_letter.tex`.

Also create the working folders if missing: `resume/`, `cover letter/`, `resume_pdf/`, `cover letter_pdf/`.

## 5. Publishing this skill to GitHub

The repo contains only dummy data. Before publishing, confirm that:

- `grep -ri` for the user's real name, phone, email, employers and schools finds nothing under this folder.
- `.gitignore` excludes `*.pdf`, `resume/`, `cover letter/`, `resume_pdf/`, `cover letter_pdf/` and any personal base resume.

Then the user can run `git init`, `git add .`, `git commit`, create a GitHub repo and push. Claude must not push without the user asking.
