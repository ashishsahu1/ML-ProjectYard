from skimage.metrics import normalized_root_mse
from matplotlib import pyplot as plt
import numpy as np
import pathlib
import time
import cv2
import os

# Increase the figure size.
plt.rc('figure', figsize=(20, 20))

input_dir = 'dataset/'
output_dir = 'output/'

start = time.time()
filenames = os.listdir(input_dir)
filenames.reverse()
imgs = [cv2.imread(input_dir + filename) for filename in filenames]
end = time.time()

img_load_time = end - start

start = time.time()
for i in range(len(imgs)-1):
	pathlib.Path(output_dir+filenames[i]).mkdir(parents=True, exist_ok=True)

	# Extract top 15% of the image.
	img = imgs[i]
	header = img[:int(img.shape[0]*0.15), :]
	cv2.imwrite(f'{output_dir}{filenames[i]}/1-header.jpg', header)

	# Perform dilation and erosion to blur the text.
	d_kernel = np.ones((5, 5), np.uint8)
	header = cv2.dilate(header, d_kernel)
	e_kernel = np.ones((15, 15), np.uint8)
	header = cv2.erode(header, e_kernel)

	cv2.imwrite(f'{output_dir}{filenames[i]}/2-header-dilated-eroded.jpg', header)

	# Use Canny to find edges.
	canny = cv2.Canny(header, 100, 100 * 2)
	cv2.imwrite(f'{output_dir}{filenames[i]}/3-header-canny.jpg', canny)

	# Find the contours using edges.
	contours, hierarchy = cv2.findContours(
		canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	# If no contours were found, skip the image.
	if not contours:
		print(f'{i} -> {i+1}: no match')
		continue

	contours = np.vstack(c for c in contours)
	x, y, w, h = cv2.boundingRect(contours)
	logo = img[y:y+h, x:x+w]

	cv2.imwrite(f'{output_dir}{filenames[i]}/4-found-logo.jpg', logo)
	cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# Extract top 15% of the pair image.
	header2 = imgs[i+1][:int(imgs[i+1].shape[0]*0.15), :]
	cv2.imwrite(f'{output_dir}{filenames[i]}/5-header-pair.jpg', header2)

	# Perform template matching of the matched template with header2.
	match = cv2.matchTemplate(header2, logo, cv2.TM_CCOEFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match)

	matched = header2[max_loc[1]:max_loc[1]+h, max_loc[0]:max_loc[0]+w]
	cv2.imwrite(f'{output_dir}{filenames[i]}/7-matched-logo.jpg', matched)

	bottom_right = (max_loc[0] + w, max_loc[1] + h)
	cv2.rectangle(imgs[i+1], max_loc, bottom_right, (0, 0, 255), 10)
	cv2.imwrite(f'{output_dir}{filenames[i]}/6-header-rectangle.jpg',
	imgs[i+1][:int(img.shape[0]*0.15), :])

	plt.subplot(221, title=f'Document {i}')
	plt.imshow(imgs[i])
	plt.subplot(222, title=f'Document {i+1}')
	plt.imshow(imgs[i+1])
	plt.subplot(223, title=f'Template (document {i})')
	plt.imshow(logo)

	if logo.shape == matched.shape:
		# Find the MSE of the matched template and the logo.
		nmse = normalized_root_mse(logo, matched)
		if nmse < 0.4:
			print(f'{i} -> {i+1}: found (score: {max_val}, mse: {mse})')
			plt.subplot(224, title=f'Matched (document {i+1}) [FOUND (score: {max_val}, mse: {mse})]')
		else:
			print(f'{i} -> {i+1}: not found (score: {max_val}, mse: {mse})')
			plt.subplot(224, title=f'Matched (document {i+1}) [NOT FOUND (score: {max_val}, mse: {mse})]')
	else:
		print(f'{i} -> {i+1}: no match')
		plt.subplot(224, title=f'Matched (document {i+1}) [NOT FOUND (score: {max_val}, dimensions mismatch)]')

	plt.waitforbuttonpress(0)
	plt.close()
	plt.show()

end = time.time()

print(f'Image load time: {img_load_time}s')
print(f'Execution time: {end-start}s')
