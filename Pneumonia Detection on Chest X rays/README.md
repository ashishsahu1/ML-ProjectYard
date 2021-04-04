## Pneumonia-Classification-using-Deep-Learning
Detecting Pneumonia in Chest X-ray Images using CNNs and Pre-trained Models in Tensorflow

#### Motivation
Machine learning has a phenomenal range of applications, including in health and diagnostics. This is especially useful during these current times as COVID-19 is known to cause pneumonia.

#### Dataset
<pre>
Dataset Name     : Chest X-Ray Images (Pneumonia)
Dataset Link     : <a href=https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia>Chest X-Ray Images (Pneumonia) Dataset (Kaggle)</a>
</pre>

<pre>
<b>Dataset Details</b>
Dataset Name            : Chest X-Ray Images (Pneumonia)
Number of Class         : 2
Number/Size of Images   : Total      : 5856 (1.15 Gigabyte (GB))
                          Training   : 5216 (1.07 Gigabyte (GB))
                          Validation : 320  (42.8 Megabyte (MB))
                          Testing    : 320  (35.4 Megabyte (MB))
</pre>


#### Results

Metric | Result
--------|-------
Accuracy (F-1) Score | 89.53%
Loss | 0.41
Precision | 88.37%
Recall (Pneumonia) | 95.48% (For positive class)


The model was built using `InceptionV3` and Deep Convolutional Neural Network as its underlying architecture. I used `Adam` as the optimizer and `categorical_crossentropy` as loss function.

###### Sample output
![Web-cam](/images/sample.png)

###### The confusion matrix
![conf-mat](/images/CM.png)


##### References
* This code has been contributed by Jahnavi Majji as a part of GSSoc '21
