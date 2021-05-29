# 🥂 WHITE WINE QUALITY PREDICTION

## Aim

The aim is to apply multiple ML classification algorithms and classify the quality of white wine in 5 categories- 4, 5, 6, 7 and 8 on the basis of various factors like volatile acidity, residual sugar, chlorides, free sulfur dioxide, etc. 

## ML Algorithms Used

1. K Nearest Neighbours

The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems. The algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other. 

The KNN Algorithm:

a. Load the data

b. Initialize K to your chosen number of neighbors.

c. For each example in the data.
-  Calculate the distance between the query example and the current example from the data.
-  Add the distance and the index of the example to an ordered collection.

d. Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances.

e. Pick the first K entries from the sorted collection.

f. Get the labels of the selected K entries.

g. In classification, return the mode of the K labels.

2. Support Vector Machines

The objective of the support vector machine algorithm is to find a hyperplane in an N-dimensional space(N — the number of features) that distinctly classifies the data points. To separate the two classes of data points, there are many possible hyperplanes that could be chosen. Our objective is to find a plane that has the maximum margin, i.e the maximum distance between data points of both classes. Maximizing the margin distance provides some reinforcement so that future data points can be classified with more confidence.

3. Decision Trees

Decision Tree Classifier is a simple and widely used classification technique. It applies a straitforward idea to solve the classification problem. Decision Tree Classifier poses a series of carefully crafted questions about the attributes of the test record. Each time time it receive an answer, a follow-up question is asked until a conclusion about the class label of the record is reached.

4. Random Forest Classifier

The Random forest or Random Decision Forest is a supervised Machine learning algorithm used for classification, regression, and other tasks using decision trees. The Random forest classifier creates a set of decision trees from a randomly selected subset of the training set. It is basically a set of decision trees (DT) from a randomly selected subset of the training set and then It collects the votes from different decision trees to decide the final prediction.

5. Naive Bayes

Naive Bayes methods are a set of supervised learning algorithms based on applying Bayes’ theorem with the “naive” assumption of conditional independence between every pair of features given the value of the class variable. GaussianNB implements the Gaussian Naive Bayes algorithm for classification.

## Source

https://www.kaggle.com/piyushagni5/white-wine-quality
