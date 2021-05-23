# Face Mask Detector
Due to the recent pandemic, we all were locked down in our homes but now we have to accept the situation and carry on our lives with this "new normal". One of the important steps to  minimize the spreading of the virus is using mask. Whether you are in office, school, public place, or anywhere, you should wear masks to keep yourself and others safe. 
The goal of this project is to ensure that people wear masks whenver they enter any building. This system can be installed in offices, restaurants, metro stations, or in any buildings entrance to make sure that the person who enters the building is wearing a mask.

![alt text](https://github.com/Ayush-Parhi/FaceMaskDetection/blob/master/Output_screenshot.png?raw=true)

# Details about the structure of the codebase
* The main python scripts that is used to detect the mask is in the ```mask_detector``` folder. This folder contains 2 python scripts namely, ```mask_detect_img.py``` and ```mask_detect_vid.py```.
The ```mask_detect_img.py``` is used to detect masks in an image file and the ```mask_detect_vid.py``` is used to detect masks in a video stream.
* The ```notebooks``` folder contains a jupyter notebook that is used to train the model for mask detection.
* Face Detection i.e enclosing the face of a person inside a bounding box is done by using a pre-trained face detection model which is stored in ```face_detection``` folder. 
* ```Images``` folder contains 2 test images that can be used to test the ```mask_detect_img.py``` script.

# Prerequisites
* Python 3 or above
* All other requirements are inside the requirements.txt file

# Installation
1. Clone the repository
```
$ git clone https://github.com/Ayush-Parhi/FaceMaskDetection.git
```

2. Go to the project directory
```
$ cd FaceMaskDetection
```

3. Create a virtual environment. (Here, I am using pipenv but you can use virtualenv also)
```
$ pipenv shell
```

4. Install the dependencies.
```
$ pip install -r requirements.txt
```

# Usage
1. Detect masks in images.
```
$ python mask_detector/mask_detect_image.py --image images/pic1.jpeg
```

2. Detect masks in real-time video
```
$ python mask_detector/mask_detect_vid.py
```


