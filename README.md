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
├── main.py                # Main detection and segmentation script
├── model/                 # YOLOv11 weight files
├── video/                 # Input video clips
├── output/                # Processed videos with annotations
├── utils/                 # Utility functions (e.g., annotation helpers)
├── requirements.txt       # Python dependencies
└── README.md              # You're here!
```

---

## 🚀 Getting Started

1. Clone the repo

   ```bash
   git clone https://github.com/your-username/yolov11-traffic-detection.git
   cd yolov11-traffic-detection
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


