
# Disaster Tweet Classifier

This project is a Natural Language Processing (NLP) solution that classifies tweets to determine whether they are about real disasters or not. It uses a Logistic Regression model trained on the Kaggle competition dataset "Natural Language Processing with Disaster Tweets."

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
  

## Project Overview

The goal of this project is to predict whether a given tweet is related to a real disaster. This can assist emergency response organizations in filtering relevant tweets in real-time.

## Dataset

- Source: [Kaggle - Natural Language Processing with Disaster Tweets](https://www.kaggle.com/competitions/nlp-getting-started)
- The dataset consists of 10,000 labeled tweets.
- Each tweet is labeled:
  - `1`: Disaster tweet
  - `0`: Not a disaster tweet

## Model Architecture

- **TF-IDF Vectorizer:** Converts text data into numerical form.
- **Logistic Regression:** Chosen for its performance and simplicity in text classification tasks.

Other models like Naive Bayes, SVM, XGBoost, and deep learning models (LSTM, BERT) were also experimented with during development.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/disaster-tweet-classifier.git
cd disaster-tweet-classifier
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Gradio app locally:

```bash
python app.py
```

The interface will open in your browser where you can input a tweet and receive the prediction.

## Deployment

This project can be deployed in two ways:

### 1. Local Deployment

* Run using FastAPI or Gradio on your local machine.

### 2. Hugging Face Spaces Deployment

* Upload the following files to a Hugging Face Space with Gradio as the SDK:

  * `app.py`
  * `logistic_model.pkl`
  * `tfidf_vectorizer.pkl`
  * `requirements.txt`
  * `README.md`

The app will be live with a public URL for sharing.

## Project Structure

```
disaster-tweet-classifier/
├── app.py                # Gradio app
├── logistic_model.pkl     # Trained logistic regression model
├── tfidf_vectorizer.pkl   # Saved TF-IDF vectorizer
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── submission.csv         # Kaggle submission file (optional)
```




