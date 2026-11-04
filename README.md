# SE Advanced Text Analysis (2026)

This repository contains the course materials for **SE Advanced Text Analysis**: lecture slides, practical notebooks, and datasets. Across the course, we work with text representation and preprocessing, dictionaries and annotation, supervised and unsupervised methods, embeddings and transformer models, and the evaluation and validation of text-based measures.

## Install the Python packages

Use **Python 3.10 or newer**. Open a terminal in the repository's top-level folder, the one containing this README and `materials/`.

Create and activate a virtual environment:

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

Install the core packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r materials/requirements.txt
```

For the full spaCy examples, install the small English language model:

```bash
python -m spacy download en_core_web_sm
```

The notebooks can still tokenize English text without this model, but trained annotations such as part-of-speech tags and lemmas require it.

### Transformer packages

When you need the transformer exercises, install their additional packages in the **same active environment**:

```bash
python -m pip install -r materials/requirements-transformers.txt
```

This requirements file also includes the core packages. It adds PyTorch, Hugging Face Transformers, Accelerate, and Datasets. The install and model downloads may take longer than the core setup.

## Use the materials

Start JupyterLab from the repository's top-level folder:

```bash
python -m jupyter lab
```

Open the notebook for your session in `materials/notebooks/` and run its cells from top to bottom. If Jupyter asks for a kernel, choose the Python environment in `.venv`. The notebooks use the bundled files in `materials/data/`, so you do not need to download datasets during class. Dataset sources are listed in the [data guide](materials/data/README.md).

Lecture slides are in the course's lecture folders. Exercise notebooks identify the cells you should edit; keep a copy of your work under a new filename if you want to preserve the supplied version. Run *Kernel → Restart Kernel and Run All Cells* before submitting or sharing a notebook to check that it works from a clean start.

## If something does not run

- **Missing Python package:** make sure `.venv` is active, rerun the relevant `pip install -r` command, and restart the notebook kernel.
- **Wrong Jupyter kernel:** run `import sys; print(sys.executable)` in a notebook. The path should point to `.venv`.
- **spaCy model missing:** run `python -m spacy download en_core_web_sm` in the active environment.
- **Data file missing:** start JupyterLab from the repository's top-level folder and run the notebook's setup cells first.

Conda users can use the environment files in `materials/` instead of the pip setup above.
