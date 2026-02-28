# 🧠 Liver Fibrosis Detection System  
### Deep Learning + Full-Stack Medical AI Web Application

An end-to-end AI-powered system for detecting liver fibrosis stages (F0–F4) from ultrasound images using a deep learning EfficientNet model integrated into a full-stack Flask web application.

This project demonstrates real-world ML deployment by combining deep learning, backend engineering, authentication systems, and database integration into one complete production-style system.

---

## 🚀 Project Overview

Liver fibrosis is a progressive disease that can lead to cirrhosis if not detected early.  
Manual ultrasound interpretation is difficult due to subtle texture variations.

This system allows users to:
- Upload liver ultrasound images  
- Get fibrosis stage prediction (F0–F4)  
- View confidence scores  
- Track prediction history  
- Access detailed reports  

The project simulates a real clinical decision-support web system powered by AI.

---

## 🧠 Deep Learning Model

**Model Used:** EfficientNet (best performing from comparative study)  
**Task:** Multi-class classification (F0–F4)

### Why EfficientNet?
- High accuracy with fewer parameters  
- Strong generalization on medical images  
- Efficient for real-time deployment  
- Lightweight and scalable  

### Model Capabilities
- Predict fibrosis stage from ultrasound image  
- Returns probability for all classes  
- Integrated into Flask backend  
- Real-time inference  

---

## 🌐 Full-Stack Features

### 👤 Authentication System
- User registration & login  
- Password hashing  
- Session management  
- Protected routes  
- User-specific prediction history  

### 🖼 Prediction System
- Upload ultrasound image  
- Model inference  
- Stage prediction with confidence  
- Probability distribution  
- Saved prediction history  

### 📊 Report System
- Individual prediction report  
- Stored results per user  
- Timestamp tracking  

---

## 🗄 Database Integration

SQLite database using Flask-SQLAlchemy.

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

Database file auto-created in:
```
instance/app.db
```

---

## 🛠 Tech Stack

### AI / ML
- Python  
- TensorFlow / Keras  
- EfficientNet  
- NumPy  
- PIL  

### Backend
- Flask  
- Flask-Login  
- Flask-SQLAlchemy  

### Frontend
- HTML  
- CSS  
- Bootstrap  
- Jinja Templates  

### Database
- SQLite  

### Tools
- VS Code  
- Jupyter Notebook  
- Git & GitHub  

---

## 📁 Project Structure
```
Liver_Fibrosis_Staging/
│
├── Dataset/
│   ├── F0 F1 F2 F3 F4 (training images)
│
├── liver_fibrosis_flask/
│   ├── app.py
│   ├── requirements.txt
│   ├── liver_fibrosis_stage_model.h5
│   ├── best_fibrosis.weights.h5
│   ├── label_map.json
│   ├── liver fibrosis.ipynb
│   │
│   ├── instance/
│   │   └── app.db
│   │
│   ├── static/
│   │   └── uploads/
│   │
│   └── templates/
│       ├── login.html
│       ├── register.html
│       ├── home.html
│       ├── predict.html
│       ├── history.html
│       └── report.html
```

---

## ▶️ Run Locally

Create virtual environment:
```
python -m venv .venv
```

Activate:

Windows:
```
.venv\Scripts\activate
```

Mac/Linux:
```
source .venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```

Run app:
```
python app.py
```

Open browser:
```
http://127.0.0.1:5000
```

---

## 💡 Skills Demonstrated
- End-to-end ML deployment  
- Deep learning model integration  
- Flask backend development  
- Authentication systems  
- Database design & ORM  
- Real-world ML system architecture  
- Medical AI application development  

---

## 🔮 Future Improvements
- Cloud deployment (AWS/GCP)  
- Docker containerization  
- PostgreSQL integration  
- Grad-CAM visualization  
- Mobile responsive UI  
- REST API integration  

---

## 👩‍💻 Author
**Uma MP**  
AI/ML Engineer • Data Science • Computer Vision  

Building real-world AI systems that combine machine learning with full-stack deployment.
