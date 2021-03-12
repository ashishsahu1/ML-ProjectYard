import cv2


# video preprocessing for detection
video = cv2.VideoCapture('cars_2.mp4')

# creating car classifier and pedestrian classifier by loading the haarcascade classsifier into cv2 cascade classifier
car_classifier = 'cars.xml'
pedestrian_classifier = 'body.xml'
car = cv2.CascadeClassifier(car_classifier)
pedestrian = cv2.CascadeClassifier(pedestrian_classifier)



#detecting cars from video
while True:
    read_successful, frame = video.read()
    if(read_successful):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cars = car.detectMultiScale(gray_frame)
        pedestrians = pedestrian.detectMultiScale(gray_frame)
        
        # drawing rectangles around cars
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # drawing rectangles around pedestrians
        for (x, y, w, h) in pedestrians:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    else:
        break

    #displaying the work
    cv2.imshow('car and pedestrian detection display', frame)
    key = cv2.waitKey(1)

    if(key==65 or key==97):
        break

video.release()