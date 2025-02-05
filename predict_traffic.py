# predict_traffic.py

from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import cv2
import os

# Load the trained model
model = load_model('traffic_detection_model.h5')  # Ensure this path is correct

# Function to preprocess the image before prediction
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust the target_size as per your model's input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image
    return img_array

# Predict function to detect traffic
def predict_traffic(img_path):
    img_array = preprocess_image(img_path)
    prediction = model.predict(img_array)

    # If prediction > 0.5, classify as "High Traffic"
    if prediction[0] > 0.5:
        print("High Traffic")
    else:
        print("Low Traffic")

# Example usage (You can replace this with the video processing part later)
img_path = 'sample2_image.jpg'  # Put a test image path here
predict_traffic(img_path)

