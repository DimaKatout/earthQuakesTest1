import datetime
import requests
from requests.exceptions import HTTPError
from flask import Flask, render_template 


app = Flask(__name__) 

@app.route("/") 
def homepage(): 
    return render_template('index.html')

@app.route("/login",methods=["POST","GET"])
def login():
    return render_template()


#to get value from html page

@app.route('/',method=['POST'])
def getValue():
    latitude=request.form['latitude']
    longitude=request.form['longitude']
    radius=request.form['radius']
    minimumMagnitude=request.form['minimumMagnitude']
    return render_template['pass.html',latitude=latitude,longitude=longitude,radius=radius,minimumMagnitude=minimumMagnitude]


if __name__ == '__main__': 
  
    
    app.run(debug = True) 

