import numpy as np
from numpy import reshape
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
print(__name__)
model = pickle.load(open('model_pricing.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("request values : ", request.form.values())
    int_features = [int(x) for x in request.form.values()]
    print("int_features : ", int_features)
    final_features = [np.array(int_features)]
    print("final features : ", final_features)
    final_features = reshape(final_features, (-1, 1)).T
    print("Reshaped and Transformed final features : ", final_features)
    prediction = model.predict(final_features)
    print("predicted value : ", prediction)
    output = round(prediction[0], 2)
    print("rounded output : ", output)
    if output == 0:
        return render_template('index.html', prediction_text='Unfortunately, these people have not survived')
    elif output == 1:
        return render_template('index.html', prediction_text='Fortunately, these people have survived')


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    print('Hello from predict_api ', output)
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
