import tensorflow as tf
import os

MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "models",
        "brain_tumor_cnn_mlflow.h5"
    )
)

print("Loading model from:", MODEL_PATH)

model = tf.keras.models.load_model(
    MODEL_PATH,
    compile=False
)

print("Model loaded successfully")


def get_model():
    return model