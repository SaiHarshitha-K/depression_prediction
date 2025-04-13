from flask import Flask, request, render_template, redirect, url_for, session
import joblib

# Load the trained model
model = joblib.load("xgb_pipeline.pkl")

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session handling

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        result_text = request.form['text']
        prediction = model.predict([result_text])[0]
        label = 'Likely Suicidal' if prediction == 1 else 'Likely Non-suicidal'
        # Save result temporarily in session
        session['label'] = label
        session['result_text'] = result_text
        return redirect(url_for('index'))  # Redirect to GET to clear POST data

    # Handle GET request (after redirect)
    label = session.pop('label', None)
    result_text = session.pop('result_text', "")
    return render_template('index.html', label=label, result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
