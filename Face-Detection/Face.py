#IMPORTING THE LIBRARIES
import cv2
import dlib

#SELECTING THE IMAGE

image = cv2.imread("Enter The name of the image here")

#USING THE CNN FILE FROM DLIB LIBRARY

face_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
detections = face_detector(image,1)

#Now creating the Dimensions in order to create the rectangle on face

for face in detections :
    l , t , r ,b ,c = face.rect.left() , face.rect.top() , face.rect.right() , face.rect.bottom() , face.confidence
    cv2.rectangle(image,(l,t) , (r,b) ,(0,255,0) ,2)
    print("-----Confidence Is Following For The Following Images-----")
    print(c)

#NUMBER OF FACES IN IMAGE
print("Number of Face Detected In Image are:-",len(detections))

cv2.imshow('After Detection',image)
cv2.waitKey()
