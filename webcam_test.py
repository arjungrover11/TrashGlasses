import cv2
import numpy as np
import tensorflow as tf
import requests
import time

# Get real location from IP
def get_location():
    try:
        r = requests.get('http://ipinfo.io/json', timeout=3)
        data = r.json()
        lat, lon = data['loc'].split(',')
        return float(lat), float(lon)
    except:
        return 26.8467, 80.9462

# Load model
interpreter = tf.lite.Interpreter(
    model_path=r"C:\Users\HP\Desktop\Project\trash_model_v2.tflite"
)
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print("Model loaded!")

def detect_trash(frame, confidence_threshold=0.45):
    img = cv2.resize(frame, (320, 320))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0]

    boxes = []
    confidences = []
    for det in output:
        confidence = float(det[4])
        if confidence > confidence_threshold:
            cx = float(det[0]) / 320
            cy = float(det[1]) / 320
            w = float(det[2]) / 320
            h = float(det[3]) / 320
            # Ignore tiny boxes — likely false detections
            if w > 0.05 and h > 0.05:
                boxes.append([cx - w/2, cy - h/2, w, h])
                confidences.append(confidence)

    if boxes:
        indices = cv2.dnn.NMSBoxes(
            boxes, confidences,
            score_threshold=0.45,
            nms_threshold=0.3
        )
        final = []
        for i in indices:
            b = boxes[i]
            final.append({
                'confidence': confidences[i],
                'x1': b[0], 'y1': b[1],
                'w': b[2], 'h': b[3]
            })
        return final
    return []

cap = cv2.VideoCapture(0)
detection_history = []
last_report_time = 0
print("Webcam started — press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    raw = detect_trash(frame)
    detection_history.append(len(raw) > 0)
    if len(detection_history) > 5:
        detection_history.pop(0)
    detections = raw if sum(detection_history) >= 3 else []

    # Send report max once every 10 seconds
    if detections:
        current_time = time.time()
        if current_time - last_report_time > 10:
            try:
                lat, lon = get_location()
                requests.post('http://127.0.0.1:5000/report', json={
                    'lat': lat,
                    'lon': lon,
                    'confidence': detections[0]['confidence'],
                    'photo': ''
                })
                last_report_time = current_time
                print(f"Report sent! Location: {lat}, {lon} | Confidence: {detections[0]['confidence']:.2f}")
            except:
                print("Dashboard not running — start app.py first")

    for d in detections:
        x1 = int(d['x1'] * w)
        y1 = int(d['y1'] * h)
        bw = int(d['w'] * w)
        bh = int(d['h'] * h)
        cv2.rectangle(frame, (x1, y1),
                      (x1 + bw, y1 + bh), (0, 0, 255), 2)
        cv2.putText(frame,
                    f"Trash {d['confidence']:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 255), 2)

    status = f"Trash DETECTED! ({len(detections)})" if detections else "No trash detected"
    color = (0, 0, 255) if detections else (0, 255, 0)
    cv2.putText(frame, status, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, color, 2)

    cv2.imshow('TrashGlasses — Live Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()