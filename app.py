import os
import json
import numpy as np
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "plant_disease_model.h5")
LABEL_PATH = os.path.join(BASE_DIR, "class_labels.json")
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(
    __name__,
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)

# Global history list for last 3 detections
detection_history = []

# Global cached model and status
_model = None
_model_load_attempted = False
_model_load_error = None

# ----------------------------------------------------------
# Load labels
# ----------------------------------------------------------
CLASS_NAMES = []
if os.path.exists(LABEL_PATH):
    try:
        with open(LABEL_PATH, "r", encoding="utf-8") as f:
            CLASS_NAMES = json.load(f)
    except Exception as e:
        print(f"[WARN] Error loading class_labels.json: {e}")
        CLASS_NAMES = ["Unknown"]
else:
    CLASS_NAMES = ["Unknown"]
    print(f"[WARN] class_labels.json not found at {LABEL_PATH} -- using placeholder.")

# ----------------------------------------------------------
# Load model safely (Lazy-loaded for Serverless compatibility)
# ----------------------------------------------------------
def get_model():
    """
    Lazily loads and caches the TensorFlow Keras model.
    Importing TensorFlow and loading the model on-demand prevents
    module-import timeouts during serverless cold starts.
    """
    global _model, _model_load_attempted, _model_load_error

    if _model is not None:
        return _model

    if _model_load_attempted and _model_load_error is not None:
        return None

    _model_load_attempted = True

    if not os.path.exists(MODEL_PATH):
        _model_load_error = f"Model file not found at {MODEL_PATH}"
        print(f"[WARN] {_model_load_error}")
        return None

    try:
        print(f"[INFO] Attempting to load model from {MODEL_PATH}...")
        from tensorflow.keras.models import load_model
        _model = load_model(MODEL_PATH)
        print("[SUCCESS] Model loaded successfully.")
        return _model
    except Exception as e:
        _model_load_error = str(e)
        print(f"[ERROR] Model load error: {e}")
        return None

# For backward compatibility with existing code/tests
def load_model_safely():
    return get_model()

# ----------------------------------------------------------
# Home Route
# ----------------------------------------------------------
@app.route("/")
def index():
    model_available = os.path.exists(MODEL_PATH)
    return render_template("index.html", model_loaded=model_available)

# ----------------------------------------------------------
# Predict Route
# ----------------------------------------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded."}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected."}), 400

    model = get_model()
    if model is None:
        err_msg = _model_load_error or "Model is not available. Please verify model dependencies and file."
        return jsonify({"error": f"Model unavailable: {err_msg}"}), 503

    try:
        from PIL import Image

        # In-memory image processing (production-safe: no local disk write to read-only filesystems)
        img = Image.open(file.stream).convert("RGB")
        img = img.resize((224, 224))
        x = np.array(img, dtype=np.float32) / 255.0
        x = np.expand_dims(x, axis=0)

        from disease_info import get_disease_info

        preds = model.predict(x)
        pred_class = CLASS_NAMES[np.argmax(preds)] if CLASS_NAMES else "Unknown"
        disease_info = get_disease_info(pred_class)

        # Add to history
        detection_history.append({
            "disease": pred_class,
            "display_name": disease_info.get("display_name", pred_class),
            "status": disease_info.get("status", "Unknown"),
            "image": file.filename or "upload.jpg"
        })
        if len(detection_history) > 3:
            detection_history.pop(0)

        return jsonify({
            "disease": pred_class,
            "display_name": disease_info.get("display_name", pred_class),
            "status": disease_info.get("status", "Unknown"),
            "precautions": disease_info.get("precautions", []),
            "medicines_pesticides": disease_info.get("medicines_pesticides", []),
            "cure_steps": disease_info.get("cure_steps", ""),
            "history": detection_history
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ----------------------------------------------------------
# Run Flask app
# ----------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
