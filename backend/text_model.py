from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

# Load pre-trained model and tokenizer
MODEL_NAME = "unitary/toxic-bert"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Predict toxicity from text
def detect_toxicity(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1).tolist()[0]

    labels = ["Non-toxic", "Toxic"]

    return {
        "text": text,
        "prediction": {
            labels[i]: float(probs[i]) for i in range(len(labels))
        }
    }
