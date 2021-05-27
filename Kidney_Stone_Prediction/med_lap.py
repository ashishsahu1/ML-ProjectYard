import cv2
import argparse
import imutils
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'Images_Used\image2.JPG', 0)

# **** check by changing the value 5 to any other odd number ****
dst = cv2.medianBlur(img, 5)

# Calculate the Laplacian
lap = cv2.Laplacian(dst,cv2.CV_64F)

# Calculate the sharpened image
# *****check this line if it is necessary******
sharp = dst - 0.3*lap

sharp = np.uint8(cv2.normalize(sharp, None, 0 , 255, cv2.NORM_MINMAX))
equ = cv2.equalizeHist(sharp)

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(equ, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.show()
