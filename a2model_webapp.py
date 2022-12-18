from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
from tensorflow import keras

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
modelpath = 'a2model_resnet50.h5'

# Loading trained model
model = load_model(modelpath)


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(256, 256))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   
    prediction = model.predict(x)
    prediction=np.argmax(prediction, axis=1)
    if prediction==0:
        prediction="This is berry"
    elif prediction==1:
        prediction="This is bird"
    elif prediction==2:
        prediction="This is dog"
    else:
        prediction="This is flower"
    
    
    return prediction


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        prediction = model_predict(file_path, model)
        result=prediction
        return result
    return None

if __name__ == '__main__':
    app.run(debug=True)
