# Heart Disease Prediction

> **Disclaimer: This is a student/learning project built for educational purposes only. It is NOT a medical tool and should NOT be used to diagnose, treat, or make any health decisions. If you or anyone else has concerns about heart disease or any medical condition, please consult a qualified doctor or healthcare professional. This project makes no medical claims whatsoever.**

A machine learning web app that predicts whether a patient is likely to have heart disease based on medical details. Built with a Keras neural network and a Gradio web interface.

## How It Works

1. A neural network is trained on the Cleveland Heart Disease dataset (`heartdisease.py`)
2. The trained model, scaler, and column info are saved to `artifacts/`
3. A Gradio web UI (`app.py`) lets users enter patient details and get an instant prediction

## Features

- 13 medical input fields (sliders for numeric values, dropdowns for categorical)
- Shows prediction result with confidence percentage
- No retraining needed — model is loaded once from saved artifacts

## Inputs

| Field | Type |
|---|---|
| Age | Slider (20–80) |
| Resting Blood Pressure | Slider |
| Serum Cholesterol | Slider |
| Max Heart Rate Achieved | Slider |
| ST Depression | Slider |
| Biological Sex | Dropdown |
| Chest Pain Type | Dropdown |
| Fasting Blood Sugar >120 mg/dl | Dropdown |
| Resting ECG Results | Dropdown |
| Exercise Induced Angina | Dropdown |
| Slope of ST Segment | Dropdown |
| Number of Major Vessels | Dropdown |
| Thalassemia Type | Dropdown |

## Setup & Run

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model (generates artifacts/)
python heartdisease.py

# 4. Launch the web app
python app.py
```

Then open the local URL shown in the terminal (usually `http://127.0.0.1:7860`).

## Tech Stack

- **Keras / TensorFlow** — neural network model
- **scikit-learn** — data preprocessing (StandardScaler)
- **Gradio** — web UI
- **pandas / numpy** — data handling
