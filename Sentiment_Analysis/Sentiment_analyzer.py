from deepface import DeepFace
import cv2


def sentiment_detector():
    """
    The function does the following tasks:
    1. Uses opencv to generate live camera feed and get each frame.
    2. Uses Haar cascade's frontal face classifier to recognize a face in the
    frame.
    3. Uses DeepFace.analyze() method which uses its facial emotion recognition
    model to identify the sentiment on the face.

    :return: None
    """

    video_capture = cv2.VideoCapture(0)

    # For detecting faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        ret, frame = video_capture.read()

        # Emotion analyzer
        final = DeepFace.analyze(frame, actions=['emotion'])

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detects the bounds within which the face is present in the frame
        face_rect = face_cascade.detectMultiScale(gray_img)

        # Inorder to draw a rectangle about the detected face
        (x, y, w, h) = face_rect[0]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        # To display the detected sentiment on the frame
        cv2.putText(frame, text=final['dominant_emotion'], org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3,
                    color=(0, 255, 0), thickness=5, lineType=cv2.LINE_AA)

        # To display the live feed
        cv2.imshow('test', frame)

        # Breaking the feed using 'esc' key
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    # Releasing the captured frames and closing the windows created for the same
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    sentiment_detector()

