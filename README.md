# 🧠 Liver Fibrosis Detection System (Full-Stack AI Web App)
### Deep Learning • Medical AI • Full-Stack ML Deployment

An end-to-end AI-powered web application that detects liver fibrosis stages (F0–F4) from ultrasound images using a deep learning model based on EfficientNet architecture.  
The system integrates deep learning inference, secure user authentication, database storage, and an interactive frontend to simulate real-world clinical decision support.

---

## 🚀 Project Overview
Liver fibrosis is a progressive liver disease that can lead to cirrhosis and liver failure if not detected early. Manual ultrasound interpretation can be difficult due to subtle texture variations between fibrosis stages.

This project presents a complete AI-enabled diagnostic support system that allows users to upload ultrasound images and receive automated fibrosis stage predictions along with confidence scores and historical tracking.

The goal is to bridge deep learning research with real-world deployment by building a production-style ML web application.

---

## 🏗 System Architecture

### Complete ML System Pipeline
1. User Authentication (Login/Register)  
2. Image Upload via Web Interface  
3. Backend Image Processing  
4. EfficientNet Model Inference  
5. Stage Prediction & Confidence Score  
6. Prediction Storage in Database  
7. Results Dashboard & History Tracking  

---

## 🧠 Deep Learning Model

**Architecture Used:** EfficientNet-based CNN  
**Task:** Multi-class classification (F0–F4)

### Why EfficientNet?
- High accuracy with fewer parameters  
- Strong performance in comparative study  
- Efficient for deployment  
- Better generalization on medical images  

### Model Capabilities
- Predict fibrosis stage from ultrasound images  
- Returns probability distribution across classes  
- Optimized for real-time inference  
- Integrated into backend API  

---

## 🔐 Authentication System
Secure login and registration implemented using Flask-Login.

### Features
- User registration & login  
- Password hashing  
- Session management  
- Protected routes  
- User-specific prediction history  

---

## 🗄 Database Integration
SQLite database integrated using Flask-SQLAlchemy.

### Tables

**User**
- id  
- full name  
- email  
- password hash  
- created_at  

**Prediction**
- uploaded image  
- predicted stage  
- confidence  
- probability distribution  
- timestamp  
- linked user  

---

## 🖼 Image Processing Pipeline
1. File validation (JPG/PNG)  
2. Secure filename handling  
3. Image resizing (224×224)  
4. RGB conversion  
5. Tensor conversion  
6. Model inference  

---

## 📊 Prediction Output
- Predicted fibrosis stage  
- Confidence score  
- Probability distribution  
- Uploaded image preview  
- Saved prediction history  

---

## 🌐 Web Application Features

### User Features
- Register & login  
- Upload ultrasound image  
- View prediction result  
- View prediction history  
- Individual report page  

### Backend Features
- Model loading & caching  
- Secure file upload handling  
- Error handling  
- User-specific data storage  
- Modular Flask architecture  

---

## 🛠 Tech Stack

### AI & ML
- Python  
- TensorFlow / Keras  
- EfficientNet  
- NumPy  
- PIL  

### Backend
- Flask  
- Flask-SQLAlchemy  
- Flask-Login  

### Database
- SQLite  

### Frontend
- HTML  
- CSS  
- Bootstrap  
- Jinja Templates  

### Tools
- VS Code  
- Git & GitHub  
- Jupyter Notebook  

---

## 📁 Project Structure
```
project/
│
├── app.py
├── liver_fibrosis_stage_model.h5
├── label_map.json
├── instance/
│   └── app.db
├── static/
│   └── uploads/
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── home.html
│   ├── predict.html
│   ├── history.html
│   └── report.html
└── README.md
```

---

## 🔒 Engineering Practices
- Password hashing for authentication  
- Secure file uploads  
- Unique file naming  
- User-based access control  
- Database relationship mapping  
- Debug-friendly error handling  

---

## 💡 Skills Demonstrated
- End-to-end ML system development  
- Deep learning model deployment  
- Flask backend development  
- Authentication & database handling  
- Real-world ML system architecture  
- Medical AI application  

---

## 🔮 Future Improvements
- Cloud deployment (AWS/GCP)  
- Docker containerization  
- PostgreSQL integration  
- Grad-CAM visualization  
- Mobile-friendly UI  

---

## 👩‍💻 Author
**Uma MP**  
AI/ML Engineer | Data Science | Computer Vision  

Passionate about building real-world AI systems combining machine learning and full-stack development.
