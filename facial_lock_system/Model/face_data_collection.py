import os

import cv2


def create_directory():
    try:
        if not os.path.exists('../dataset'):
            os.makedirs('dataset')
    except OSError:
        print('directory not created')


def face_extraction(img):
    face = cv2.CascadeClassifier('./dataset/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.5, 5)
    if faces is ():
        return None
    for (x, y, w, h) in faces:
        crop = img[y:y + h, x:x + w]
    return crop


def data_collection(camera):
    c = 0
    while True:
        checker, frame = camera.read()
        if face_extraction(frame) is not None:
            c += 1
            face1 = cv2.resize(face_extraction(frame), (200, 200))
            face2 = cv2.cvtColor(face1, cv2.COLOR_BGR2GRAY)
            name = './dataset/count' + str(c) + '.jpg'
            print(name)
            cv2.imwrite(name, face2)
            cv2.imshow("Data Collection", face2)
        else:
            print('not found')
            pass
        key = cv2.waitKey(1)
        if key == 27 or c == 200:
            break
    cv2.destroyAllWindows()
