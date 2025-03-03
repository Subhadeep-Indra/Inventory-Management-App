!pip install ultralytics
from ultralytics import YOLO

from google.colab import drive
drive.mount('/content/gdrive',  force_remount=True)

# Load a pre-trained YOLOv8 model or start from scratch
model = YOLO('yolov8n.pt')  # Use 'n' for Nano, or 's', 'm', 'l', 'x' for different sizes

# Train on your custom dataset
model.train(data='/content/gdrive/MyDrive/data.yaml', epochs=50)

# Validate the model (optional)
metrics = model.val()

import locale
def getpreferredencoding(do_setlocale = True):
    return "UTF-8"
locale.getpreferredencoding = getpreferredencoding
!ls runs/detect/train2/

from IPython.display import Image
Image('runs/detect/train2/confusion_matrix.png')

#Accuracy on Validation Dataset
import numpy as np

# Example confusion matrix (replace with actual values from your matrix)
confusion_matrix = np.array([
    [70, 1, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 48, 7, 17, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 53, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 163, 8, 11, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 82, 6, 18, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 60, 2, 19, 0, 0, 0, 0],
    [11, 0, 0, 0, 0, 0, 74, 17, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 84, 20, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 60, 12, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 160, 22, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 100, 27],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 76, 10]
])

# Calculate accuracy
true_positives = np.trace(confusion_matrix)  # Sum of diagonal elements
total_predictions = np.sum(confusion_matrix)  # Sum of all elements
accuracy = true_positives / total_predictions

print(f"Accuracy: {accuracy * 100:.2f}%")

Accuracy: 76.63%
import os
import cv2
import matplotlib.pyplot as plt

# Define the output directory
output_dir = '/content/runs/detect/train2'

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(output_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Loop through and display each image
for image_file in image_files:
    img_path = os.path.join(output_dir, image_file)
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(8, 8))
    plt.imshow(img_rgb)
    plt.axis('off')  # Hide axes
    plt.title(image_file)  # Display image name as title
    plt.show()

#Visualise the Result
import matplotlib.pyplot as plt
import cv2
import numpy as np

# Define the function to draw bounding boxes and count the fruits
def draw_boxes_and_count(results, img):
    # Initialize counts for each class
    class_counts = {
        'Fresh apple': 0, 'Fresh banana': 0, 'Fresh guava': 0, 'Fresh lemon': 0, 'Fresh orange': 0, 'Fresh pomegranate': 0,
        'Spoiled apple': 0, 'Spoiled banana': 0, 'Spoiled guava': 0, 'Spoiled lemon': 0, 'Spoiled orange': 0, 'Spoiled pomegranate': 0
    }

    # Define colors for the bounding boxes
    class_colors = {
        'Fresh apple': (0, 255, 0), 'Fresh banana': (0, 255, 0), 'Fresh guava': (0, 255, 0), 'Fresh lemon': (0, 255, 0),
        'Fresh orange': (0, 255, 0), 'Fresh pomegranate': (0, 255, 0), 'Spoiled apple': (0, 0, 255), 'Spoiled banana': (0, 0, 255),
        'Spoiled guava': (0, 0, 255), 'Spoiled lemon': (0, 0, 255), 'Spoiled orange': (0, 0, 255), 'Spoiled pomegranate': (0, 0, 255)
    }

    # Loop through each detection and draw boxes
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])

            # Map the class index to the class name
            if cls == 0:
                class_name = 'Fresh apple'
            elif cls == 1:
                class_name = 'Fresh banana'
            elif cls == 2:
                class_name = 'Fresh guava'
            elif cls == 3:
                class_name = 'Fresh lemon'
            elif cls == 4:
                class_name = 'Fresh orange'
            elif cls == 5:
                class_name = 'Fresh pomegranate'
            elif cls == 6:
                class_name = 'Spoiled apple'
            elif cls == 7:
                class_name = 'Spoiled banana'
            elif cls == 8:
                class_name = 'Spoiled guava'
            elif cls == 9:
                class_name = 'Spoiled lemon'
            elif cls == 10:
                class_name = 'Spoiled orange'
            elif cls == 11:
                class_name = 'Spoiled pomegranate'

            # Draw bounding box and count the detection
            color = class_colors[class_name]
            cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness=3)
            class_counts[class_name] += 1

    return img, class_counts

# List of image paths
image_paths = [
    '/content/gdrive/MyDrive/test/images/IMG20200730132545_jpg.rf.5be933e398431ec343a4faf26adbf7d0.jpg',
    '/content/gdrive/MyDrive/test/images/IMG20200728131742_jpg.rf.a9a36dad7d33bc800f98fa8685bfe0d0.jpg',
    '/content/gdrive/MyDrive/test/images/IMG20200728125225_jpg.rf.67e07fdeda364b304f4f301b7dba1fc0.jpg'
]

# Loop through each image, process it, and display the results with counts beside the image
for img_path in image_paths:
    # Run inference on each image
    results = model(img_path)  # Assuming model is already loaded

    # Read the image and draw bounding boxes with counts
    img = cv2.imread(img_path)
    img_with_boxes, class_counts = draw_boxes_and_count(results, img.copy())

    # Set up matplotlib figure with two subplots (image + text list)
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Plot the image with bounding boxes
    ax[0].imshow(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB))
    ax[0].axis('off')  # Turn off axis
    ax[0].set_title("Detected Fruits")

    # Display the class counts as a list beside the image
    count_text = "\n".join([f"{fruit}: {count}" for fruit, count in class_counts.items()])
    ax[1].text(0.1, 0.9, count_text, fontsize=12, ha='left', va='top', wrap=True)
    ax[1].axis('off')  # Turn off axis for the second subplot

    plt.tight_layout()
    plt.show()
