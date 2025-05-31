from ultralytics import YOLO
import cv2
import os

def detect_players_and_ball(frame_dir: str, output_dir: str = "data/detections"):
    os.makedirs(output_dir, exist_ok=True)
    model = YOLO("yolov8n.pt")  # 또는 yolov8s.pt (더 정확하지만 느림)

    frame_files = sorted(os.listdir(frame_dir))

    for filename in frame_files:
        frame_path = os.path.join(frame_dir, filename)
        frame = cv2.imread(frame_path)

        results = model(frame)[0]  # 첫 번째 프레임 결과만 사용

        for box in results.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]

            if label in ["person", "sports ball"]:
                # bounding box 그리기
                xyxy = box.xyxy[0].tolist()
                x1, y1, x2, y2 = map(int, xyxy)
                color = (0, 255, 0) if label == "person" else (0, 0, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # 저장
        save_path = os.path.join(output_dir, filename)
        cv2.imwrite(save_path, frame)

    print(f"✅ Detection results saved to: {output_dir}")
