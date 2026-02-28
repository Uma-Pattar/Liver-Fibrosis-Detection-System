# 🧠 Deep Learning Frameworks for Liver Fibrosis Detection

A comprehensive comparative study of multiple deep learning architectures for multi-class liver fibrosis staging (F0–F4) using B-mode ultrasound images.

This project evaluates CNN-based transfer learning models and Vision Transformers to identify the most effective architecture for medical image classification of liver fibrosis.

---

## 🚀 Project Highlights
- Comparative study of **5 deep learning models**
- Medical imaging classification using ultrasound data
- Transfer learning vs custom CNN analysis
- Vision Transformer dual-branch architecture
- Grad-CAM explainability for model interpretation
- Class imbalance handling using weighted sampling
- Stratified cross-validation evaluation

---

## 🏥 Problem Statement
Liver fibrosis is a progressive disease that can lead to cirrhosis and liver failure if not detected early.  
Manual ultrasound interpretation is difficult due to subtle texture differences between fibrosis stages.

This project builds an AI-based system to automatically classify liver fibrosis stages (F0–F4) from ultrasound images.

---

## 🧠 Models Implemented
- EfficientNet-B0 (Best performing)
- ResNet50
- MobileNetV3-Large
- Custom CNN (baseline)
- Dual-Branch Vision Transformer (RGB + CLAHE)

---

## 📊 Results Summary

| Model | Accuracy | Macro F1 Score |
|------|---------|---------------|
| EfficientNet-B0 | 97.88% | 0.971 |
| ResNet50 | 97.31% | 0.964 |
| MobileNetV3 | 97.47% | 0.963 |
| Dual-Branch ViT | 94.86% | 0.929 |
| Custom CNN | 64.66% | 0.575 |

EfficientNet-B0 achieved the best performance across stratified cross-validation.

---

## 🧾 Dataset
- Liver Fibrosis Ultrasound Dataset (Kaggle)
- 6323 B-mode ultrasound images
- 5 classes: F0–F4
- Imbalanced dataset handled using weighted sampling

---

## ⚙️ Tech Stack
- Python
- PyTorch
- OpenCV
- Albumentations
- Scikit-learn
- Matplotlib
- Vision Transformers (ViT)
- Grad-CAM Explainability

---

## 📈 Evaluation Metrics
- Accuracy
- Macro F1 Score
- Confusion Matrix
- One-vs-Rest AUC
- Classification Report

---

## 🔍 Explainability
Grad-CAM visualization used to interpret CNN predictions and highlight important liver regions influencing model decisions.

---

## 📂 Repository Structure
```
├── liver_fibrosis_models.ipynb
├── research_paper.pdf
├── requirements.txt
├── results/
└── README.md
```

---

## 📜 Research Paper
This work is part of our research study:  
**"A Comparative Study of Deep Learning Frameworks for Liver Fibrosis Detection Using Ultrasound Images"**

---

## 👩‍💻 Author
**Uma MP**  
Information Science Engineering  
AI & Data Science Enthusiast | MERN Developer  

---

## ⭐ Future Improvements
- Deploy as web app for clinical usage
- Add model ensemble
- Hyperparameter tuning
- Larger dataset training
- Real-time ultrasound prediction system
