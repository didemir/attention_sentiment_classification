
# Sentiment Analysis

This is the **Assignment 1** of **Transformers and Attention-Based Deep Networks** Course.

## Details

* The task is to classify the sentiment of customer service conversations.
* WANDB will be used for experiment tracking and hyperparameter tuning.
* Github and git will be used for version control and publishing.
* A suitable attention-based network will be used for sentiment classification.
* Input will be _customer-support interaction_ while the output is expected to be _positive, negative, or neutral_

## TODOs

- [ ] Data exploration and pre-processing
  - [ ] Prepare an Exploratory Data Analysis (EDA)
    - [ ] Indicate distribution of the sentiment classes
    - [ ] Find and report important facts about the data
    - [ ] Check and report correlation of sentiment feature with other features.
  - [ ] Determine necessary features
    - [ ] Explain why they are necessary
  - [ ] Prepare train and validation subsets
    - [ ] Make sure there is no data-leakage from test dataset
  - [ ] Complete data preprocessing
    - [ ] Explain each step
    - [ ] Justify your approaches
  - [ ] Include figures, tables and plots
- [ ] Model training
  - [ ] Decide on training from scratch or fine-tuning
    - [ ] Justify your decision
  - [ ] Evaluate the trained model on the test set
  - [ ] Report the results with appropriate evaluation metrics
  - [ ] The code will be submited to odtuclass and it must be working and reproducible 
  - [ ] The code must made publicly available at the github repo
  - [ ] Experiments must be recorded by utilizing WANDB and the report must be publicly available as a dashboard or report
- [ ] Prepare a report that clearly explains the steps

## Dataset

```
0_data/
├── test.csv
└── train.csv
```

