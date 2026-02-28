# 🧠 Liver Fibrosis Detection using Deep Learning & Vision Transformers  
### Medical AI | Computer Vision | Research-Based Comparative Study

A comprehensive deep learning project focused on **multi-class liver fibrosis staging (F0–F4)** using B-mode ultrasound images.  
This repository presents a full comparative evaluation of CNN transfer learning architectures and Vision Transformers for medical image classification.

> Designed as a research-grade implementation with strong emphasis on performance, interpretability, and real-world deployment feasibility.

---

# 🚀 Project Overview
Liver fibrosis is a progressive liver disease that can lead to cirrhosis and liver failure if not detected early.  
Manual ultrasound interpretation is challenging due to subtle texture differences between fibrosis stages.

This project builds an **AI-powered diagnostic support system** that classifies liver fibrosis stages automatically using deep learning.

---

# 🏆 Key Highlights
✔ Comparative study of **5 deep learning architectures**  
✔ Medical imaging classification using ultrasound data  
✔ Transfer learning vs custom CNN analysis  
✔ Vision Transformer dual-branch fusion model  
✔ Grad-CAM explainability visualization  
✔ Class imbalance handling with weighted sampling  
✔ Stratified cross-validation for robust evaluation  
✔ Research-paper-based implementation  

---

# 🧠 Models Implemented
This project evaluates multiple architectures under a unified pipeline:

| Model | Type |
|------|------|
| EfficientNet-B0 | Transfer Learning CNN (Best Performer) |
| ResNet50 | Deep Residual CNN |
| MobileNetV3-Large | Lightweight Deployment Model |
| Custom CNN | Built-from-scratch baseline |
| Dual-Branch Vision Transformer | RGB + CLAHE fusion |

---

# 📊 Performance Comparison

| Model | Accuracy | Macro F1 Score | AUC |
|------|---------|---------------|-----|
| 🥇 EfficientNet-B0 | 97.88% | 0.971 | 0.998 |
| ResNet50 | 97.31% | 0.964 | 0.996 |
| MobileNetV3 | 97.47% | 0.963 | 0.998 |
| Dual-Branch ViT | 94.86% | 0.929 | 0.992 |
| Custom CNN | 64.66% | 0.575 | 0.897 |

**EfficientNet-B0 achieved the best overall performance** under stratified cross-validation.

---

# 🧾 Dataset Information
- Source: Kaggle Liver Fibrosis Ultrasound Dataset  
- Total Images: 6323  
- Classes: F0, F1, F2, F3, F4  
- Imaging Type: B-mode ultrasound  
- Challenge: Class imbalance + subtle inter-stage differences  

Imbalance handled using:
- WeightedRandomSampler  
- Class-weighted loss  

---

# 🧪 Methodology Pipeline
1. Data preprocessing & augmentation  
2. CLAHE enhancement for texture emphasis  
3. Transfer learning with pretrained CNNs  
4. Dual-branch ViT fusion architecture  
5. Class imbalance handling  
6. Stratified validation  
7. Grad-CAM explainability  

---

# 🔍 Explainable AI (XAI)
Grad-CAM visualization is used to highlight regions influencing predictions, ensuring model decisions align with relevant liver regions rather than noise/artifacts.

This improves **trust and transparency** for medical AI deployment.

---

# 🛠 Tech Stack

### Languages & Frameworks
- Python
- PyTorch
- OpenCV
- Albumentations
- Scikit-learn

### Deep Learning Models
- EfficientNet
- ResNet50
- MobileNetV3
- Vision Transformers (ViT)

### Visualization & Analysis
- Matplotlib
- Seaborn
- Grad-CAM

---

# 📁 Repository Structure
```
Liver-Fibrosis-Detection/
│
├── liverFibrosisStaging.ipynb
├── requirements.txt
├── README.md
│
├── results/
│   ├── EfficientNet-B0/
│   │   ├── confusion_matrix.png
│   │   ├── gradcam_outputs.png
│   │
│   ├── ResNet50/
│   │   ├── confusion_matrix.png
│   │   ├── gradcam_outputs.png
│   │   ├── training_loss.png
│   │   └── validation_metrics.png
│   │
│   ├── MobileNetV3/
│   │   ├── confusion_matrix.png
│   │   ├── training_loss.png
│   │   └── validation_metrics.png
│   │
│   ├── Custom_CNN/
│   │   ├── confusion_matrix.png
│   │   ├── training_loss.png
│   │   └── validation_metrics.png
│   │
│   └── Dual_ViT/
│       ├── confusion_matrix.png
│       ├── training_loss.png
│       └── validation_metrics.png
```

---

# 📜 Research Publication
**A Comprehensive Comparative Study of Deep Learning Frameworks for Liver Fibrosis Detection Using Ultrasound Images**

This repository accompanies our academic research work focusing on comparative performance evaluation of CNNs and Vision Transformers for medical imaging.

---

# 💡 Future Scope
- 🔬 Hyperparameter optimization & model ensemble  
- 🌐 Deploy as web-based clinical support tool  
- ☁️ Cloud deployment (Streamlit / Flask)  
- 📱 Lightweight mobile inference model  
- 🧠 Multimodal imaging integration  

---

# 👩‍💻 Author
**Uma MP**  
Information Science Engineering  
AI & Data Science Enthusiast | AI & ML Engineer | Computer Vision | Deep Learning  
Building real-world AI projects & research-driven solutions 

> Passionate about building intelligent systems that bridge research and real-world impact.

---

# ⭐ If you found this project interesting
Give this repo a star ⭐ and connect with me!
