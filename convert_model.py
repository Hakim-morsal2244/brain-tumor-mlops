import tensorflow as tf


# Load old H5 model
old_model = tf.keras.models.load_model(
    "notebooks/brain_tumor_cnn_baseline.h5",
    compile=False
)


# Save as new Keras format
old_model.save(
    "models/brain_tumor_cnn_mlflow.keras"
)


print("Model converted successfully!")