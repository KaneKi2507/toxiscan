from transformers import AutoProcessor, DetrForObjectDetection
from PIL import Image
import torch

# Load processor and model from HuggingFace
processor = AutoProcessor.from_pretrained("facebook/detr-resnet-50")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50")

# Function to predict image contents
def predict_image_toxicity(image: Image.Image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    # Convert output to readable labels
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

    # Get labels like "person", "car", etc.
    detected_labels = [model.config.id2label[label.item()] for label in results["labels"]]

    if not detected_labels:
        return "No objects detected"
    return "Detected: " + ", ".join(detected_labels)
