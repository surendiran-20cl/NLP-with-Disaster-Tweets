import gradio as gr
import joblib
import pandas as pd

# Load model and vectorizer
model = joblib.load("logistic_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Prediction function
def predict_disaster(text):
    text_df = pd.DataFrame([text], columns=["text"])
    text_transformed = vectorizer.transform(text_df["text"])
    prediction = model.predict(text_transformed)
    label = "Disaster Tweet" if prediction[0] == 1 else "Not a Disaster Tweet"
    return label

# Gradio Interface
iface = gr.Interface(
    fn=predict_disaster,
    inputs=gr.Textbox(lines=4, placeholder="Enter the tweet here..."),
    outputs="text",
    title="Disaster Tweet Classifier",
    description="Classifies whether a tweet is about a real disaster or not.",
)

iface.launch()
