# Overleaf workflow (via Claude in Chrome)

Overleaf is used as the real compiler, because only a real compile proves one page and no wrapped lines.

## Project layout

One Overleaf project per user, with three files:

- `main.tex`: the base resume (never overwrite it with a tailored one).
- `companyvise.tex`: the current job's tailored resume.
- `coverletter.tex`: the current job's cover letter.

The user must already be signed in to Overleaf in Chrome. Claude never types credentials.

## Loading browser tools

Load the Chrome tools in one ToolSearch call, then call `tabs_context_mcp` with `createIfEmpty: true`. Open the project in the session's own tab and prefer `browser_batch` for sequences.

## Pasting a file into the editor

Typing into the editor is unreliable (auto-closing brackets duplicate braces). Replace the document through CodeMirror instead:

1. Click the file's tab so it is the active editor.
2. Run this with `javascript_tool` (the text goes inside `String.raw` so backslashes survive; it must not contain a backtick or `${`):

```js
const txt = String.raw`...entire .tex file...`;
const v = document.querySelector('.cm-content').cmView.view;
v.dispatch({changes:{from:0, to:v.state.doc.length, insert:txt}});
v.state.doc.length + ' (expected ' + txt.length + ')'
```

3. Confirm the two numbers match. If the file was non-empty and you did not mean to overwrite it, stop.

## Choosing which file compiles

Overleaf compiles the project's **main document**.

1. File menu (top left) then **Settings** then **Compiler** tab.
2. Find the "Main document" dropdown with `find`, set it with `form_input` to `companyvise.tex` (resume) or `coverletter.tex` (letter).
3. Close the dialog, press **Recompile**.

Gotchas:

- The first Recompile after switching the main document can show the old PDF. Wait about 8 to 10 seconds. If the preview did not change, press Recompile again.
- Menu positions shift. Take a screenshot before clicking coordinates.

## Verify

- The page counter next to the preview must read `1 / 1`.
- Screenshot or zoom the preview for a quick look, then do the real check by downloading and viewing the PDF.

## Download and name

1. Click the download icon next to Recompile.
2. The file lands in the user's Downloads folder as `<ProjectName>.pdf` (or `<ProjectName> (1).pdf` if one exists). Identify it as the newest PDF by timestamp.
3. Rename it to `<First>_resume_<Company>.pdf` or `<First>_CL_<Company>.pdf`.
4. Move it into the workspace: resumes to `resume_pdf/`, cover letters to `cover letter_pdf/` (create the folder if missing). Do not put PDFs in `resume/` or `cover letter/`, which hold only `.tex`.
5. Read the PDF from there and run the QA checks (wrapped lines, whitespace). Upload to job portals from there too.

## Recompile loop

If QA fails, edit the local `.tex`, re-paste into Overleaf, recompile, download again, and overwrite the PDF in `resume_pdf/` (or `cover letter_pdf/`) with the corrected one so only the final version remains. Delete other files only if the user asks (send to Recycle Bin, never hard-delete).
