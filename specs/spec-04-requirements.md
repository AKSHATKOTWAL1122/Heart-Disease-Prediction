# Spec 04 — Requirements

Create `requirements.txt` and verify full end-to-end run.

## `requirements.txt`
```
tensorflow>=2.13
gradio>=4.0
pandas
numpy
scikit-learn
matplotlib
```

## Run order
```bash
pip install -r requirements.txt   # once
python heartdisease.py             # train + save artifacts
python app.py                      # launch UI at localhost:7860
```

## Edge Cases
- TensorFlow requires Python 3.8–3.11; 3.12+ may fail — note this if install errors occur
- `tensorflow` includes Keras — no separate `keras` install needed

## Done when
All 3 commands run without errors in sequence
