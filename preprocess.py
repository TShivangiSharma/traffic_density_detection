import cv2
import os
import numpy as np

# Define input and output directories
input_dirs = {
    "more_traffic": "dataset/more_traffic",
    "less_traffic": "dataset/less_traffic"
}
output_dir = "processed_dataset"
os.makedirs(output_dir, exist_ok=True)

# Image size for resizing
IMG_SIZE = (224, 224)

def preprocess_images():
    for label, input_dir in input_dirs.items():
        output_folder = os.path.join(output_dir, label)
        os.makedirs(output_folder, exist_ok=True)

        for img_name in os.listdir(input_dir):
            img_path = os.path.join(input_dir, img_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f"Skipping {img_name} (unable to read)")
                continue

            # Resize and normalize
            img = cv2.resize(img, IMG_SIZE)
            img = img / 255.0  # Normalize

            # Save preprocessed image
            output_path = os.path.join(output_folder, img_name)
            cv2.imwrite(output_path, img * 255)  # Convert back to 0-255 scale
            print(f"Processed: {output_path}")

preprocess_images()

