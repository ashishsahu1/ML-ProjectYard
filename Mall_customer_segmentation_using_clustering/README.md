# K- Means Clustering

K-means clustering is one of the simplest and popular unsupervised machine learning algorithms.
Typically, unsupervised algorithms make inferences from datasets using only input vectors without referring to known, or labelled, outcomes.
A cluster refers to a collection of data points aggregated together because of certain similarities.

You’ll define a target number  _k_, which refers to the number of centroids you need in the dataset. A centroid is the imaginary or real location representing the center of the cluster.

Every data point is allocated to each of the clusters through reducing the in-cluster sum of squares.
In other words, the K-means algorithm identifies  _k_  number of centroids, and then allocates every data point to the nearest cluster, while keeping the centroids as small as possible.
The  _‘means’_  in the K-means refers to averaging of the data; that is, finding the centroid.

# **How the K-means algorithm works**
To process the learning data, the K-means algorithm in data mining starts with a first group of randomly selected centroids, which are used as the beginning points for every cluster, and then performs iterative (repetitive) calculations to optimize the positions of the centroids

It halts creating and optimizing clusters when either:

-   The centroids have stabilized — there is no change in their values because the clustering has been successful.
-   The defined number of iterations has been achieved.
- 
**Read Data**
We receive input as a text file (‘data.txt’). Each line represents an item, and it contains numerical values (one for each feature) split by commas.

**Initialize Means**
We want to initialize each mean’s values in the range of the feature values of the items. For that, we need to find the min and max for each feature.
**Euclidean Distance**
We will be using the euclidean distance as a metric of similarity for our data set (note: depending on your items, you can use another similarity metric).

**Update Means**
To update a mean, we need to find the average value for its feature, for all the items in the mean/cluster. We can do this by adding all the values and then dividing by the number of items, or we can use a more elegant solution.
	m = (m*(n-1)+x)/n
	where _m_ is the mean value for a feature, _n_ is the number of items in the cluster and _x_ is the feature value for the added item.

**Classify Items**
Now we need to write a function to classify an item to a group/cluster. For the given item, we will find its similarity to each mean, and we will classify the item to the closest one.
**Find Means**

To actually find the means, we will loop through all the items, classify them to their nearest cluster and update the cluster’s mean. We will repeat the process for some fixed number of iterations. If between two iterations no item changes classification, we stop the process as the algorithm has found the optimal solution.

The other popularly used similarity measures are:-
1.  **Cosine distance:**  It determines the cosine of the angle between the point vectors of the two points in the n dimensional space
![enter image description here](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-3fd139cbbf734c3a069c4c1416528409_l3.svg)

2.  **Manhattan distance:**  It computes the sum of the absolute differences between the co-ordinates of the two data points.

![d = \sum_{n} X{_{i}}-Y{_{i}} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-ac9b0b227cd80bf647d1df50d5ac3512_l3.svg "Rendered by QuickLaTeX.com")

3.  **Minkowski distance:**  It is also known as the generalised distance metric. It can be used for both ordinal and quantitative variables

![d = (\sum _{n}|X_{i}-Y_{i}|^{\frac{1}{p}})^{p} ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-b9b33ef0586a88a621a0932327048647_l3.svg "Rendered by QuickLaTeX.com")


