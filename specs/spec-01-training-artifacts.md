# Spec 01 — Save Training Artifacts

Modify `heartdisease.py` to save 3 files after training.

## Changes to `heartdisease.py`
- Add `import pickle, os`
- After `pd.get_dummies(...)`, before split: `feature_columns = df.drop('target', axis=1).columns.tolist()`
- After `model.fit(...)`:
```python
os.makedirs('artifacts', exist_ok=True)
model.save('artifacts/model.keras')
pickle.dump(scaler, open('artifacts/scaler.pkl', 'wb'))
pickle.dump(feature_columns, open('artifacts/columns.pkl', 'wb'))
```

## Edge Cases
- Re-running overwrites artifacts — intended, keeps model/scaler/columns in sync
- `feature_columns` must be captured after `get_dummies` but before `sample()` — full column order, not a subset
- If CSV fetch fails, nothing is saved (no partial artifacts)

## Done when
`artifacts/` has `model.keras`, `scaler.pkl`, `columns.pkl`
