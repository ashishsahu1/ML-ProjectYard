import dlib
import cv2
import numpy as np
from scipy.spatial import distance as dist
import time
import winsound


def eye_aspect_ratio(eye):
    """
    It is used to determine EAR value based on the list we passed
    which consists of 6 points.
    :param eye: list of 6 points that we get from landmark
    :return: calculated ear value
    """
    # A & B for Vertical distance
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # C for Horizontal distance
    C = dist.euclidean(eye[0], eye[3])

    # Formula for calculating EAR
    ear = (A + B) / (2.0 * C)

    return ear


def drowsiness_detector():
    """
    This function consists main logic of the program in which
    1. detect faces
    2. from 68 landmark points we detect eyes
    3. from that points, calculation eye aspect ratio (EAR), then taking
       median of both eye EAR ratios.
    4. Checking for how many frames EAR is below our Threshold limit indicating,
       closed eyes.
    5. if eyes closed for more than the threshold we set for frames means person
       is feeling drowsy.
    :return: None
    """

    # detector for detecting the face in the image
    detector = dlib.get_frontal_face_detector()
    # predictor of locating 68 landmark points from the face by using a pretrained model
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    # Threshold values if EYE ASPECT RATIO (EAR) is less than 0.3 then eye is close
    EYE_AR_THRESH = 0.3
    # if eye is closed (ear < threshold) for a minimum consecutive frames ie person
    # feeling drowsy.
    EYE_AR_CONSEC_FRAMES = 48
    # for keeping count of frames below ear
    COUNTER = 0
    ALARM_ON = False

    # time.sleep(2)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if ret:
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # detecting faces in the frame
            faces = detector(frameGray)

            # if faces are present then locating the landmark points
            for face in faces:
                landmarks = predictor(frameGray, face)
                # list for storing points location in pixel.
                landmark_points_location = []

                # taking x,y location of only points from (36 to 47)+1
                # because eye's location are at this
                for i in range(36, 48):
                    x = landmarks.part(i).x
                    y = landmarks.part(i).y
                    # calculating x and y and appending it into a list
                    landmark_points_location.append([x, y])

                # changing the list into numpy array to perform computations.
                landmark_points_location = np.array(landmark_points_location)

                leftEye = landmark_points_location[:6]
                rightEye = landmark_points_location[6:]

                # calculating left and right eye EAR
                leftEye_ear = eye_aspect_ratio(leftEye)
                rightEye_ear = eye_aspect_ratio(rightEye)

                # calculating mean EAR
                ear = (leftEye_ear + rightEye_ear) / 2
                # Displaying EAR ration on every frame
                width = int(cap.get(3))
                cv2.putText(frame, "EAR: {:.2f}".format(ear), (width-125, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                # Drawing lines on ROI ie Left and Right eye
                leftEyeHull = cv2.convexHull(leftEye)
                cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                rightEyeHull = cv2.convexHull(rightEye)
                cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

                # here we are checking, if our calculated EAR < threshold then we are incrementing the counter
                if ear < EYE_AR_THRESH:
                    COUNTER += 1
                    # If counter is greater than threshold then DROWSINESS
                    if COUNTER >= EYE_AR_CONSEC_FRAMES:
                        if not ALARM_ON:
                            ALARM_ON = True
                            winsound.PlaySound("alert_signal.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS)

                        # Displaying Alert on Frame
                        cv2.putText(frame, 'DROWSINESS ALERT!!', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                    (0, 0, 255), 2, cv2.LINE_AA)
                else:
                    COUNTER = 0
                    ALARM_ON = False
                    winsound.PlaySound(None, winsound.SND_PURGE)

            # for showing frames on the window named Detector
            cv2.imshow('Detector', frame)

            # for quiting the program press 'ESC'
            if cv2.waitKey(1) & 0xFF == 27:
                break

        else:
            break

    # releasing all the frames we captured and destroying thw windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    drowsiness_detector()

