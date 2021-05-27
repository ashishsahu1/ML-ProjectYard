#%%     #this line is for VSCode editor only
import cv2
#from skimage.measure import compare_ssim
import argparse
import imutils
import numpy as np
import matplotlib.pyplot as plt
#change the path as per you configuration
img = cv2.imread(r'Images_Used\image1.jpg',1)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
#sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
#laplacian = cv2.Laplacian(img,cv2.CV_64F)

plt.subplot(111), plt.imshow(sobely, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.show()
