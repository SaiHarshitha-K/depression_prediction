# 🧠 Suicide Detection Web App (Flask + XGBoost)

This is a Flask-based web application that allows users to input a message and receive a prediction on whether the text is **likely suicidal** or **likely non-suicidal**. It uses a pre-trained XGBoost model (`xgb_pipeline.pkl`) for classification.

> ⚠️ **Disclaimer**: This project is for **educational and demonstration purposes only**.  
> It is not medically validated and should **not be used as a clinical or diagnostic tool**.

---

## ✅ What This Project Includes

- A simple Flask interface (`app.py`)
- Pre-trained XGBoost model loaded with `joblib`
- Styled front-end using HTML and CSS (`templates/index.html`)
- Input truncation and clean result display
- Educational disclaimer shown in the UI

---

## 🛠️ Technologies Used

- `Flask` – for the web server and routing  
- `XGBoost` – for the machine learning model  
- `scikit-learn` – for preprocessing pipeline  
- `joblib` – for loading the saved model  
- `HTML/CSS` – for UI styling

---


---

## ▶️ How to Run the App Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Flask server

```bash
python app.py
```

### 3. Open your browser and go to

```
http://127.0.0.1:5000
```


