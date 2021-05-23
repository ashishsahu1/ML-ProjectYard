## Dog Breed Multi Class Classification


### 1.Problem
There are 120 breeds of dog in the data. We have to identify according to their breeds.

### 2.Data
The dataset is taken from kaggle competition: kaggle.com/c/dog-breed-identification/data

There are training set and a test set of images of dogs. Each image has a filename that is its unique id. The dataset comprises 120 breeds of dogs.
* train.zip - the training set, you are provided the breed for these dogs
* test.zip - the test set, you must predict the probability of each breed for each image
* sample_submission.csv - a sample submission file in the correct format
* labels.csv - the breeds for the images in the train set

### Evaluation
Cross entropy loss.
### Features
* we are dealing with the unstructure data set.
* There are about 10000+ images in the training data.
* There are about 10000+ images in the test data.


## Load the saved model directly ~>

```python
# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
 
# load model
model = load_model('model.h5')
# summarize model.
model.summary()
```

## How to use this project~>

- Star this repo.
- Fork this repo onto your github account.
- Clone it to your local system and play around with the notebook!!

#### Contributor
@prathameshThakur