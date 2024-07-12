from PIL import Image
import requests
from io import BytesIO
import torch
from transformers import CLIPProcessor, CLIPModel

def generate_image(prompt):
    # Cargar modelo de generación de imágenes
    model_id = "CompVis/stable-diffusion-v1-4"
    model = torch.hub.load("huggingface/pytorch-transformers", model_id)
    
    # Generar imagen
    inputs = processor(text=prompt, return_tensors="pt", padding=True)
    outputs = model.generate(**inputs)
    image = Image.fromarray(outputs.cpu().numpy(), "RGB")
    return image

def classify_image(image_file):
    # Cargar modelo de clasificación
    processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
    model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
    
    # Preprocesar imagen
    image = Image.open(image_file).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    
    # Clasificar imagen
    with torch.no_grad():
        logits = model(**inputs).logits
    
    # Obtener la etiqueta predicha
    predicted_label = logits.argmax(-1).item()
    label = model.config.id2label[predicted_label]
    return label