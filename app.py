from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('profaid_prod_model.joblib')
vectorizer = joblib.load('profaid_prod_vectorizer.joblib')  # Make sure to replace with the correct filename

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def predict():
    try:
        input_data = request.args.get('text')
        new_text_vectorized = vectorizer.transform([input_data])
        predicted_label = model.predict(new_text_vectorized)[0]

        return jsonify({'prediction': predicted_label})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # app.run(port=5000)
    app.run(debug=True)