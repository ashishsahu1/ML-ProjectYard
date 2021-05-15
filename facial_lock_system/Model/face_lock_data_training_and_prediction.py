from os import listdir
from os.path import isfile, join

import cv2
import numpy as np


def model_training():
    data_path = '../dataset/'
    only_files = [f for f in listdir(data_path) if isfile(join(data_path, f))]
    Training_Data, Labels = [], []
    for i, files in enumerate(only_files):
        image_path = data_path + only_files[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    Labels = np.asarray(Labels, dtype=np.int32)
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    print("Model Training.......")
    return model


def face_detector(img, size=0.5):
    face_classifier = cv2.CascadeClassifier('./dataset/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.5, 5)

    if faces == ():
        return img, []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))

    return img, roi


def face_lock_system(camera, model):
    while True:

        ret, frame = camera.read()

        image, face = face_detector(frame)
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            result = model.predict(face)
            if result[1] < 500:
                confidence = int(100 * (1 - (result[1]) / 300))
                display_string = str(confidence) + '% Confidence it is user'
                cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)

            if confidence > 75:
                cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow('Face Cropper', image)

            else:
                cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                # display_string = str(confidence) + '% Confidence it is not user'
                cv2.imshow('Face Cropper', image)
        except:
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass

        if cv2.waitKey(1) == 27:
            break
    camera.release()
    cv2.destroyAllWindows()
