import os, json, uuid
from datetime import datetime

import numpy as np
from PIL import Image

from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

import tensorflow as tf

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)
DB_PATH = os.path.join(INSTANCE_DIR, "app.db")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

MODEL_PATH = os.path.join(BASE_DIR, "liver_fibrosis_stage_model.h5")
LABEL_MAP_PATH = os.path.join(BASE_DIR, "label_map.json")

app = Flask(__name__)
app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.context_processor
def inject_now():
    return {"datetime": datetime}

# -----------------------------
# Database Models
# -----------------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(180), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    image_filename = db.Column(db.String(255), nullable=False)
    stage = db.Column(db.String(20), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    probs_json = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    user = db.relationship("User", backref=db.backref("predictions", lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# -----------------------------
# Model + Labels (Debug friendly)
# -----------------------------
_model = None
_model_err = ""
_class_names = ["F0", "F1", "F2", "F3", "F4"]

def load_label_map():
    global _class_names
    try:
        if os.path.exists(LABEL_MAP_PATH):
            with open(LABEL_MAP_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
            _class_names = data.get("class_names", _class_names)
    except Exception:
        pass

def get_model():
    """
    Loads model once and caches it.
    Uses compile=False to avoid many H5 load issues (loss/metrics mismatch).
    Also stores a readable error message into _model_err for UI debugging.
    """
    global _model, _model_err

    if _model is not None:
        return _model

    if not os.path.isfile(MODEL_PATH):
        _model_err = f"Model file not found at: {MODEL_PATH}"
        print(_model_err)
        return None

    try:
        print("✅ Loading model from:", MODEL_PATH)
        _model = tf.keras.models.load_model(MODEL_PATH, compile=False)  # ✅ IMPORTANT
        _model_err = ""
        print("✅ Model loaded successfully.")
        return _model
    except Exception as e:
        _model_err = f"{type(e).__name__}: {e}"
        print("❌ Model load error:", _model_err)
        return None

# -----------------------------
# Helpers
# -----------------------------
def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(pil_img: Image.Image, target_size=(224, 224)) -> np.ndarray:
    img = pil_img.convert("RGB").resize(target_size)
    arr = np.array(img).astype("float32")  # keep 0..255

    # ✅ If your training used rescale=1./255 (0..1), uncomment:
    # arr = arr / 255.0

    arr = np.expand_dims(arr, axis=0)
    return arr

# -----------------------------
# Routes
# -----------------------------
# -----------------------------
# Routes (UPDATED FLOW)
# -----------------------------

# -----------------------------
# Routes (FINAL REQUIRED FLOW)
# -----------------------------

@app.route("/")
def index():
    # App should start with Login page.
    # If already logged in, go to Home.
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    # If already logged in, go directly to Home
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid email or password.", "error")
            return redirect(url_for("login"))

        login_user(user)
        flash("Logged in successfully.", "success")
        return redirect(url_for("home"))   # ✅ after login → home

    return render_template("login.html")


@app.route("/home")
@login_required
def home():
    return render_template("home.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.", "success")
    return redirect(url_for("login"))      # ✅ after logout → login


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        if not full_name or not email or not password:
            flash("Please fill all fields.", "error")
            return redirect(url_for("register"))

        if password != confirm:
            flash("Passwords do not match.", "error")
            return redirect(url_for("register"))

        if User.query.filter_by(email=email).first():
            flash("Email already registered. Please login.", "error")
            return redirect(url_for("login"))

        user = User(
            full_name=full_name,
            email=email,
            password_hash=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        flash("Account created successfully. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/predict", methods=["GET", "POST"])
@login_required
def predict():
    load_label_map()
    model = get_model()

    if request.method == "POST":
        if model is None:
            flash(f"Model not loaded. Path: {MODEL_PATH}. Error: {_model_err}", "error")
            return redirect(url_for("predict"))

        if "image" not in request.files:
            flash("No file selected.", "error")
            return redirect(url_for("predict"))

        file = request.files["image"]
        if file.filename == "":
            flash("No file selected.", "error")
            return redirect(url_for("predict"))

        if not allowed_file(file.filename):
            flash("Only JPG, JPEG, PNG files are allowed.", "error")
            return redirect(url_for("predict"))

        ext = secure_filename(file.filename).rsplit(".", 1)[1].lower()
        unique_name = f"{uuid.uuid4().hex}.{ext}"
        save_path = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
        file.save(save_path)

        try:
            pil_img = Image.open(save_path)
            x = preprocess_image(pil_img, target_size=(224, 224))
            probs = model.predict(x, verbose=0)[0]
        except Exception as e:
            flash(f"Prediction failed: {type(e).__name__}: {e}", "error")
            return redirect(url_for("predict"))

        pred_id = int(np.argmax(probs))
        stage = _class_names[pred_id] if pred_id < len(_class_names) else str(pred_id)
        confidence = float(probs[pred_id])

        probs_dict = {
            (_class_names[i] if i < len(_class_names) else str(i)): float(probs[i])
            for i in range(len(probs))
        }

        row = Prediction(
            user_id=current_user.id,
            image_filename=unique_name,
            stage=stage,
            confidence=confidence,
            probs_json=json.dumps(probs_dict)
        )
        db.session.add(row)
        db.session.commit()

        flash("Prediction completed.", "success")
        return redirect(url_for("report", pred_id=row.id))

    return render_template("predict.html", model_ready=(model is not None), class_names=_class_names)

@app.route("/history")
@login_required
def history():
    rows = (Prediction.query
            .filter_by(user_id=current_user.id)
            .order_by(Prediction.created_at.desc())
            .all())
    return render_template("history.html", rows=rows)

@app.route("/report/<int:pred_id>")
@login_required
def report(pred_id):
    row = Prediction.query.get_or_404(pred_id)
    if row.user_id != current_user.id:
        abort(403)
    probs = json.loads(row.probs_json)
    probs_sorted = sorted(probs.items(), key=lambda kv: kv[1], reverse=True)
    return render_template("report.html", row=row, probs_sorted=probs_sorted)

# -----------------------------
# Init DB
# -----------------------------
def ensure_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    ensure_db()
    app.run(debug=True)
