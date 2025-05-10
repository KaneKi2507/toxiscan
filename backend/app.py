from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
import pytesseract
from PIL import Image
import torch
from nsfw_detector import classify_image  # <-- Import new NSFW detector function

# Tell Python where Tesseract OCR is installed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
CORS(app)

# Load text toxicity detection model
classifier = pipeline("text-classification", model="unitary/toxic-bert", top_k=None)

# Logs
detected_texts = []
detected_images = []
nsfw_images = []
banned_users = []

# ---------- TEXT TOXICITY DETECTION ----------
@app.route("/detect_text", methods=["POST"])
def detect_text():
    data = request.get_json()
    input_text = data.get("text", "")

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    result = classifier(input_text)[0]
    formatted = {item['label']: round(item['score'], 4) for item in result}

    detected_texts.append({
        "text": input_text,
        "prediction": formatted
    })

    return jsonify({
        "text": input_text,
        "prediction": formatted
    })

# ---------- TEXT-FROM-IMAGE DETECTION (OCR) ----------
@app.route("/detect_image", methods=["POST"])
def detect_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    img = Image.open(image_file.stream)

    extracted_text = pytesseract.image_to_string(img)
    result = classifier(extracted_text)[0]
    formatted = {item['label']: round(item['score'], 4) for item in result}

    detected_images.append({
        "image_name": image_file.filename,
        "text": extracted_text,
        "prediction": formatted
    })

    return jsonify({
        "image": image_file.filename,
        "text_extracted": extracted_text,
        "prediction": formatted
    })

# ---------- NSFW IMAGE DETECTION ----------
@app.route("/detect_nsfw_image", methods=["POST"])
def detect_nsfw_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files['image']
    image = Image.open(image_file.stream).convert("RGB")

    prediction = classify_image(image)

    nsfw_images.append({
        "image_name": image_file.filename,
        "prediction": prediction
    })

    return jsonify({
        "image": image_file.filename,
        "prediction": prediction
    })

# ---------- ADMIN PANEL ----------
@app.route("/admin/get_logs", methods=["GET"])
def get_logs():
    return jsonify({
        "texts": detected_texts,
        "images": detected_images,
        "nsfw_images": nsfw_images,
        "banned_users": banned_users
    })

@app.route("/admin/delete_text", methods=["POST"])
def delete_text():
    data = request.get_json()
    text_to_delete = data.get("text", "")
    detected_texts[:] = [entry for entry in detected_texts if entry["text"] != text_to_delete]
    return jsonify({"status": "Deleted", "text": text_to_delete})

@app.route("/admin/ban_user", methods=["POST"])
def ban_user():
    data = request.get_json()
    username = data.get("username", "")
    if username and username not in banned_users:
        banned_users.append(username)
        return jsonify({"status": f"User {username} banned"})
    return jsonify({"error": "Invalid username or already banned"}), 400

# Run server
if __name__ == "__main__":
    app.run(debug=True)
