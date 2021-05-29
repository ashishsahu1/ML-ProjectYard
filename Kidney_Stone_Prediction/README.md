# Kidney Stone Detection
## Using Image Processing Techniques

The main objective of this is to detect the kidney stone from a digital ultrasound image of the kidney by performing various image processing techniques.

### WORK PERFORMED
The data were collected from various sources some were online, whose link is given below and also from some close contacts. After collecting the data, we proceeded towards our working.
The first step was to get a clear and better quality of the data so we worked on the IMAGE ENHANCEMENT:
1.	The first one we applied was Frequency Domain + Gaussian Filter. Here we had to divide the image into two plains real plain and complex plain and then apply the Gaussian Filter in both.
2.	The second attempt was with Gaussian Blur + Laplacian Filter. We had to apply Gaussian Blur to make Laplacian filter less sensitive to noise.
3.	On further studies, we found in some research papers (link given below) that Ultrasounds give speckle noise. So, our third attempt was to replace Gaussian Blur with Median Blur as the latter is more effective for low-level noises like speckle noise, salt-and-pepper noise etc. followed by Laplacian filter.
4.	In the application of the Gabor filter, the restored image is enriched with optimal resolution in both spatial and frequency domains (as stated in one of the research papers, whose link is given below). 2-D Gabor filter is easier to tune the direction and radial frequency bandwidth, and easier to tune centre frequency, so they can simultaneously get the best resolution in the spatial domain and frequency domain.

Now we moved to our next step HISTOGRAM EQUALIZATION. 
It is a technique for adjusting image intensities to enhance contrast. This process leads to an increase in contrast of the shadow of the stone and the stone itself. Thus, it became more visible.

 After this, we proceeded towards IMAGE SEGMENTATION.
It partitions an image into distinct regions containing each pixel with similar attributes. To be meaningful and useful for image analysis and interpretation, the regions should strongly relate to depicted objects or features of interest. Meaningful segmentation is the first step from low-level image processing transforming a greyscale or colour image into one or more other images to high-level image description in terms of features, objects, and scenes. Hereby performing this, we needed to partition our stone from the rest of the image. The type of Image Segmentation used here is Watersheds. Here we divide the image into peaks (high intensity) and valleys (low intensity). We fill the valleys (points of minima or background) with water of different colours (labels). As the water rises, depending on the peaks(gradients) nearby, water from different valleys, obviously with different colours will start to merge. To avoid this, we need to build barriers in the area where the water is mixing. Also, we continue the process of filling water until all the peaks are under water. The barriers, thus, created are the result of image segmentation. Now, the shadow gets separated from the stone giving a clear image of the stone. 

The last step being MARKING.
 It provides you with a way to identify or label a spot within the processing pipeline. Adding a marker into the pipeline will allow you to refer to the image currently being processed at that point. It can also be used to specify a location in the pipeline for other modules.



| WaterShed  | Read Write | Med Lap |
| ------------- | ------------- | ------------- |
| ![WaterShed](https://user-images.githubusercontent.com/67019423/119897060-85a55200-bf5d-11eb-8b91-b45b39f530c9.PNG) | ![read_write](https://user-images.githubusercontent.com/67019423/119897084-8ccc6000-bf5d-11eb-8ece-ac0646e23d77.PNG) | ![med_lap](https://user-images.githubusercontent.com/67019423/119897117-9655c800-bf5d-11eb-80b6-d0a085089d52.PNG) |

| Gaussian  | Gabor HistEq | Final Image |
| ------------- | ------------- | ------------- |
| ![gaussian](https://user-images.githubusercontent.com/67019423/119897180-a9689800-bf5d-11eb-9885-671785171637.PNG) | ![Gabor_HistEq](https://user-images.githubusercontent.com/67019423/119897224-b8e7e100-bf5d-11eb-9cd9-a2b6955077d9.PNG) | ![Finalcode](https://user-images.githubusercontent.com/67019423/119897256-c43b0c80-bf5d-11eb-8ac2-df3291acda56.PNG) |

### RESULTS
Total of 4 approaches have been performed to enhance the quality of the image, namely: Gabor Filter, Median blur + Laplacian Filter, Gaussian blur + Laplacian Filter, Gaussian Filtering in Frequency domain. Out of the 4, we have noticed that Gabor Filter was effective on a larger number of images though not all. Nextly Median blur + Laplacian Filter and Gaussian blur + Laplacian Filter worked perfectly with other of the few images which are lesser compared to Gabor Filter. Lastly, Gaussian Filtering in Frequency domain, which didn’t work as expected and hence this technique was not employed to enhance any of the other images. We also could generalize the effectiveness of the techniques due to lack of data samples.
Resulting images of ultrasound are given below:

| Original image  | Image with detection |
| ------------- | ------------- |
| ![image](https://user-images.githubusercontent.com/67019423/119896533-c6e93200-bf5c-11eb-973f-79330915b0d9.png) | ![image](https://user-images.githubusercontent.com/67019423/119896558-d0729a00-bf5c-11eb-8bb6-94f75137f1f9.png) |
| ![image](https://user-images.githubusercontent.com/67019423/119896609-df594c80-bf5c-11eb-943d-90cbe5856fb7.png) | ![image](https://user-images.githubusercontent.com/67019423/119896625-e7b18780-bf5c-11eb-91dd-f2b8941c6556.png) |
