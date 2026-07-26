from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np

from app.model_loader import get_model

app = FastAPI(
    title="Brain Tumor Classification API",
    version="0.1.0"
)

# Load model once when the API starts
model = get_model()

# Class labels (make sure these match your training folder order)
class_names = [
    "glioma",
    "meningioma",
    "notumor",
    "pituitary"
]


@app.get("/")
def home():
    return {
        "message": "Brain Tumor Classification API is running!"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read uploaded image
        image = Image.open(file.file).convert("RGB")

        # Resize to model input size
        image = image.resize((224, 224))

        # Convert to numpy array
        image = np.array(image).astype("float32") / 255.0

        # Add batch dimension
        image = np.expand_dims(image, axis=0)

        # Make prediction
        prediction = model.predict(image, verbose=0)[0]

        # Get predicted class
        predicted_index = int(np.argmax(prediction))
        predicted_class = class_names[predicted_index]

        # Confidence score
        confidence = round(float(np.max(prediction)), 4)

        return JSONResponse(
            content={
                "prediction": predicted_class,
                "confidence": confidence
            }
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": str(e)
            }
        )