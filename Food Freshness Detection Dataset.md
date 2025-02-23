# Food Freshness Detection Dataset for YOLOv8 Fine-Tuning

## Dataset Overview

This dataset was made to fine-tune a YOLOv8 model for classifying fruits as fresh or rotten. Annotated images of six ethnic fruit types are provided with bounding boxes highlighting the relevant regions.

### Features:
- **Total Images**: 1059
- **Annotations**: 5850
- **Image Dimensions**: Median size of 192 x 256 pixels
- **Mean Annotations per Image**: 5.5
- **Classes**: Fresh, Spoiled

### Annotation Details:
| Fruit         | Fresh | Spoiled |
|---------------|-------|---------|
| Lemon         | 903   | 864     |
| Banana        | 596   | 509     |
| Oranges       | 479   | 486     |
| Apple         | 406   | 313     |
| Pomegranate   | 305   | 380     |
| Guava         | 291   | 318     |

---

## Dataset Preparation

### 1. Preprocessing Steps
- **Data Cleaning**: Removal of incomplete or incorrect annotations.
- **Data Integration**: The union of multiple datasets for variety.
- **Data Reduction**: Lowering image sizes for computational ease.
- **Data Augmentation**: General transformations like rotation, scale, and flip applied to images.

### 2. Splitting of Dataset
- **Training set**: 70% (for model development)
- **Validation set**: 20% (for tuning and lessening of overfitting)
- **Test set**: 10% (for unprejudiced performance evaluation)

### 3. Annotation Process
- **Bounding Boxes**: Areas marked were of fresh and spoiled fruits.
- **Classes**: Either "Fresh" or "Spoiled".
- **YOLOv8 Integration**: The annotations are written in a way that input is directed into the YOLOv8 pipeline.

---

## Visualization and Interpretation

### Visualization Method
- **Bounding Box**:
  - Green for fresh fruits
  - Red for rotten fruits
- **Counting Display**: The detected number of fresh and rotten fruits is shown directly in the image.
- **Visualization Tools**: Annotated images were displayed using Matplotlib.

### Sample Annotated Images
Here are some sample annotated images showcasing fresh and spoiled fruits with bounding boxes:

---

## Accessing the Dataset

This dataset is hosted on Google Drive and can be accessed using the following link:  
📂 [Google Drive Folder](https://drive.google.com/drive/folders/1MRWZBSwpkUTzB07UJSNMyDgx1PO8GM_i?usp=sharing)