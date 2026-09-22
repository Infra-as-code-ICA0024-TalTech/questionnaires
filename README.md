# ICA0024 lecture questionnaires

**Work in progress.** Questions and grading guidance are open to revision. Exports pass local validation; live Moodle and Microsoft Forms imports still need review.

English assessments for the first three Infrastructure as Code lectures, grounded in the lecture recordings and slides. Questions assess principles, design choices, and codebase organization; they require no code reading, commands, tool syntax, or access to demo repositories.

Each lecture contains **10 single-answer multiple-choice questions worth 20 marks**, including two practical scenarios. Q1-Q4 carry 1 mark each, Q5-Q8 carry 2, and Q9-Q10 carry 4. Every question has four choices and exactly one correct answer. There are 30 questions and 60 marks overall, with no free-response questions. The term **infrastructure pillars** is used throughout.

## Files

| Lecture | Moodle question bank | Microsoft Forms Quick Import |
|---|---|---|
| 1: Infrastructure as Code concepts | [XML](moodle/lecture-01.xml) | [PDF](ms-forms/lecture-01.pdf) |
| 2: Images and machine initialization | [XML](moodle/lecture-02.xml) | [PDF](ms-forms/lecture-02.pdf) |
| 3: Server state and configuration organization | [XML](moodle/lecture-03.xml) | [PDF](ms-forms/lecture-03.pdf) |

The editable sources are [Student_questionnaire.md](source/Student_questionnaire.md) and [Answer_key.md](source/Answer_key.md). The [source map](source/Source_map.md) records lecture review windows and the concepts applied in each scenario. [grading-reference.json](ms-forms/grading-reference.json) provides the same question IDs, choices, correct answers, points, and marking guidance in a structured form; it is **not** a Forms import format.

**Solutions included:** XML files, the answer key, and the grading reference contain solutions. Only the student questionnaire and Quick Import PDFs exclude the answers. Organization members can read this repository under the existing permissions; this is intentional for the work in progress. See [GitHub access](docs/github-access.md).

## Concept glossary

The glossary has moved to the separate [ICA0024 glossary repository](https://github.com/Infra-as-code-ICA0024-TalTech/glossary). It contains the editable Markdown, HTML/PDF/Moodle Glossary exports, its own Python converter, and VS Code tasks. Build and maintain it there; this repository contains the questionnaires and their exporters.

## Import into Moodle

1. Open the course's **Question bank**, then use its **Questions** dropdown to select **Import**.
2. Select **Moodle XML format** and upload one XML file. Enable **Get category from file** if offered. Repeat for the other lectures.
3. Confirm 10 questions in each `ICA0024 / Lecture 01`, `Lecture 02`, and `Lecture 03` category. Preview all questions and choices, including the scenarios.
4. Add a **Quiz** activity for each lecture and add its 10 questions from the question bank. Importing questions alone does not create a student-facing quiz. Set the quiz maximum grade to 20 if you want it to match the question marks.
5. Configure availability, attempts, and review settings. Preview an attempt before making it available to students.

All questions use Moodle **Multiple choice** with one correct answer and automatic grading. Answer explanations are stored as general feedback, whose release depends on the quiz review settings. No Essay or Short answer questions are generated.

The exports use native Moodle question types and require no question-type plugin. Reference: [Moodle XML format](https://docs.moodle.org/en/Moodle_XML_format).

## Import into Microsoft Forms

1. In Forms, select **Quick Import**, upload a lecture PDF from your device, and choose **Quiz**. Repeat for the other lectures.
2. Review all conversion warnings. Confirm exactly **10 choice questions** per lecture, including the scenarios. Disable multiple answers and require one choice per question.
3. Compare prompts and all four choices against the PDF, paying particular attention to question boundaries. Correct any conversion errors.
4. Set the correct choices and points using the answer key or `grading-reference.json`: Q1-Q4 = 1 point each, Q5-Q8 = 2, Q9-Q10 = 4. The PDF omits answers, so the import does not establish the answer key.
5. Check result-sharing settings, preview the quiz, and submit a trial response before sharing it with students.

Microsoft supports local PDF/Word Quick Import for multiple-choice and open-text questions, with a 10 MB file limit. These PDFs contain selectable text, use a single column, and are below that limit. Conversion does not replace review or setup of correct answers and scoring. The PDFs are import sources, not interactive PDF forms.

Reference: [Microsoft Forms Quick Import](https://support.microsoft.com/en-us/forms/convert-a-word-or-pdf-form-or-quiz-to-microsoft-forms).

## Rebuild and validate

### VS Code tasks

Open this repository folder in VS Code, then choose **Terminal > Run Task**:

1. Run **Questions: Set up dependencies** once after cloning (and after dependency changes). This creates `.venv` and installs `requirements.txt`; Python 3.12+ and internet access are required.
2. Edit the Markdown sources, then run **Questions: Convert all formats**, **Questions: Convert to Moodle XML**, or **Questions: Convert to Microsoft Forms PDF**.
3. Run **Questions: Validate exports** to check all existing exports against the current sources without rebuilding them.

**Terminal > Run Build Task** runs the default **Convert all formats** task. Conversion tasks use `.venv` directly and do not reinstall dependencies each time. Tasks include macOS/Linux paths and Windows overrides (using the `py` launcher for setup); no VS Code extension is required. See [.vscode/tasks.json](.vscode/tasks.json) and the [VS Code task documentation](https://code.visualstudio.com/docs/debugtest/tasks).

### Command line

Use Python 3.12 or later:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/build.py
```

Edit the Markdown sources, rebuild, and commit the sources and generated exports together. The [source format guide](docs/source-format.md) explains question IDs, choices, code blocks, and answer-key entries. To check existing exports without rebuilding:

```sh
.venv/bin/python scripts/build.py --check
```

To generate just one format, use `scripts/build.py --format moodle` or `scripts/build.py --format forms` with the same Python environment. A format-specific build validates only that format and leaves the other exports and complete validation report unchanged. Combine `--format` with `--check` to validate just one format. Regenerate all formats before committing a source change so the exports stay consistent.

The build verifies question IDs, marks, XML round trips, correct choices, feedback, grading-reference consistency, PDF question headings and choices, page counts, and file sizes. See [validation.json](docs/validation.json). All 12 PDF pages were also rendered and visually reviewed. **Live imports into Moodle and Forms have not yet been tested.**

The repository excludes recordings, audio, transcripts, transcription models, and runtime environments.
