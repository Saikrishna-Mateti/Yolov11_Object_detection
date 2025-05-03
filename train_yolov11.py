from ultralytics import YOLO
import torch
from roboflow import Roboflow

# Download the dataset from Roboflow
rf = Roboflow(api_key="KCaSBABRf8G7xiPtu9rA")
project = rf.workspace("university-of-peradeniya-5ywn6").project("final-lmoyv")
version = project.version(1)
dataset = version.download("yolov11")
print(f"Dataset downloaded to: {dataset.location}")

# Check if MPS is available
# if torch.backends.mps.is_available():
#     device = 'mps'
# else:
#     device = 'cpu'
# print(f"Using device: {device}")

# Load the pre-trained YOLOv11 segmentation model
model = YOLO('yolo11n-seg.pt')  # Nano version for faster training

# Train the model on the Roboflow dataset
results = model.train(
    data=f"{dataset.location}/data.yaml",  # Path to the downloaded data.yaml
    epochs=10,             # Adjust as needed
    imgsz=640,             # Image size
    batch=8,               # Adjust based on memory
    device='cpu',         # Use MPS or CPU
    patience=5             # Early stopping
)

# Save the trained weights
model.save('yolo11n_custom_trained.pt')             