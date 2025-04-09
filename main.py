import cv2
import os

video_path = r'cam8.avi'
output_folder = 'frames_8'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps

for sec in range(int(duration)):
    cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    success, frame = cap.read()
    if success:
        cv2.imwrite(f"{output_folder}/frame_{sec+1:02d}.jpg", frame)

cap.release()
