from PIL import Image
from backend.model_loader import model, processor
import torch
import torch.nn.functional as F

def predict_image(file):
    image = Image.open(file).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probabilities = F.softmax(logits, dim=-1)
    prediction = logits.argmax(-1).item()
    confidence = (probabilities[0][prediction].item() * 100)

    return {
        "prediction": "AI Generated" if prediction == 1 else "Real Image",
        "confidence": round(confidence, 2)
    }