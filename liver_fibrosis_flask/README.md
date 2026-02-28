# Liver Fibrosis Staging (Flask + SQLite)

Pages:
- Login, Register
- Home, About
- Prediction (upload image)
- History (all predictions)
- Report (per prediction)
- Logout

## Put your trained model files in project root
- `liver_fibrosis_stage_model.h5`
- `label_map.json` (sample included)

If the model file is missing, the app still runs but Prediction shows a warning.

## Install & Run
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open: http://127.0.0.1:5000

SQLite DB is created at: `instance/app.db`
