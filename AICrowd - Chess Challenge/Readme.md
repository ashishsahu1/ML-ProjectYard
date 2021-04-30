# AICrowd Chess Challenge

In this project we are trying to solve a problem statement which was the part of AI Blitz community challenge on Aicrowd. 

## Problem statement

We are given a data of chess pieces on a board. These are all images of size 254*254. Our goal is to detrmine which side on the board has  least number of pieces.

## Approach

To solve this problem i experimented with many custom architectures but all of them failed. VGG16 and VGG19 failed to give good results as well. I then used InceptionResnetV2 which gave a good accuracy on training data but under performed on testing data. It's a clear case of underfitting but there should be some custom architecture that will prove to be much better for this data.

## Results

The training accuracy reached upto 92% on 10 epochs but the testing accuracy didn't seem to be good and was at 50-52% which means the model was underfitting.
Maybe  experimenting with the number of epochs could get better results but i feel a new architectural approach would give more robust model.

<p align="center">
<img src="https://github.com/AM1CODES/ML-ProjectYard/blob/main/AICrowd%20-%20Chess%20Challenge/Model/acc_result.png" alt="drawing" width="400"/>
</p>
