###  Libraries Used

#### imread()
cv2.imread() method loads an image from the specified file. If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format) then this method returns an empty matrix.

#### cvtColor()
cv2.cvtColor() method is used to convert an image from one color space to another. There are more than 150 color-space conversion methods available in OpenCV. 

#### GaussianBlur()
In the Gaussian Blur operation, the image is convolved with a Gaussian filter instead of the box filter. The Gaussian filter is a low-pass filter that removes the high-frequency components are reduced. It also smoothens or blurs the image. You can perform this operation on an image using the Gaussianblur() method of the imgproc class. Gaussian blurring is highly effective in removing Gaussian noise from an image.

#### cv2.threshold() 
If pixel value is greater than a threshold value, it is assigned one value (may be white), else it is assigned another value (may be black). The function used is cv2.threshold. First argument is the source image, which should be a grayscale image. Second argument is the threshold value which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.

#### cv2.SimpleBlobDetector_create()
SimpleBlobDetector is an algorithm which is controlled by parameters in the following way-

Thresholding : Convert the source images to several binary images by thresholding the source image with thresholds starting at minThreshold. These thresholds are incremented  by thresholdStep until maxThreshold. So the first threshold is minThreshold, the second is minThreshold + thresholdStep, the third is minThreshold + 2 x thresholdStep, and so on.
Grouping : In each binary image,  connected white pixels are grouped together.  Let’s call these binary blobs.
Merging  : The centers of the binary blobs in the binary images are computed, and  blobs located closer than minDistBetweenBlobs are merged.
Center & Radius Calculation :  The centers and radii of the new merged blobs are computed and returned.