# 🧠 Brain Tumor Classification MLOps Project

An end-to-end **Machine Learning Operations (MLOps)** project for classifying brain tumors from MRI images using **Deep Learning, TensorFlow, MLflow, FastAPI, and Docker**.

This project demonstrates the complete ML lifecycle:

🚀 Data preprocessing  
🧠 CNN model training  
📊 Model evaluation  
🔬 Experiment tracking with MLflow  
⚡ FastAPI deployment  
🐳 Docker containerization  
🔄 Model prediction pipeline  

---

# 📌 Project Overview

Brain tumors require accurate and early detection to support medical decision-making.

This project builds a deep learning classification system that analyzes MRI brain images and predicts one of four classes:

| Class | Description |
|---|---|
| 🧠 Glioma | A type of brain tumor originating from glial cells |
| 🧠 Meningioma | A tumor developing from the meninges |
| ✅ No Tumor | MRI image without tumor |
| 🧠 Pituitary | Tumor affecting the pituitary gland |

The final model is deployed as an API where users can upload an MRI image and receive a prediction with confidence score.

---

# 🏗️ System Architecture
```text
MRI Images
     |
     ↓
Data Preprocessing
     |
     ↓
CNN Model Training
     |
     ↓
Model Evaluation
     |
     ↓
MLflow Experiment Tracking
     |
     ↓
Saved Model
     |
     ↓
FastAPI Deployment
     |
     ↓
Docker Container
     |
     ↓
Prediction API
```

# 🛠️ Technologies Used

## Machine Learning

- 🐍 Python
- 🧠 TensorFlow 2.21
- 🔥 Keras
- 📊 Scikit-learn
- 🖼️ Pillow
- 🔢 NumPy

## MLOps Tools

- 🔬 MLflow
- 🐳 Docker
- ⚡ FastAPI
- 🚀 Uvicorn
- 📓 Jupyter Notebook

## Development Tools

- Git & GitHub
- VS Code
- Python Virtual Environment

---

# 📂 Project Structure
```text
brain-tumor-mlops/

├── app/
│   ├── api.py                 # FastAPI prediction API
│   ├── model_loader.py        # Loads trained model
│   ├── utils.py               # Utility functions
│   └── __init__.py

├── models/
│   └── brain_tumor_cnn_mlflow.h5

├── notebooks/
│   └── train_model.ipynb      # Model training notebook

├── Dockerfile                 # Container configuration
├── requirements.txt           # Python dependencies
├── mlflow_tracking.py         # MLflow experiment tracking
├── convert_model.py           # Model conversion utility
└── README.md                  # Project documentation
```

# 🧪 Model Training Pipeline

The training workflow includes:

### 1. Data Preprocessing

✅ MRI image loading  
✅ Image resizing to 224×224  
✅ RGB conversion  
✅ Pixel normalization  
✅ Dataset preparation  

---

### 2. Model Development

A Convolutional Neural Network (CNN) model was trained for multi-class classification.

Optimization techniques used:

✅ Adam optimizer  
✅ Validation monitoring  
✅ Model checkpointing  
✅ Loss optimization  

---

# 📊 Model Evaluation

The model was evaluated using multiple metrics:

| Metric | Score |
|---|---|
| Accuracy | ~87% |
| Precision | ~88% |
| Recall | ~87% |
| F1-score | ~87% |

Evaluation included:
<img width="510" height="389" alt="Screenshot 2026-07-27 005916" src="https://github.com/user-attachments/assets/6d2faaf9-263a-4fe5-b8ab-6ec115a46b4f" />

- Confusion matrix
- Classification report
- Loss curves
- Accuracy monitoring

---

# 🔬 MLflow Experiment Tracking

MLflow is used to track:

✅ Training experiments  
✅ Model versions  
✅ Performance metrics  
✅ Saved artifacts  

Example tracked information:

- Model parameters
- Accuracy
- Loss
- Trained model files

---

# 🚀 Running the API Locally

## 1. Clone Repository

```bash
git clone https://github.com/Hakim-morsal2244/brain-tumor-mlops.git
cd brain-tumor-mlops
```

## 2. Create Environment

```bash
python -m venv .venv
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Start API Server

```bash
uvicorn app.api:app --host 0.0.0.0 --port 8000
```

API will run at:

```
http://localhost:8000
```

---

# 📖 API Documentation

FastAPI automatically provides interactive documentation.

Open:

```
http://localhost:8000/docs
```

Users can:

- 📤 Upload MRI image
- ⚡ Run prediction
- 📊 Receive predicted tumor class
- 🎯 View confidence score

---

# 📸 API Demo Screenshots

## Swagger API Interface

![Swagger API](https://github.com/user-attachments/assets/31e5c474-a638-4372-af5f-c3211c75ee76)

## Prediction Result

![Prediction Result](https://github.com/user-attachments/assets/46feb697-b78d-4565-8a89-0ed48ab73f75)

---

# 🐳 Running with Docker

Build image:

```bash
docker build -t brain-tumor-api .
```

Run container:

```bash
docker run -p 8000:8000 brain-tumor-api
```

🔮 Prediction Example

Input:

MRI brain image

Output:

{
  "prediction": "glioma",
  "confidence": 0.94
}
🔄 Retraining Workflow

The project supports model retraining through:

- 📥 New MRI data collection
- 🗂️ Data preprocessing
- 🧠 CNN model training
- 📊 Model evaluation
- 🔬 MLflow tracking
- 💾 Saving updated model

👩‍💻 Author

Morsal Hakim

Software Engineering Student
African Leadership University

🔗 GitHub:
https://github.com/Hakim-morsal2244

⭐ Future Improvements
Add web-based user interface
Deploy API to cloud platform
Add automated CI/CD pipeline
Improve accuracy using transfer learning models

⭐ If this project helped you, consider giving it a star!
