from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from PIL import Image
import numpy as np
import io

from model_utils import download_model

app = Flask(__name__)
CORS(app)

# Étape 1 : Télécharger le modèle si pas encore présent
download_model()

# Étape 2 : Charger le modèle
model = tf.keras.models.load_model('alzheimer_model_201.h5')

# Étape 3 : Route API
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier reçu'}), 400

    file = request.files['file']
    img = Image.open(file.stream).resize((224, 224))  # adapte si besoin
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    confidence = float(np.max(prediction))

    label_map = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
    result = label_map[predicted_class]

    return jsonify({'diagnosis': result, 'confidence': confidence})
