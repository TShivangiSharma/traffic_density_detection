import cv2
import os

def extract_frames(video_path, output_folder):
    print(f"Processing video: {video_path}")

    # Check if the video file exists
    if not os.path.exists(video_path):
        print(f"Error: {video_path} not found!")
        return

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    print(f"Output folder created: {output_folder}")

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Unable to open video {video_path}")
        return

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("End of video reached or no frames found.")
            break  # Exit loop when video ends

        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        print(f"Saved frame: {frame_path}")  # Debugging print

        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    print(f"Extracted {frame_count} frames from {video_path}")

# Run extraction for both videos
#extract_frames("high_traffic.mp4", "dataset/more_traffic/")
extract_frames("low_traffic.mp4", "dataset/less_traffic/")
