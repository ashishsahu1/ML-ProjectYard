# Identify matching documents using template matching

This script identifies matching documents (represented as images) which belong to the same vendor by extracting their logos and computing the normalized mean squared error between them.

> Note: This script was designed for documents which contain textual information / artifacts around the logo, and therefore, might not work for all invoices.

# Example

Let's iterate through the steps involved in determining wether the following two documents belong to the same vendor.

<p align="center">
  <img src="dataset/document1.png" height="400">
  <img src="dataset/document2.png" height="400">
</p>

1. Extract top 15% of image.

<p align="center">
  <img src="output/document1.png/1-header.jpg" width="500">
</p>

2. Perform dilation and erosion to hide out the extraneous text.

<p align="center">
  <img src="output/document1.png/2-header-dilated-eroded.jpg" width="500">
</p>

3. Find all contours and extract the region occupied by the logo.

<p align="center">
  <img src="output/document1.png/4-found-logo.jpg" width="500">
</p>

4. Extract top 15% of the pair image.
5. Perform template matching of the logo found in step 3 with the pair image.

<p align="center">
  <img src="output/document1.png/6-header-rectangle.jpg" width="500">
</p>

7. Compute normalized mean squared error between the region found in step 6 with the logo.

<p align="center">
  <img src="output/document1.png/4-found-logo.jpg" width="250">
  <img src="output/document1.png/7-matched-logo.jpg" width="250">
</p>

If NMSE is less than a certain threshold (arbitrary value), the documents match. For the logos extracted above, the NMSE is `0.351`. Being a very small value, it gives us a high probability that the logos do indeed match.

# Setup

Place all the documents in the `dataset/` directory. Ideally, the filenames should be read from an external file to ensure the order in which the images are matched.

### Package requirements

This script was tested on Python 3.8, and requires the following modules:

- NumPy
- Matplotlib
- OpenCV
- Scikit-image

# Usage

This script can be used as a preprocessing step when performing OCR on documents.

# Datasets

Some publicly available datasets which contain image invoices are:

- [Ghega dataset](https://machinelearning.inginf.units.it/data-and-tools/ghega-dataset)
- [RVL-CDIP dataset](http://www.cs.cmu.edu/~aharley/rvl-cdip)
