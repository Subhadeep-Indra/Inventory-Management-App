# 🍎 Food Freshness Detection Dataset for YOLOv8 🚀

## 📂 Dataset Overview

This dataset is designed to fine-tune a **YOLOv8 model** for classifying fruits as **fresh** or **rotten**. It includes annotated images of six ethnic fruit types with bounding boxes highlighting the relevant regions.

---

### 🎯 Key Features
| Feature                  | Details                        |
|--------------------------|--------------------------------|
| **Total Images**         | 1059                          |
| **Annotations**          | 5850                          |
| **Image Dimensions**     | Median size of 192 x 256 pixels |
| **Mean Annotations/Image** | 5.5                          |
| **Classes**              | Fresh, Spoiled                |

---

### 📊 Annotation Details
| Fruit         | Fresh | Spoiled |
|---------------|-------|---------|
| 🍋 Lemon      | 903   | 864     |
| 🍌 Banana     | 596   | 509     |
| 🍊 Oranges    | 479   | 486     |
| 🍎 Apple      | 406   | 313     |
| 🍈 Pomegranate| 305   | 380     |
| 🥑 Guava      | 291   | 318     |

---

## 🛠️ Dataset Preparation

### 1. Preprocessing Steps
- **Data Cleaning**: Removal of incomplete or incorrect annotations.
- **Data Integration**: Combining multiple datasets for variety.
- **Data Reduction**: Resizing images for computational efficiency.
- **Data Augmentation**: Applying transformations like rotation, scaling, and flipping.

### 2. Dataset Splitting
| Split          | Percentage | Purpose                          |
|----------------|------------|----------------------------------|
| **Training**   | 70%        | Model development                |
| **Validation** | 20%        | Hyperparameter tuning            |
| **Test**       | 10%        | Unbiased performance evaluation  |

### 3. Annotation Process
- **Bounding Boxes**: Marked areas for fresh and spoiled fruits.
- **Classes**: Labeled as "Fresh" or "Spoiled".
- **YOLOv8 Integration**: Annotations formatted for YOLOv8 pipeline.

---

## 🖼️ Visualization and Interpretation

### Visualization Method
- **Bounding Box Colors**:
  - 🟢 Green for fresh fruits
  - 🔴 Red for rotten fruits
- **Counting Display**: Number of fresh and rotten fruits displayed on the image.
- **Tools**: Annotated images visualized using **Matplotlib**.

---

## 🖼️ Sample Annotated Images

Here are some sample annotated images showcasing fresh and spoiled fruits with bounding boxes:

### 🍌 Bananas
<img src="https://github.com/user-attachments/assets/68d3daac-0663-46bc-93c3-ebdb24267a7c" alt="Bananas" width="400" style="border: 2px solid #ddd; border-radius: 10px;"/>

### 🍋 Lemons
<img src="https://github.com/user-attachments/assets/e9b5d747-e94a-4f12-962d-493e0a66186d" alt="Lemons" width="400" style="border: 2px solid #ddd; border-radius: 10px;"/>

### 🍊 Oranges
<img src="https://github.com/user-attachments/assets/e3ce5d54-5d70-4ad5-aa07-7d855c593d92" alt="Oranges" width="400" style="border: 2px solid #ddd; border-radius: 10px;"/>

### 🥑 Guavas
<img src="https://github.com/user-attachments/assets/4463d11c-2d68-4af8-bd48-bd30f1ad4141" alt="Guavas" width="400" style="border: 2px solid #ddd; border-radius: 10px;"/>

### 🍎 Apples
<img src="https://github.com/user-attachments/assets/8e5b88be-4685-4672-8534-d1301087bc8f" alt="Apples" width="400" style="border: 2px solid #ddd; border-radius: 10px;"/>

### 🍈 Pomegranates
<img src="https://github.com/user-attachments/assets/f54aa7f9-71b1-4e0f-8c6b-47538593c4d1" alt="Pomegranates" width="400" style="border: 2px solid #ddd; border-radius: 10px;"/>

---

## 📂 Accessing the Dataset

This dataset is hosted on **Google Drive** and can be accessed using the following link:  
📂 [Google Drive Folder](https://drive.google.com/drive/folders/1MRWZBSwpkUTzB07UJSNMyDgx1PO8GM_i?usp=sharing)

---

