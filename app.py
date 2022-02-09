from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
#from matplotlib.font_manager import json_load
import tensorflow as tf
import os
from tensorflow.keras import Model
from tensorflow.keras.utils import Sequence
import numpy as np


app = Flask(__name__)
loaded_model = tf.keras.models.load_model("Model_2022_02_08_11_17_41_.h5", compile=False)
@app.route("/", methods=[ "POST","GET"])
@cross_origin()
def index():
    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                data=[float(i) for i in dict_req.values()]
                #print(data)
                response= loaded_model.predict([data])
                return render_template("index.html",response=response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}

            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    data1=data.values()
    print(data1)
    #print(data2)
    prediction = loaded_model.predict([data1])
    output =str(prediction[0])
    
    return jsonify(output)



if __name__ == "__main__":
    #app.run(host='http://localhost', port=8001, debug=True)
	app.run(debug=True) # running the app