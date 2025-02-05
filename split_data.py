import os
import shutil
import random

# Paths
input_dir = "processed_dataset"
output_dir = "split_dataset"

train_ratio = 0.8  # 80% train, 20% test

# Create train and test folders
for split in ["train", "test"]:
    for category in ["more_traffic", "less_traffic"]:
        os.makedirs(os.path.join(output_dir, split, category), exist_ok=True)

# Split data
for category in ["more_traffic", "less_traffic"]:
    images = os.listdir(os.path.join(input_dir, category))
    random.shuffle(images)  # Shuffle images randomly

    split_idx = int(len(images) * train_ratio)
    train_images, test_images = images[:split_idx], images[split_idx:]

    # Move images
    for img in train_images:
        shutil.copy(os.path.join(input_dir, category, img), os.path.join(output_dir, "train", category, img))

    for img in test_images:
        shutil.copy(os.path.join(input_dir, category, img), os.path.join(output_dir, "test", category, img))

print("Dataset split completed!")
