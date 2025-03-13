import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy an np
import pandas as pd

app=Flask(__name__)
## Load the model
model=pickle.load(open('','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.jsom['data']
    print(data)
