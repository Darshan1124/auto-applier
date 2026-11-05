# Applying in Chrome

Use Claude in Chrome. The user's real browser and sign-ins are used. Work in a new tab and close it when finished unless the user wants it kept.

## Before you click anything

- Resume (and cover letter if required) is finished and QA-passed.
- Eligibility blockers were already flagged to the user (nationality, clearance, location, closing date).
- The final PDF exists in `resume_pdf/` as `<First>_resume_<Company>.pdf` (and `cover letter_pdf/<First>_CL_<Company>.pdf` if a letter is needed).

## Always stop and hand to the user

- Creating an account, choosing or typing a password, 2-factor codes, verification emails, CAPTCHAs.
- Legal or eligibility declarations: right to work, nationality or citizenship, security clearance, criminal record, sponsorship, terms and consent boxes.
- Equal-opportunity and voluntary self-identification questions.
- Salary expectations and notice period when the user has not told you.
- The final **Submit** or **Apply** button. Summarise what will be sent and ask before pressing.

If the user wants a default or reused answer for any of the above, they state it in chat each time. Do not carry approval between applications.

## Typical flow (Workday-style portals)

1. Open the job URL in a new tab. Decline non-essential cookies.
2. Press **Apply**. A dialog may offer *Autofill with Resume*, *Apply Manually*, *Use My Last Application*.
3. The next step is usually **Create Account / Sign In**. Stop and ask the user to do it. Continue after they confirm they are signed in.
4. Upload the PDF resume. Do not click the upload button (it opens a native file picker). Use `read_page` or `find` to get the file input's ref, then `file_upload`. Only files the user shared with the session or inside the working folder are accepted, which is why the PDFs are kept in `resume_pdf/` and `cover letter_pdf/` inside the working folder. If the path is still rejected, tell the user and ask them to connect the folder or upload by hand.
5. Review the autofilled sections (My Information, My Experience). Correct them to match the resume. Fill missing fields from the base resume. Ask for anything not in it.
6. Answer application questions from the resume and base facts. Leave the declarations above to the user.
7. On the Review page, show the user a summary and ask for explicit approval before submitting.

## Edge cases

| Situation | What to do |
|---|---|
| Extension not connected or tool calls time out | Say so once. Do not retry in a loop. Tell the user how to reconnect (see `setup.md`). |
| Site permission prompt | Tell the user and wait. Do not work around it. |
| Job posting closed or moved | Report it and stop. |
| Posting requires login to read | Ask the user to sign in or paste the description. |
| Autofill from resume mangles dates or titles | Fix each field against the `.tex`, not the other way round. |
| Form asks for a cover letter | Make one with `cover-letter.md`, same QA, PDF in `cover letter_pdf/`. |
| Form field limits (character caps) | Shorten text. Do not truncate mid-sentence. |
| A required document is not available (transcript, ID) | Ask the user. Never upload identity documents unless the user clearly asks for that exact file. |
| JavaScript dialog appears and the browser freezes | Tell the user to dismiss it. Avoid actions that trigger alerts. |
| Several application sites for the same job | Apply only where the user asked. |
| Unexpected extra pages or tangents | Stop and ask. |

## After submitting (only when the user confirmed)

Report what was submitted, the confirmation number or message, and where the `.tex` and PDF files are.
