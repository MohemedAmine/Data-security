import gradio as gr
import joblib
import pandas as pd
import numpy as np
from feature_extraction import extract_features, preprocess

# Load the trained model
model = joblib.load("best_model.pkl")

# Class label mapping
label_map = {
    0: "🟢 Benign",
    1: "🟠 Defacement",
    2: "🔶 Malware",
    3: "🔴 Phishing"
}

# Prediction function
def predict_url_type(url):
    try:
        # Prepare input
        input_df = pd.DataFrame({"url": [url]})
        features_df = extract_features(input_df)
        X = preprocess(features_df)

        # Make prediction
        prediction = model.predict(X)[0]
        proba_all = model.predict_proba(X)[0]

        # Format result
        result = f"## {label_map[prediction]}\n\n"
        result += "### 🔍 Prediction Probabilities:\n"
        result += f"- 🟢 Benign: {proba_all[0]:.2%}\n"
        result += f"- 🟠 Defacement: {proba_all[1]:.2%}\n"
        result += f"- 🔶 Malware: {proba_all[2]:.2%}\n"
        result += f"- 🔴 Phishing: {proba_all[3]:.2%}\n"

        return result

    except Exception as e:
        return f"❌ Error during analysis: {str(e)}"

# Gradio Interface
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown(
        """
# 🛡️ URL Threat Detector
This system uses a machine learning model to detect whether a given URL is classified as:  
**Benign**, **Defacement**, **Malware**, or **Phishing**.
"""
    )

    with gr.Row():
        url_input = gr.Textbox(label="🔗 Enter URL", placeholder="https://example.com", lines=1)
        predict_btn = gr.Button("🔍 Analyze")
        clear_btn = gr.Button("🧹 Clear")

    result_output = gr.Markdown("Prediction result will appear here.")

    predict_btn.click(fn=predict_url_type, inputs=url_input, outputs=result_output)
    clear_btn.click(fn=lambda: "", inputs=None, outputs=url_input)

# Launch the app
app.launch()

