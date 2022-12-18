from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'a2model_resnet50.h5'

# import os
# MODEL_PATH = os.path.join(os.path.dirname(__file__), "a2model_resnet50.h5")

# Load your trained model
model = load_model(MODEL_PATH)


def model_predict(img_path, model):
    img = image.load_img(img_path, data_image_size=(256, 256))

    # Preprocessing the image
    layer = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    layer = layer / 255
    layer = np.expand_dims(layer, axis=0)

    preds = model.predict(layer)
    preds = np.argmax(preds, axis=0)
    if preds == 0:
        preds = "This is a berry"
    elif preds == 1:
        preds = "This is a bird"
    elif preds == 1:
        preds = "This is a dog"
    else:
        preds = "This is a flower"


    return preds


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
        preds = model_predict(file_path, model)
        result = preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)