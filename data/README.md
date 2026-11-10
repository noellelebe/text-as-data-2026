# Local Datasets

| File | Exercise | Source |
| --- | --- | --- |
| `sms_spam.csv` | Neural classification, frozen features, transformer fine-tuning | [UCI SMS Spam Collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection) |
| `sotu.csv` | Freedom sentences and semantic axes in State of the Union speeches | Existing State of the Union dataset from the teaching repository |
| `tweet_eval_sentiment_sample.csv` | Zero-shot and few-shot LLM sentiment annotation | Local sample of [TweetEval sentiment](https://huggingface.co/datasets/cardiffnlp/tweet_eval) |

The CSVs are unchanged copies of the datasets used in the course notebook.
No data download is needed during the practical. SMS duplicates are removed in
the notebook before its train/validation/test split.
