from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import torch

# ✅ Use a public, working model
model_id = "Falconsai/nsfw_image_detection"
extractor = AutoFeatureExtractor.from_pretrained(model_id)
model = AutoModelForImageClassification.from_pretrained(model_id)

# 🔍 Main prediction function
def classify_image(image):
    image = image.convert("RGB")
    inputs = extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
    labels = model.config.id2label
    return {labels[i]: round(probs[i].item(), 4) for i in range(len(probs))}
