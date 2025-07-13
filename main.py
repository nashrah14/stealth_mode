from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

model = YOLO("best.pt") 

tracker = DeepSort(
    max_age=60,
    n_init=3,
    nn_budget=100,
    max_cosine_distance=0.3
)

# Input video
video_path = "15sec_input_720p.mp4"
cap = cv2.VideoCapture(video_path)

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_reid.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)
    detections = []

    
    for box in results[0].boxes:
        cls_id = int(box.cls.item())
        conf = float(box.conf.item())
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

        if cls_id == 0:  
            bbox = [x1, y1, x2 - x1, y2 - y1]  # Convert to (x, y, w, h)
            detections.append((bbox, conf, "player"))

    
    tracks = tracker.update_tracks(detections, frame=frame)

  
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(frame, f'Player {track_id}', (l, t - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)

    
    cv2.imshow("Player Re-ID", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()
