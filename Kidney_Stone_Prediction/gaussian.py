import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

ddepth = cv.CV_16S
kernel_size = 3
# [variables]
# [load]
src = cv.imread(r'Images_Used\image2.JPG', cv.IMREAD_COLOR) # Load an image
# Check if image is loaded fine
# [load]
# [reduce_noise]
# Remove noise by blurring with a Gaussian filter
src = cv.GaussianBlur(src, (3, 3), 0)
# [reduce_noise]
# [convert_to_gray]
# Convert the image to grayscale
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# [convert_to_gray]
# Create Window
# [laplacian]
# Apply Laplace function
dst = cv.Laplacian(src_gray, ddepth, kernel_size)
# [laplacian]
# [convert]
# converting back to uint8
abs_dst = cv.convertScaleAbs(dst)
# [convert]
# [display]
plt.subplot(121),plt.imshow(src, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(abs_dst, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
