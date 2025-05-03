
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
from datetime import datetime
import supervision as sv
from supervision import ByteTrack


# Load the YOLO model
model = YOLO('yolo11l-seg.pt')
tracker = sv.ByteTrack()

# Open video input
video_path = '/Users/saikrishnamateti/Documents/Yolov11 Object detection/video/video_1.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Output file setup
now = datetime.now()
date_time = now.strftime("%Y%m%d_%H%M%S")
output_video_path = f"output_video_with_speed_{date_time}.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Define the annotators
mask_annotator = sv.MaskAnnotator()
label_annotator = sv.LabelAnnotator(text_color=sv.Color.BLACK, text_position=sv.Position.CENTER)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to PIL image
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Perform prediction
    result = model.predict(pil_image, conf=0.25)[0]

    # Convert detections
    detections = sv.Detections.from_ultralytics(result)

    # Annotate the frame with masks and labels
    annotated_frame = frame.copy()
    annotated_frame = mask_annotator.annotate(annotated_frame, detections=detections)
    annotated_frame = label_annotator.annotate(annotated_frame, detections=detections)

    # Write annotated frame to output video
    out.write(annotated_frame)

# Release resources
cap.release()
out.release()

print(f'Video saved to {output_video_path}')

