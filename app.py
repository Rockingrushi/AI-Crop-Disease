import os
import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MODEL_PATH = "plant_disease_model.h5"
LABEL_PATH = "class_labels.json"

# Global history list for last 3 detections
detection_history = []

# ----------------------------------------------------------
# 🌱 Load model safely
# ----------------------------------------------------------
def load_model_safely():
    """
    Load the model if it exists; otherwise, return None and print instructions.
    """
    if not os.path.exists(MODEL_PATH):
        print("⚠️ Model not found at", MODEL_PATH)
        print("Please train the model using plant_disease_training.ipynb (in Colab) and download plant_disease_model.h5 and class_labels.json from your Google Drive to this directory.")
        return None

    try:
        model = load_model(MODEL_PATH)
        print("✅ Model loaded successfully.")
        return model
    except Exception as e:
        print("❌ Model load error:", e)
        return None

# ----------------------------------------------------------
# 🌿 Load model & labels
# ----------------------------------------------------------
model = load_model_safely()

if os.path.exists(LABEL_PATH):
    with open(LABEL_PATH, "r") as f:
        CLASS_NAMES = json.load(f)
else:
    CLASS_NAMES = ["Unknown"]
    print("⚠️ class_labels.json not found — using placeholder.")

# ----------------------------------------------------------
# 🌼 Home Route
# ----------------------------------------------------------
@app.route("/")
def index():
    model_loaded = model is not None
    return render_template("index.html", model_loaded=model_loaded)

# ----------------------------------------------------------
# 🔍 Predict Route
# ----------------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not available. Please restart the server."})

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded."})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected."})

    try:
        img_path = os.path.join("static", file.filename or "uploaded_image.jpg")
        file.save(img_path)

        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0) / 255.0

        preds = model.predict(x)
        pred_class = CLASS_NAMES[np.argmax(preds)] if CLASS_NAMES else "Unknown"

        # Add to history
        detection_history.append({"disease": pred_class, "image": "/" + img_path})
        if len(detection_history) > 3:
            detection_history.pop(0)

        return jsonify({"disease": pred_class, "history": detection_history})
    except Exception as e:
        return jsonify({"error": str(e)})

# ----------------------------------------------------------
# 🚀 Run Flask app
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
