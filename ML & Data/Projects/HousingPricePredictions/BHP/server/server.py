from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    responce = jsonify({
        'locations': util.get_location_names()
    })
    responce.headers.add('Acces-Control-Allow-Origin', '*')
    return responce

@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/predict_home_price', methods = ['POST'])

def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    response = jsonify({
        # 'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server for Home Prediction... ")
    app.run()
