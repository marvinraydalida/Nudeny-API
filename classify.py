import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

from PIL import Image
from io import BytesIO

MODEL_NAME = "nudity_classifier.h5"
MODEL_DIR = ".\models\classify_model"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

class NudenyClassify:
    def __init__(self):
        self.model = load_model(MODEL_PATH)

    def classify(self, file, filename):
        img = Image.open(BytesIO(file))

        if filename.endswith('.png'):
            img = img.convert('RGB')
        
        img_input = tf.image.resize(img, (160,160))
        resized_img = np.expand_dims(img_input, 0)
        prediction = self.model.predict_on_batch(resized_img)
        prediction = tf.nn.sigmoid(prediction)
        prediction = tf.where(prediction < 0.5, 0, 1)
        prediction.numpy()
        if prediction[0] == 1:
            return {"filename" : filename, "class": "safe"}
        else:
            return {"filename" : filename, "class": "nude"}
    
        