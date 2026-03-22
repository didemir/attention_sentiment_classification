# DI725 Assignment 1 — Sentiment Classification of Customer-Service Conversations

**Course:** Transformers and Attention-Based Deep Networks  
**Student:** Didem Demir — 2739563  

## Task

3-class sentiment classification (**positive / negative / neutral**) of customer-service conversations using a fine-tuned BERT model.

## Repository Structure

```
├── 0_data/
│   ├── train.csv                  # Training data (970 samples)
│   └── test.csv                   # Test data (30 samples) — never used during training
├── main.ipynb                     # Full pipeline: EDA → augmentation → training → evaluation
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md
```

## Approach

- **EDA:** Cramer's V analysis for feature selection; removed data-leaking and low-signal columns
- **Augmentation:** Gemini paraphrasing + EN→FR→EN back-translation to expand 17 positive samples to 68
- **Model:** `bert-base-uncased` + learned categorical embeddings (BertTabular)
- **Training:** Differential learning rates (2e-5 BERT / 1e-3 head), weighted cross-entropy, linear warmup
- **Truncation:** Tail truncation — keeps last 510 tokens to preserve sentiment-rich conversation endings

## Results

| Metric | Value |
|---|---|
| Best Val Macro F1 | 0.862 (epoch 5) |
| Test Macro F1 | 0.614 |
| Test Accuracy | 0.633 |

## Experiment Tracking

WANDB project: `DI725-sentiment` — run `bert-tabular-v1`  
Public dashboard: https://wandb.ai/didem-demir_01-middle-east-technical-university/DI725-sentiment

## Setup

```bash
pip install -r requirements.txt
```

Then run `main.ipynb` top to bottom.

> ⚠️ A Gemini API key is required for the augmentation step. Add it to a `.env` file as `GEMINI_API_KEY=...`. The augmented data is already saved, so this step can be skipped on re-runs.

## Environment

Python version is `Python 3.11.9`.

