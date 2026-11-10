"""Create a small, unlabelled teaching extract from downloaded ParlLawSpeech speech files.

Example:
  python prepare_parllawspeech_sample.py /path/Corpus_speeches_EP.RDS \
      /path/Corpus_speeches_germany.RDS --output materials/data/parllawspeech_sample.csv

Source: Schwalbach et al. (2025), ParlLawSpeech v1.0.0, DOI 10.7802/2824.
The official files are CC BY 4.0. This script does not download them.
"""
import argparse
from pathlib import Path
import pandas as pd


def read_source(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".rds":
        try:
            import pyreadr
        except ImportError as e:
            raise SystemExit("Install pyreadr first: pip install pyreadr") from e
        result = pyreadr.read_r(str(path))
        frame = next(iter(result.values()))
    elif path.suffix.lower() == ".csv":
        frame = pd.read_csv(path)
    elif path.suffix.lower() == ".parquet":
        frame = pd.read_parquet(path)
    else:
        raise SystemExit(f"Unsupported input: {path}")
    if not {"text", "speechnumber", "date"}.issubset(frame.columns):
        raise SystemExit(f"{path.name}: expected text, speechnumber, date; found {frame.columns.tolist()}")
    frame = frame.copy()
    frame["source_file"] = path.name
    frame["year"] = pd.to_datetime(frame.date, errors="coerce").dt.year
    frame["n_chars"] = frame.text.fillna("").astype(str).str.len()
    return frame


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("sources", nargs="+", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--n-per-year", type=int, default=20)
    ap.add_argument("--min-chars", type=int, default=200)
    ap.add_argument("--max-chars", type=int, default=4000)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    if args.n_per_year < 1 or args.min_chars < 1 or args.max_chars < args.min_chars:
        ap.error("Check sample size and length bounds")
    parts = []
    for path in args.sources:
        frame = read_source(path)
        frame = frame.loc[frame.year.notna() & frame.n_chars.between(args.min_chars, args.max_chars)]
        sample = (frame.groupby("year", group_keys=False)
                  .apply(lambda x: x.sample(min(len(x), args.n_per_year), random_state=args.seed),
                         include_groups=False))
        # pandas groupby.apply may exclude the grouping key; restore it from each sampled row's date.
        sample = sample.reset_index(drop=True)
        sample["year"] = pd.to_datetime(sample.date, errors="coerce").dt.year
        parts.append(sample)
        print(path.name, "sampled", len(sample), "speeches from", sample.year.nunique(), "years")
    out = pd.concat(parts, ignore_index=True, sort=False)
    out["source_id"] = out.source_file.astype(str) + ":" + out.speechnumber.astype(str)
    if out.source_id.duplicated().any():
        raise SystemExit("Duplicate source_id values; inspect the original identifiers")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False, encoding="utf-8")
    print("Wrote", args.output, "rows", len(out), "columns", len(out.columns))
    print("Unlabelled, length-filtered and year-stratified demonstration sample; not a prevalence sample.")


if __name__ == "__main__":
    main()
