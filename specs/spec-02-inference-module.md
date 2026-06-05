# Spec 02 — Inference Module (`predict.py`)

Loads saved artifacts once at import, exposes a single `predict()` function.

## Logic
1. Load `model.keras`, `scaler.pkl`, `columns.pkl` at module level
2. Build a zero-filled row matching all columns from `columns.pkl`
3. Fill numeric values directly; for each categorical (e.g. `sex=1`), set `sex_1 = 1`
4. Apply `scaler.transform()` to numeric columns only
5. Run `model.predict()` → return `(probability: float, label: str)`

## Numeric columns
`age, trestbps, chol, thalach, oldpeak, slope`

## Categorical → one-hot mapping
`pd.get_dummies` names columns as `{col}_{value}`. User selects `cp=2` → set `cp_2 = 1`.

## Edge Cases
- Artifacts must exist before import — raise a clear error if `artifacts/` is missing
- Scaler transforms only numeric columns; one-hot columns must stay as 0/1 integers
- `columns.pkl` order must be respected exactly — wrong order silently corrupts predictions
- `slope` is numeric in the scaler but has only 3 values (0/1/2) — pass it as-is to the scaler

## Done when
`python predict.py` prints a prediction for a hardcoded test row without errors
