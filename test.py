import cv2

video_path = "high_traffic.mp4"  # Change filename if converted

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: OpenCV cannot read this video file.")
else:
    print("Success: Video opened!")
cap.release()
