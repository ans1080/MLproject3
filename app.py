from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from arduino import Arduino

# Initialise Flask
app = Flask(__name__)


# Temporary storage for uploaded pictures
# to be able to display uploaded pictures they should locate in static directory
UPLOAD_FOLDER = 'static/tmp' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Maximum Image Uploading size
# app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024

# Image extension allowed
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods = ['POST', 'GET'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      if file and allowed_file(file.filename):
         filename = secure_filename(file.filename)
         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
         file.save(filepath)
         prediction = search(filepath)
         return render_template('search_results.html',
                    original=filepath,
                    best_guess_label=prediction,
                    image_urls="")

def search(f):
    cur_dir = os.path.dirname(__file__)
    model_dir = os.path.join(cur_dir, 'tensorflow')
    model = tf.keras.models.load_model(model_dir)
    model = tf.keras.Sequential([tf.keras.layers.Rescaling(scale=1./255), model, tf.keras.layers.ReLU()])
    label = {0: 'Defect 1', 1: 'Defect 2', 2: 'Normal'}

    img = tf.keras.preprocessing.image.load_img(f, target_size=(80,80))
    inputarr = tf.keras.preprocessing.image.img_to_array(img)
    
    inputarr = np.array([inputarr])
    prediction = model.predict(inputarr)
    score = tf.nn.softmax(prediction[0])

    arduino = Arduino()  # Added this initialize
    arduino.output(score) # Added this call

    # Changed score to score_string because the arduino needs the numbers
    score_string = "This image most likely belongs to {} with a {:.2f} percent confidence.".format(label[np.argmax(score)], 100 * np.max(score))

    print(score_string)
    return score_string

if __name__ == '__main__':
    app.run(debug=True)
