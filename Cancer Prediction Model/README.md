# BREAST CANCER PREDICTION

## GOAL

The main goal is to predict whether a patient who is suffering from breast cancer is of which type. Benign or Malignant.

## DATASET

DATASET - "https://www.kaggle.com/uciml/breast-cancer-wisconsin-data?select=data.csv". I have taken the dataset from Kaggle.

## WHAT I HAD DONE

- Firstly imported the required libraries needed for the project
- Taking path of the dataset as input and reading it using pd.read_csv.
- To make a good prediction, I had dropped few unnamed and irrelevent data from the dataset. 
- With the well needed data, I had trained and tested using train_test_split from sklearn.
- Finally, I had incorporated them using 4 models to compare the accuracy.

## MODELS USED

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Classifier

## LIBRARIES NEEDED

1. Numpy
2. Pandas
3. MatplotLib
4. Seaborn

## CONCLUSION

With comparison, I could notice that Logistic Regression(97.07%) and Support Vector Classifier(95.32%) has highest accuracy.
