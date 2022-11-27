import warnings
from io import BytesIO
import numpy as np
from object_detection.utils import visualization_utils as viz_utils
import cv2
import tensorflow as tf
import os
import time
import uuid
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore')


PATH_TO_SAVED_MODEL = ".\models\detect_model\saved_model"
BASE_PATH = "http://127.0.0.1:8000/static/"


class NudenyDetect:

    def __init__(self):
        print('Loading model...', end='')
        start_time = time.time()
        self.detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Done! Took {} seconds'.format(elapsed_time))

        self.category_index = {1: {'id': 1, 'name': 'buttocks'}, 2: {'id': 2, 'name': 'female_breast'}, 3: {
            'id': 3, 'name': 'female_genitalia'}, 4: {'id': 4, 'name': 'male_genitalia'}}

    def detect(self, file):
        img_stream = BytesIO(file)
        img = cv2.imdecode(np.frombuffer(img_stream.read(), np.uint8), 1)
        image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image_expanded = np.expand_dims(image_rgb, axis=0)
        input_tensor = tf.convert_to_tensor(img)
        input_tensor = input_tensor[tf.newaxis, ...]
        detections = self.detect_fn(input_tensor)

        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                      for key, value in detections.items()}
        detections['num_detections'] = num_detections

        detections['detection_classes'] = detections['detection_classes'].astype(
            np.int64)

        return img.copy(), detections

    def draw_bounding_box(self, file, filename):
        image_with_detections, detections = self.detect(file)
        height = image_with_detections.shape[0]
        width = image_with_detections.shape[1]

        viz_utils.visualize_boxes_and_labels_on_image_array(
            image_with_detections,
            detections['detection_boxes'],
            detections['detection_classes'],
            detections['detection_scores'],
            self.category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=200,
            min_score_thresh=0.5,
            agnostic_mode=False)

        exposed_parts = {}
        index = 0
        for scores in detections['detection_scores']:
            if scores >= 0.5:
                bottom = detections['detection_boxes'][index][2] * height
                top = detections['detection_boxes'][index][0] * height

                right = detections['detection_boxes'][index][3] * width
                left = detections['detection_boxes'][index][1] * width

                key = self.category_index[detections['detection_classes']
                                          [index]]['name']
                exposed_parts[key] = {"confidence_score": scores * 100, "top": int(
                    top), "left": int(left), "bottom": int(bottom), "right": int(right)}
            else:
                break
            index += 1

        extension = os.path.splitext(filename)[1]
        if extension == '':
            filename = filename + ".jpg"

        new_filename = str(uuid.uuid4()) + "-" + filename
        cv2.imwrite(os.path.join('./static', new_filename),
                    image_with_detections)

        return {
            "filename": filename,
            "url": BASE_PATH + new_filename,
            "exposed_parts": exposed_parts
        }

    def censor_exposed_part(self, file, filename):
        censored_image, detections = self.detect(file)
        height = censored_image.shape[0]
        width = censored_image.shape[1]

        exposed_parts = {}
        index = 0
        for scores in detections['detection_scores']:
            if scores >= 0.5:
                bottom = detections['detection_boxes'][index][2] * height
                top = detections['detection_boxes'][index][0] * height

                right = detections['detection_boxes'][index][3] * width
                left = detections['detection_boxes'][index][1] * width

                start_point = (int(left), int(top))
                end_point = (int(right), int(bottom))
                censored_image = cv2.rectangle(
                    censored_image, start_point, end_point, (0, 0, 0), -1)

                key = self.category_index[detections['detection_classes']
                                          [index]]['name']
                exposed_parts[key] = {"confidence_score": scores * 100, "top": int(
                    top), "left": int(left), "bottom": int(bottom), "right": int(right)}
            else:
                break
            index += 1

        extension = os.path.splitext(filename)[1]
        if extension == '':
            filename = filename + ".jpg"

        new_filename = str(uuid.uuid4()) + "-" + filename
        cv2.imwrite(os.path.join('./static', new_filename), censored_image)

        return {
            "filename": filename,
            "url": BASE_PATH + new_filename,
            "exposed_parts": exposed_parts,
        }
