import cv2

import facial_lock_system.Model.face_data_collection as collector
import facial_lock_system.Model.face_lock_data_training_and_prediction as predictor


class face_lock(object):

    def __init__(self):
        super().__init__()

    @staticmethod
    def call_method():
        camera1 = cv2.VideoCapture(0)
        collector.create_directory()
        collector.data_collection(camera1)
        camera1.release()
        model = predictor.model_training()
        camera2 = cv2.VideoCapture(0)
        predictor.face_lock_system(camera2, model)


if __name__ == "__main__":
    face_lock_object = face_lock()
    face_lock_object.call_method()
