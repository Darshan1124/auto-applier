# Cover letter

Write one only when the posting asks for it or the user wants it. Save the `.tex` as `cover letter/<First>_CL_<Company>.tex` and the PDF downloaded from Overleaf as `cover letter_pdf/<First>_CL_<Company>.pdf`.

## Start from the base

Copy `base_cover_letter.tex` from the main folder (built from `templates/base_cover_letter.tex`, which has dummy data and the exact layout). Change only the text: date, recipient, role and reference number, and the body paragraphs.

## Rules

1. Exactly **one page**. Confirm `1 / 1` in a real compile (Overleaf main document set to `coverletter.tex`).
2. Four to five short paragraphs, about 300 to 380 words, plain and specific.
3. Use only facts from the base resume and what the user told you. No invented achievements, numbers or employers.
4. Mirror the job's own keywords in the body. Name the role and any job reference number in the subject line.
5. Be honest about gaps in one sentence and show intent to close them. Do not claim skills the user lacks.
6. No filler openers ("I am thrilled to...") and no generic closers. End with a specific, polite call to action.
7. Same header style as the resume (name in small caps, one contact line).
8. Leave eligibility and legal statements out of the letter.

## Layout (fixed)

`\documentclass[letterpaper,11pt]{article}`, `geometry` with 1in margins, `\parindent 0pt`, `\parskip 9pt`, `\pagestyle{empty}`, then: centered name and contact line, date, recipient block, bold "Re:" line, greeting, body paragraphs, sign-off, name. Only change the text.

## Structure

1. Role, company, and one sentence saying why the user's degree and strengths fit it.
2. Education and technical grounding mapped to the posting's requirements.
3. Work experience mapped to the posting's duties (documentation, collaboration, risk, tools).
4. Honest gap and growth statement, plus working style in one line.
5. Thanks and an invitation to discuss.

## QA

Compile, view the PDF, confirm one page with the signature block on the page, and no overfull lines. Save the `.tex` in `cover letter/` and the PDF in `cover letter_pdf/`.
