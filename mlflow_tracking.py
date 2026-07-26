import mlflow
import mlflow.keras
from tensorflow.keras.models import load_model


# Path to converted compatible model
model_path = "models/brain_tumor_cnn_mlflow.keras"


# Load model
model = load_model(
    model_path,
    compile=False
)


# Compile model
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# Create MLflow experiment
mlflow.set_experiment("Brain_Tumor_CNN_Experiments")


# Start MLflow run
with mlflow.start_run(run_name="Baseline_CNN_Run"):

    # Log model information
    mlflow.log_param(
        "model_type",
        "Baseline CNN"
    )

    mlflow.log_param(
        "image_size",
        "224x224"
    )

    mlflow.log_param(
        "batch_size",
        32
    )

    mlflow.log_param(
        "epochs",
        10
    )


    # Log evaluation results
    mlflow.log_metric(
        "test_accuracy",
        0.8694
    )

    mlflow.log_metric(
        "test_loss",
        1.2043
    )


    # Save model artifact in MLflow
    mlflow.keras.log_model(
        model,
        "brain_tumor_model"
    )


print("MLflow tracking completed!")