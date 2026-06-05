import os
import pickle
import numpy as np
import pandas as pd

_ARTIFACTS = "artifacts"
for _f in ["model.keras", "scaler.pkl", "columns.pkl"]:
    if not os.path.exists(os.path.join(_ARTIFACTS, _f)):
        raise FileNotFoundError(
            f"Missing artifact: {os.path.join(_ARTIFACTS, _f)}. "
            "Run heartdisease.py first to generate the artifacts folder."
        )

from tensorflow import keras  # noqa: E402 — import after path check

_model = keras.models.load_model(os.path.join(_ARTIFACTS, "model.keras"))
_scaler = pickle.load(open(os.path.join(_ARTIFACTS, "scaler.pkl"), "rb"))
_columns = pickle.load(open(os.path.join(_ARTIFACTS, "columns.pkl"), "rb"))

_NUMERIC = ["age", "trestbps", "chol", "thalach", "oldpeak", "slope"]
_CATEGORICAL = ["sex", "cp", "fbs", "restecg", "exang", "ca", "thal"]


def predict(age, trestbps, chol, thalach, oldpeak, slope,
            sex, cp, fbs, restecg, exang, ca, thal):
    """
    Returns (probability: float, label: str).
    Numeric args: raw values. Categorical args: integer category values.
    """
    row = dict.fromkeys(_columns, 0)

    for col, val in zip(_NUMERIC, [age, trestbps, chol, thalach, oldpeak, slope]):
        row[col] = val

    for col, val in zip(_CATEGORICAL, [sex, cp, fbs, restecg, exang, ca, thal]):
        key = f"{col}_{val}"
        if key in row:
            row[key] = 1

    df = pd.DataFrame([row], columns=_columns)
    df[_NUMERIC] = _scaler.transform(df[_NUMERIC])

    prob = float(_model.predict(df.astype("float32").to_numpy(), verbose=0)[0][0])
    label = "Heart Disease Detected" if prob >= 0.5 else "No Heart Disease"
    return prob, label


if __name__ == "__main__":
    prob, label = predict(
        age=63, trestbps=145, chol=233, thalach=150, oldpeak=2.3, slope=0,
        sex=1, cp=3, fbs=1, restecg=0, exang=0, ca=0, thal=1,
    )
    print(f"{label}  (probability: {prob:.3f})")
