# 🧠 Suicide Risk Detection Web App (XGBoost + NLP + Flask)

This project is a complete machine learning pipeline and web application that detects suicide risk from text input using Natural Language Processing (NLP) techniques. The project began with multiple models in PySpark and transitioned into a web-deployable XGBoost pipeline using scikit-learn, wrapped in a Flask interface.

---

## 📚 Dataset Information

This project uses the publicly available **(Suicide and Depression Detection(https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch))**.

The dataset contains real-world text messages labeled as `suicide` or `non-suicide`.

📝 **Modifications made**:
- Text cleaned and lowercased
- Stopwords removed
- Label encoded: `suicide` → 1, `non-suicide` → 0
- Predefined train and dev datasets used

> **All rights and credit go to the original dataset creators.** This project uses the dataset solely for academic and educational purposes.

---

## 🔁 Project Workflow Summary

### 1. 🔵 PySpark-Based Modeling (Exploration Phase)

Initially, the dataset was processed and modeled using **PySpark's MLlib** to explore distributed training approaches on large data. Models trained:

- ✅ **Naive Bayes**
- ✅ **Random Forest**  
- ✅ **Gradient-Boosted Trees (GBTClassifier)**  

All models were built using Spark's `Pipeline` with preprocessing stages:

- `Tokenizer` → `StopWordsRemover` → `CountVectorizer` → `IDF` → Classifier

**Best PySpark model performance (dev set):**

| Model           | Accuracy |
|----------------|----------|
| Naive Bayes     | ~89%     |
| GBTClassifier   | ~86%     |
| Random Forest   | ~82%     |



---

### 2. 🟠 Machine Learning (scikit-learn + XGBoost)

To simplify deployment, the project was ported to a **scikit-learn pipeline** with an **XGBoost classifier**.

- **Preprocessing**: `CountVectorizer` + `TfidfTransformer`
- **Classifier**: `XGBClassifier(n_estimators=200, max_depth=5)`

**Evaluation (dev set):**
- ✅ Accuracy: ~91%
- ✅ Weighted Precision, Recall, F1-score reported using `classification_report`

Model saved using `joblib` for integration into the web app.

---

### 3. 🟢 Web Application (Flask App + XGBoost)

The final deployed model (XGBoost) is integrated into a **Flask app** where users can:

- Paste input text
- Get prediction: **Suicidal** or **Non-suicidal**

---

## ⚠️ Important Disclaimer

> **This project is developed strictly for academic and educational purposes.**  
> It is not a diagnostic tool and is not intended for real-world mental health screening or clinical use.  
> The model's predictions are based on statistical patterns and may not be fully accurate or reliable for critical decision-making.  
> If you or someone you know is in crisis, please seek professional help or contact a licensed mental health provider or suicide prevention helpline.

## 🌐 Live Web App (Local)

Run locally with:
```bash
python app.py
