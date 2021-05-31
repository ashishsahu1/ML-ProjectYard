# SPECTRAL CLUSTERING

## Introduction

Spectral Clustering treats each data point as a graph-node and thus transforms the clustering problem into a graph-partitioning problem. A typical implementation consists of three fundamental steps:-

1. Pre-processing

▪ Construct a matrix representation of the graph.

2. Decomposition

▪ Compute eigenvalues and eigenvectors of the matrix.

▪ Map each point to a lower-dimensional representation based on one or more eigenvectors.

3. Grouping

▪ Assign points to two or more clusters, based on the new representation.

Clustering techniques, like K-Means, assume that the points assigned to a cluster are spherical about the cluster centre. This is a strong assumption and may not always be relevant. In such cases, Spectral Clustering helps create more accurate clusters. It can correctly cluster observations that actually belong to the same cluster, but are farther off than observations in other clusters, due to dimension reduction.

## Advantages

▪ Elegant and well-founded mathematically.

▪ Works quite well when relations are approximately transitive (like similarity).

## Disadvantages

▪ Very noisy datasets cause problems; performance can drop suddenly from good to terrible.

▪ Expensive for very large datasets.

## References

▪ https://www.absolutdata.com/learn-analytics-whitepapers-webinars/spectral-clustering/

▪ https://www.geeksforgeeks.org/ml-spectral-clustering/

▪ http://cobweb.cs.uga.edu/~squinn/mmd_s15/lectures/lecture10_feb4.pdf
