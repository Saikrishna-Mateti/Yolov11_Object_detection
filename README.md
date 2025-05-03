# 🚗 Real-Time Vehicle & Person Detection with YOLOv11 Segmentation

### Research Project | University of Alabama at Birmingham (UAB)

Welcome to my latest research project where I explore the power of **YOLOv11** in enhancing real-time urban traffic analysis. This work investigates how cutting-edge **object detection and segmentation** models can help build **smarter, safer, and more efficient transportation systems**.

---

## 🔍 Project Overview

This project leverages **YOLOv11 (You Only Look Once)** to detect and segment:

* 🚘 Vehicles: cars, buses, trucks
* 🚶 Pedestrians: people in various urban scenarios

Each video frame is **annotated with bounding boxes and pixel-level masks**, enabling fine-grained scene understanding under real-world conditions.

---

## ⚙️ Tech Stack

| Tool          | Role                                      |
| ------------- | ----------------------------------------- |
| `YOLOv11`     | Real-time object detection & segmentation |
| `PyTorch`     | Deep learning framework                   |
| `OpenCV`      | Video I/O and frame processing            |
| `Supervision` | Visualization of masks and bounding boxes |
| `Python`      | Scripting and orchestration               |

---

## 📊 Results

| Metric                            | YOLOv11                                  | YOLOv8 |
| --------------------------------- | ---------------------------------------- | ------ |
| **mAP\@0.5**                      | 🎯 91.2%                                 | 87.5%  |
| **IoU (Intersection over Union)** | 📈 78.9%                                 | 74.1%  |
| **Segmentation Accuracy**         | 🧠 Higher in occluded/overlapping scenes |        |

YOLOv11 demonstrates superior detection performance, particularly in **complex urban environments**.

---

## 🎯 Key Features

* ✅ Real-time object detection from video
* ✅ Pixel-accurate segmentation overlays
* ✅ Annotated video output for visualization
* ✅ Modular and extendable Python-based pipeline

---

## 🔧 Practical Applications

* 🚦 Smart Traffic Light Automation
* 👮‍♂️ Urban Surveillance & Crowd Monitoring
* 🚘 Perception Systems in Autonomous Vehicles
* 🧠 Edge AI Deployment (e.g., NVIDIA Jetson for low-latency inference)

---

## 🧪 Sample Output

> ✅ Annotated sample video with segmentation and bounding boxes coming soon!
> (*To be added in `/output` folder or linked via YouTube/GIF preview*)

---

## 📁 Repository Structure

```
📁 Yolov11-Object-Detection/
├── main.py                        # Main script for detection and segmentation
├── roboflow_dataset.py           # Script to download/prepare dataset from Roboflow
├── train_yolov11.py              # Custom training script for YOLOv11
├── yolo11l-seg.pt                # YOLOv11 large segmentation model weights
├── yolo11n-seg.pt                # YOLOv11 nano segmentation model weights
├── yolo11n_custom_trained.pt     # Your custom-trained YOLOv11 model weights
├── requirements.txt              # List of required Python packages
├── README.md                     # Project documentation (this file)

📁 model/                          # Pretrained model weights (optional for organization)
│   ├── yolo11l-seg.pt
│   ├── yolo11n-seg.pt
│   └── yolo11n_custom_trained.pt

📁 video/                          # Raw input video clips
│   ├── video_1.mp4
│   └── video_2.mp4

📁 output/                         # Output videos with bounding boxes & segmentation masks
│   ├── output_video_1.mp4
│   └── output_video_2.mp4

📁 runs/                           # YOLO training logs and checkpoints
│   ├── train/
│   └── detect/

📁 Output_video_files/             # Optional duplication folder for processed outputs
│   └── (same content as /output/)

```

---

## 🚀 Getting Started

1. Clone the repo

   ```bash
   git clone https://github.com/Saikrishna-Mateti/Yolov11_Object_detection.git
   cd Yolov11_Object_detection
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run detection

   ```bash
   python main.py
   ```

---

## 📬 Contact

**Sai Krishna Mateti**
📍 Graduate Researcher, UAB
📧 \[saikrishna.mateti7@gmail.com]
🌐 [LinkedIn]((https://www.linkedin.com/in/sai-krishna-mateti7/))


