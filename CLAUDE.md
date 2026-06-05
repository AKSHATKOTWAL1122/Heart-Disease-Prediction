# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Goal
Add a Gradio web UI to an existing Keras heart disease classifier so users can enter medical details and get a prediction.

## Progress

| Spec | Task | Status |
|---|---|---|
| spec-01 | Modify `heartdisease.py` to save artifacts | Done |
| spec-02 | Create `predict.py` (inference module) | Done |
| spec-03 | Create `app.py` (Gradio UI) | Done |
| spec-04 | Create `requirements.txt` | Done |

Update status to `Done` as each spec is completed. Implement in order — each depends on the previous.

## Key Decisions
- **Gradio** chosen for frontend (beginner-friendly, pure Python, no server needed)
- **Train once, save artifacts** — model is never retrained at inference time
- **Full human-readable labels** in the UI; mapped back to dataset column names in code
- **Sliders** for all 5 numeric inputs; **dropdowns** for all 8 categorical inputs
- User is a beginner — keep code simple, no unnecessary abstractions
