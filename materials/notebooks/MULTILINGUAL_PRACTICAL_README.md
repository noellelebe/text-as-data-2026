# Day 4 multilingual practical

## Files

- `day_4_multilingual_analysis.ipynb`: complete, route-led practical. Its core runs offline using only the course's main requirements.
- `../data/multilingual_climate_examples.csv`: 36 constructed EN/DE/ES headlines and human-written English teaching paraphrases. No row is a ParlLawSpeech record or machine translation.
- `../data/multilingual_climate_embeddings.npz`: 36 × 384 normalized sentence embeddings of the **original** headlines. Generated with `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`; IDs and vector order are verified in the notebook.
- `prepare_parllawspeech_sample.py`: optional adapter for official ParlLawSpeech RDS files downloaded before class. It exports a small year-stratified, length-filtered, **unlabelled** CSV. It does not download the approximately 4 GB official release.
- `../requirements-multilingual-optional.txt`: packages for the optional model calls and RDS conversion. The core notebook does not need them.

## Route through the notebook

| Part | Core demonstration | Lecture connection |
|---|---|---|
| 0–1 | Corpus and codebook; comparable vs parallel; language labels, mixed spans, Unicode, scripts, tokenization, word/character TF–IDF | Slides 13–29 |
| 2 | Route A: local dictionaries, error repair, entity linking, supervised models, local topics, sentiment | Slides 38–59 |
| 3 | Route B: term vs full-text translation, English dictionary and classifier, translated topics, paired audits | Slides 60–73 |
| 4 | Route C: real multilingual vectors, retrieval, cross-language prototype classification, shared clustering, linked documents, optional NLI and sentiment models, LLM prompt/evaluation protocol | Slides 74–96 |
| 5 | Per-language/category errors, method disagreements, abstention, confounding | Slides 97–109 |
| 6–8 | ParlLawSpeech adapter, optional model reproduction, research design handoff | Slides 110–114 |

## Suggested live use

For a practical block of roughly 75–90 minutes, run sections 0–1 (15 minutes), Route A (20), Route B (15), Route C through the embedding prototype and cluster (20), and the validation tables (15). Use the interpretive prompts after the displayed tables. The optional NLI/sentiment model cells and the full ParlLawSpeech adapter are extensions; they are disabled or conditional so the core run is predictable.

The 36 constructed headlines yield unusually easy cross-language embedding matches. The resulting perfect prototype score is explicitly labelled as a property of this teaching sample, not a method comparison for real speech. The local supervised classifiers also have only 12 examples per language; their numbers illustrate pipeline mechanics only. For a research-grade exercise, prepare human-coded, source-language held-out examples from an authentic corpus.

## ParlLawSpeech choice

ParlLawSpeech is substantively well suited to this course: it provides parliamentary speeches with speaker, date, party, agenda and links to bills and laws across seven countries plus the European Parliament. The EP and Hungarian speech files also include English translations for substantial portions of the data. However, the official release is large, in RDS format, and does not provide the three teaching labels. The EP corpus includes mid-speech language changes, so a single speech language label can be wrong. A prepared extract works better than a live download, but it needs a new speech/paragraph-level codebook and human labels before method evaluation.

Data source: Schwalbach, Hetzer, Proksch, Rauh & Sebők (2025), *ParlLawSpeech*, GESIS, v1.0.0, DOI [10.7802/2824](https://doi.org/10.7802/2824), CC BY 4.0. [Official data schema](https://parllawspeech.org/data). The [data descriptor](https://www.nature.com/articles/s41597-026-08335-4) documents the EP sentence-level language detection and English translation process. **No PLS extract is currently bundled.**

To prepare one once the official files are local:

```bash
python materials/notebooks/prepare_parllawspeech_sample.py \
  /path/to/Corpus_speeches_EP.RDS \
  /path/to/Corpus_speeches_germany.RDS \
  --output materials/data/parllawspeech_sample.csv \
  --n-per-year 20
```

The script keeps source metadata and outputs an unlabelled, length-filtered, year-stratified demonstration sample. It is not a prevalence sample. Review its fields, select the coding unit, and have language-capable readers label a separate test set.

## Verification

All 45 core code cells were executed in sequence in a clean temporary directory with the two bundled teaching data files. Optional model cells were left off. The Jupyter kernel could not start inside the sandbox because local socket binding is restricted, so verification used sequential in-process cell execution. The optional model calls require their dependencies and have not been included in that core run.
