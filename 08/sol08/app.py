import numpy as np
from numpy import reshape
from flask import Flask, request, jsonify, render_template
from PIL import Image
import pickle

app = Flask(__name__)
print(__name__)
model = pickle.load(open('model_numbers.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print("request values : ", request.form.values())

    file = request.files['img']
    print("file : ", file)
    img = Image.open(file)
    print(type(img))
    img = np.asarray(img)
    print(type(img))
    print("final file : ", img)
    img = img[:, :, 0]
    img = img.reshape(784,)
    print("final 1D array: ", img)
    prediction = model.predict([img])
    print("predicted value : ", prediction)
    return render_template('index.html', prediction_head="Your image contains", prediction_text=str(prediction))


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
