import cv2
import pandas as pd
from ultralytics import YOLO
from datetime import datetime

# Load YOLOv8 pretrained model (detects cars, trucks, bus, motorcycle from COCO)
model = YOLO("yolov8n.pt")   # n = nano version (fast), can use yolov8m.pt for better accuracy

# Open video file or webcam (0 = webcam)
cap = cv2.VideoCapture("C:\\Users\\hp\\Desktop\\projects\\vaultofcode projects\\vehicle\\cars2.mp4")

# Data storage
vehicle_data = []
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    results = model(frame)

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            
    
            if label in ["car", "truck", "bus", "motorcycle","person"]:
             
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, label, (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

                
                vehicle_data.append({
                    "Frame": frame_count,
                    "Vehicle Type": label,
                    "Time": datetime.now().strftime("%H:%M:%S")
                })

    # Show live detection
    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Save results to Excel
df = pd.DataFrame(vehicle_data)
df.to_excel("vehicle_report.xlsx", index=False)

print("Detection complete. Results saved to vehicle_report.xlsx")
