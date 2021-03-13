## Music Genre Classification
### Prerequisites

 - python_speech_features library
 - mfcc function
 - scipy.io.wavfile function
 - numpy library
 - tempfile library
 - os module
 - pickle module
 - random module
 - operator module
 - math library
 - GTZAN Genre dataset - ''[http://marsyas.info/downloads/datasets.html](http://marsyas.info/downloads/datasets.html)''

We can use either Python or Google Colab for executing this code. 
Make sure the above prerequisites have been fulfilled in both the cases.
When using Google Cloud, you can upload the data needed to your Drive, to ensure a seamless process of executing the model. 

### Algorithm used - KNN 
K - Nearest Neighbours is an efficient algorithm, in terms of calculation time and predictive power, for classification. 
Here, K is usually equal to sqrt(N), where N stands for the number of classes.
We can easily implement a KNN using the following steps:

 1. Load the dataset
 2. Initialize the value of k
 3. Iterate from 1 to the total number of data training points:
		 a. Calculate the distance between the test data and each row of 		    the training data.
		 b. Sort the distances in ascending order.
		 c. Get top k rows from the sorted list.
		 d. Get the most frequent class of these k rows.
		 e. Return the predicted class.