# Editing the plain-text sources

Edit `source/Student_questionnaire.md` and `source/Answer_key.md` in any text editor. These Markdown files are the source of truth. Do not edit generated XML, JSON, or HTML files directly; rebuilding replaces them.

Question headings identify the lecture, question number, title, and marks:

```markdown
### L1 Q1 Infrastructure pillars — 1 mark

Which set contains the three infrastructure pillars introduced in the lecture?

- A. Deployment, testing, and monitoring
- B. Compute, storage, and network
- C. Development, testing, and production
- D. Applications, users, and source code
```

The corresponding answer-key entry uses the same ID and marks and identifies the correct choice:

```markdown
### L1 Q1 Answer B — 1 mark

Compute executes workloads, storage retains data, and networking connects components.
```

All questions, including scenarios, must use four choices labeled `- A.`, `- B.`, `- C.`, and `- D.` and exactly one correct answer. Each answer-key heading must use `Answer A` through `Answer D`, followed by feedback explaining the correct choice. The converter rejects missing choices, mismatched IDs, and missing correct-answer headings. No free-response questions are supported.

Use normal Markdown paragraphs. Keep questions focused on principles and design decisions: do not require code excerpts, commands, product-specific syntax, or familiarity with a demo. Scenarios describe a situation and ask students to select the best design or explanation. Distractors should represent plausible misconceptions; avoid multiple defensible answers. The converter supports fenced code blocks, but they are not needed for this assessment.

The assessment has a fixed structure: one set per lecture listed in `TITLES` in `scripts/build.py` (currently lectures 1-9), questions 1-10, four choices per question. Q1-Q4 carry 1 mark each, Q5-Q8 carry 2, and Q9-Q10 carry 4, preserving 20 marks per lecture. Question and answer headings must use the em dash shown in the examples. Preserve IDs when changing wording; update the corresponding feedback and source-map entry.

Run `uv run scripts/build.py` after editing. It generates:

- `moodle/lecture-01.xml` through `lecture-09.xml`: prompts, choices, marks, correct answers, and answer explanations.
- `self-check/index.html`: the student self-check page, with answers and explanations hidden until checked.
- `data/questions.json`: all questions, choices, correct answers, marks, and marking guidance in structured form.
- `docs/validation.json`: structural validation results.

You can also use **Terminal > Run Task** in VS Code. Run **Questions: Set up dependencies** first, then select a conversion task. The individual conversion commands are `uv run scripts/build.py --format moodle` and `--format selfcheck`; each validates only its selected exports. Run the all-formats task before committing changes to the sources.

Changing lecture counts, question counts, ordering, or mark totals requires updating the corresponding structure and validation in `scripts/build.py`. Preview the imported quizzes and the self-check page before student use.
