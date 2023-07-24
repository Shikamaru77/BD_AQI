import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('BDaqi.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        int_features = [float(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        prediction = model.predict(final_features)
        output_category = ['Unhealthy', 'Very Unhealthy', 'Hazardous', 'Unknown', 'Unhealthy for Sensitive Groups', 'Moderate', 'Good'][int(prediction[0])]
        return render_template("index.html", prediction=output_category)

  
@app.route('/predict_api',methods=['POST'])
def predict_api():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)