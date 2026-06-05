try:
    from predict import predict
except FileNotFoundError as e:
    raise SystemExit(f"ERROR: {e}") from e

import gradio as gr


def run_prediction(age, trestbps, chol, thalach, oldpeak,
                   sex, cp, fbs, restecg, exang, slope, ca, thal):
    sex_val    = {"Female": 0, "Male": 1}[sex]
    cp_val     = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}[cp]
    fbs_val    = {"No": 0, "Yes": 1}[fbs]
    restecg_val = {"Normal": 0, "ST-T Abnormality": 1, "LV Hypertrophy": 2}[restecg]
    exang_val  = {"No": 0, "Yes": 1}[exang]
    slope_val  = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}[slope]
    ca_val     = int(ca)
    thal_val   = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2, "Unknown": 3}[thal]

    prob, label = predict(
        age=age, trestbps=trestbps, chol=chol, thalach=thalach, oldpeak=oldpeak,
        slope=slope_val, sex=sex_val, cp=cp_val, fbs=fbs_val, restecg=restecg_val,
        exang=exang_val, ca=ca_val, thal=thal_val,
    )
    confidence = prob if prob >= 0.5 else 1 - prob
    return f"Result: {label}  (Confidence: {confidence:.1%})"


with gr.Blocks(title="Heart Disease Predictor") as demo:
    gr.Markdown("## Heart Disease Predictor")

    with gr.Row():
        with gr.Column():
            age      = gr.Slider(20, 80,  step=1,   label="Age")
            trestbps = gr.Slider(80, 200, step=1,   label="Resting Blood Pressure (mm Hg)")
            chol     = gr.Slider(100, 600, step=1,  label="Serum Cholesterol (mg/dl)")
            thalach  = gr.Slider(60, 220, step=1,   label="Max Heart Rate Achieved")
            oldpeak  = gr.Slider(0.0, 6.2, step=0.1, label="ST Depression (Exercise vs Rest)")

        with gr.Column():
            sex     = gr.Dropdown(["Female", "Male"],                                                        label="Biological Sex")
            cp      = gr.Dropdown(["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"], label="Chest Pain Type")
            fbs     = gr.Dropdown(["No", "Yes"],                                                             label="Fasting Blood Sugar >120 mg/dl")
            restecg = gr.Dropdown(["Normal", "ST-T Abnormality", "LV Hypertrophy"],                         label="Resting ECG Results")
            exang   = gr.Dropdown(["No", "Yes"],                                                             label="Exercise Induced Angina")
            slope   = gr.Dropdown(["Upsloping", "Flat", "Downsloping"],                                     label="Slope of Peak Exercise ST Segment")
            ca      = gr.Dropdown(["0", "1", "2", "3", "4"],                                                label="Number of Major Vessels")
            thal    = gr.Dropdown(["Normal", "Fixed Defect", "Reversible Defect", "Unknown"],               label="Thalassemia Type")

    submit = gr.Button("Predict")
    output = gr.Textbox(label="Prediction")

    submit.click(
        fn=run_prediction,
        inputs=[age, trestbps, chol, thalach, oldpeak,
                sex, cp, fbs, restecg, exang, slope, ca, thal],
        outputs=output,
    )

if __name__ == "__main__":
    demo.launch()
