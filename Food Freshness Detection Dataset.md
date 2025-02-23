Food Freshness Detection Dataset for YOLOv8 Fine-Tuning
Dataset Overview

This dataset was made to fine-tune a YOLOv8 model for classifying fruits as fresh or rotten. Annotated images of six ethnic fruit types are with bounding boxes highlighting the relevant regions.

Some features include:

Total Images: 1059

Annotations: 5850

Image Dimensions: Median size of 192 x 256 pixels

Mean Annotations per Image: 5.5

Classes: Fresh, Spoiled

Annotation details:

Lemon: 903 fresher; 864 spoiled

Banana: 596 fresh, 509 spoiled

Oranges: 479 fresh, 486 rotten

Apple: 406 fresh, 313 spoiled

Pomegranate: 305 fresh; 380 rotten

Guava: 291 fresh, 318 rotting

Dataset Preparation
1. Preprocessing Steps

Data Cleaning: Removal of incomplete or incorrect annotations.

Data Integration: The union of multiple datasets for variety.

Data Reduction: Lowering image sizes for computational ease.

Data augmentation: General transformations like rotation, scale, and flip applied to images.

2. Splitting of Dataset

Training set: 70% (for model development)

Validation set: 20% (for tuning and lessening of overfitting)

Test set: 10% (for unprejudiced performance evaluation)

3. Annotation Process

Bounding Boxes: Areas marked were of fresh and spoiled fruits.

Classes: Either "Fresh" or "Spoiled".

YOLOv8 integration: The annotations are written in a way that input is directed into the YOLOv8 pipeline.

Looking and interpreting
Visualization Method

Annotated images analyzed using a specialized draw-and-count function:

Bounding Box:

Green for fresh fruits

Red for rotten fruits

Counting display: Made the detected number of fresh and rotten fruits show directly in the image.

Visualization Tools: Annotated images were displayed using Matplotlib.

Sample Annotated Images

Here are some sample annotated images showcasing fresh and spoiled fruits with bounding boxes:

Accessing the Dataset

This dataset is hosted on Google Drive and can be accessed by the following link:
📂 Google Drive folder.
