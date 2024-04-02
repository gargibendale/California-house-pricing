import pickle
from flask import Flask, request, app, jsonify, url_for, render_template

import numpy as np
import pandas as pd

#load the model

app=Flask(__name__)
regmodel=pickle.load(open('regmodel', 'rb'))

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
