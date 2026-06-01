from transformers import AutoImageProcessor
from transformers import AutoModelForImageClassification

MODEL_NAME = "umm-maybe/AI-image-detector"

processor = AutoImageProcessor.from_pretrained(MODEL_NAME)

model = AutoModelForImageClassification.from_pretrained(
    MODEL_NAME
)