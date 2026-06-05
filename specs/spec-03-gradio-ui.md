# Spec 03 — Gradio UI (`app.py`)

Web form with human-readable labels. Sliders for numeric inputs, dropdowns for categorical.

## Inputs

| Full Label (UI) | Dataset col | Component | Range / Options |
|---|---|---|---|
| Age | `age` | Slider | 20–80 |
| Resting Blood Pressure (mm Hg) | `trestbps` | Slider | 80–200 |
| Serum Cholesterol (mg/dl) | `chol` | Slider | 100–600 |
| Max Heart Rate Achieved | `thalach` | Slider | 60–220 |
| ST Depression (Exercise vs Rest) | `oldpeak` | Slider | 0.0–6.2, step 0.1 |
| Biological Sex | `sex` | Dropdown | Female=0, Male=1 |
| Chest Pain Type | `cp` | Dropdown | Typical Angina=0, Atypical Angina=1, Non-anginal Pain=2, Asymptomatic=3 |
| Fasting Blood Sugar >120 mg/dl | `fbs` | Dropdown | No=0, Yes=1 |
| Resting ECG Results | `restecg` | Dropdown | Normal=0, ST-T Abnormality=1, LV Hypertrophy=2 |
| Exercise Induced Angina | `exang` | Dropdown | No=0, Yes=1 |
| Slope of Peak Exercise ST Segment | `slope` | Dropdown | Upsloping=0, Flat=1, Downsloping=2 |
| Number of Major Vessels | `ca` | Dropdown | 0, 1, 2, 3, 4 |
| Thalassemia Type | `thal` | Dropdown | Normal=0, Fixed Defect=1, Reversible Defect=2, Unknown=3 |

## Output
```
Result: Heart Disease Detected  (Confidence: 87.3%)
```

## Edge Cases
- Dropdown values are strings in Gradio — map them to ints before passing to `predict()`
- `oldpeak` slider returns a float — pass directly, scaler handles it
- Port 7860 already in use — Gradio auto-increments to 7861; no fix needed
- If `predict.py` fails to import (missing artifacts), show a clear error message before launching UI

## Done when
UI loads at `localhost:7860`, sliders and dropdowns work, prediction displays on submit
