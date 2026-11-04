# SE Advanced Text Analysis — Text as Data (2026)

This repository contains the slides, notebooks, and small datasets used in **SE Advanced Text Analysis**. We use them to examine how choices about preprocessing, text representation, and modeling change what we can measure and conclude from text.

## Course guide

The practical work follows a recurring sequence:

1. **Define the question and concept.** Decide what a text-based measure should capture.
2. **Represent the text.** Tokenize documents and build features such as word counts, n-grams, and TF-IDF.
3. **Compare choices.** Hold the corpus fixed while changing one preprocessing or representation setting.
4. **Inspect the result.** Look at terms, document similarities, and examples from the original texts.
5. **Explain the trade-off.** Connect numerical differences back to the research question and possible measurement errors.

The repository currently contains the **Day 1 materials**. The slides introduce text as data; the guided notebook works through representation choices; and the exercise asks you to change a small part of the code and interpret the difference. Later course materials can be added to the same structure.

| Start here | Purpose |
| --- | --- |
| [`day1/main.pdf`](day1/main.pdf) | Day 1 lecture slides |
| [`materials/notebooks/day_1_representation.ipynb`](materials/notebooks/day_1_representation.ipynb) | Guided example: tokenization, document-term matrices, weighting, and similarity |
| [`materials/notebooks/day_1_representation_exercise.ipynb`](materials/notebooks/day_1_representation_exercise.ipynb) | Student exercise: change a representation and discuss the result |
| [`materials/data/`](materials/data/) | CSV datasets used by the notebooks; see the [data guide](materials/data/README.md) for sources |
| [`day1/main.tex`](day1/main.tex) | Editable Beamer source for the slides; LaTeX is optional for students |

## First-time setup

Use **Python 3.10 or newer**. Open a terminal in the repository's top-level folder, the one containing this README and the `materials` folder. You need an internet connection to install Python packages and the optional spaCy model.

### 1. Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Check that the active Python is version 3.10 or newer:

```bash
python --version
```

### 2. Install the course packages

From the repository's top-level folder:

```bash
python -m pip install --upgrade pip
python -m pip install -r materials/requirements.txt
```

For the guided notebook's full spaCy examples, also install the small English language model:

```bash
python -m spacy download en_core_web_sm
```

The notebooks can still tokenize text if this model is unavailable, but part-of-speech tags, lemmas, and other trained annotations require it.

### 3. Optional: install transformer packages

Install these **in the same active environment** when the course moves to transformer-based work:

```bash
python -m pip install -r materials/requirements-transformers.txt
```

This file also includes the base requirements. It adds PyTorch, Hugging Face Transformers, Accelerate, and Datasets. The install and later model downloads are larger than the Day 1 setup; you do not need them for the notebooks currently in this repository.

### 4. Start JupyterLab

```bash
python -m jupyter lab
```

In the browser, open `materials/notebooks/day_1_representation.ipynb`. Choose the kernel from your `.venv` if Jupyter asks. Run cells **from top to bottom**. Then open `day_1_representation_exercise.ipynb`, run its prepared setup cells, and edit the cells marked **STUDENT EDIT**. Use *Kernel → Restart Kernel and Run All Cells* to check that your work runs from a clean start.

The CSV files are already included in `materials/data/`; no dataset download is needed for class. The script in `materials/scripts/` is only for rebuilding selected open datasets.

## How to work with the repository

- Keep the original data files in `materials/data/`. Save your own analyses or modified notebooks under a new name so you can compare them with the supplied version.
- When you change a representation, compare it with the baseline on the **same documents**. Record which setting changed and what happened to the vocabulary, most frequent terms, and document similarities.
- Read example texts before interpreting a pattern as a substantive finding. A feature can be statistically prominent yet measure something other than the concept you intended.
- If new course materials are added later, update your local copy before class (`git pull` for a clone, or download a new ZIP).

## Troubleshooting

- **`No module named ...` or the wrong Jupyter kernel:** activate `.venv`, reinstall with the commands above if needed, and restart JupyterLab. In a notebook, `import sys; print(sys.executable)` should point to the `.venv` Python.
- **spaCy cannot find `en_core_web_sm`:** run `python -m spacy download en_core_web_sm` in the active environment. The notebooks fall back to a blank English tokenizer if the model is missing.
- **A data file is not found:** start JupyterLab from the repository's top-level folder and run the notebook's setup cells before later cells.
- **Windows does not activate the environment:** use Command Prompt with `.venv\Scripts\activate.bat`, or follow your institution's guidance for PowerShell execution policy.

The optional conda environment files are in `materials/` for students who use conda rather than pip.
