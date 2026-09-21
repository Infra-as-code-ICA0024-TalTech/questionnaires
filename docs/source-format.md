# Editing the plain-text sources

Edit `source/Student_questionnaire.md` and `source/Answer_key.md` in any text editor. These Markdown files are the source of truth. Do not edit generated XML, PDF, or JSON files directly; rebuilding replaces them.

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

For explanations and scenarios, use a descriptive answer-key heading instead of `Answer B` and put the grading rubric in the body:

```markdown
### L1 Q5 Version control — 2 marks

Award 1 mark each for two benefits connected to reliable delivery.
```

Use normal Markdown paragraphs. Keep questions focused on principles and design decisions: do not require code excerpts, commands, product-specific syntax, or familiarity with a demo. Practical scenarios should describe a situation and ask students to justify their reasoning. The converter supports fenced code blocks, but they are not needed for this assessment. Numbered scenario subparts become lettered subparts in the Forms PDFs to help the importer keep each scenario together.

The current assessment has a fixed structure: lectures 1-3, questions 1-10, four multiple-choice questions first, four explanations next, and two scenarios last. Choices must use `- A.`, `- B.`, `- C.`, and `- D.`. Question and answer headings must use the em dash shown in the examples. Preserve IDs when changing wording; update the corresponding rubric and source-map entry.

Run `python scripts/build.py` from the repository's Python environment after editing. It generates:

- `moodle/lecture-01.xml` through `lecture-03.xml`: prompts, choices, marks, correct answers, and grading rubrics.
- `ms-forms/lecture-01.pdf` through `lecture-03.pdf`: questions only, for Quick Import.
- `ms-forms/grading-reference.json`: an instructor reference generated from the same sources.
- `docs/validation.json`: structural validation results.

You can also use **Terminal > Run Task** in VS Code. Run **Questions: Set up dependencies** first, then select a conversion task. The individual conversion commands are `python scripts/build.py --format moodle` and `python scripts/build.py --format forms`; each validates only its selected exports. Run the all-formats task before committing changes to the sources.

Changing lecture counts, question counts, ordering, or mark totals requires updating the corresponding structure and validation in `scripts/build.py`. Changes that increase question length may require adapting PDF page breaks. Render and review changed PDFs, and preview the imported quizzes before student use.

## Glossary source

Edit `source/Glossary.md`. Use one `#` title followed by an introduction, `## Lecture 1: ...` through `## Lecture 3: ...` headings, and a `### Term` heading followed by its definition for each entry. Keep definitions in prose paragraphs; inline Markdown such as emphasis is supported. Term names must be unique. The exporter sorts entries alphabetically within each lecture.

Run `python scripts/build.py --format glossary` to generate `glossary/glossary.html`, `glossary/glossary.pdf`, and `glossary/moodle-glossary.xml`. The same task is available as **Glossary: Convert all formats** in VS Code. Add `--check` to detect stale exports. The all-formats build also generates the glossary. The XML targets Moodle's Glossary activity and preserves lecture categories; it is separate from question-bank XML.
