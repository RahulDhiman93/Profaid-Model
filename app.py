from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load('profaid_prod_model.joblib')
vectorizer = joblib.load('profaid_prod_vectorizer.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json().get('input_text')

        if input_data == "":
            return jsonify({'prediction': "No Input or Wrong Input"})
        else:
            print("PAYLOAD:", input_data)
            new_text_vectorized = vectorizer.transform([input_data])
            predicted_label = model.predict(new_text_vectorized)[0]
            return jsonify({'prediction': predicted_label})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # app.run(port=5000)
    app.run(debug=True)