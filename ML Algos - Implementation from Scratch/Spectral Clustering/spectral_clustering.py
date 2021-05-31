'''
Aim: To implement Spectral Clustering from scratch.

'''

import numpy as np

'''
Primary Functions:
nearest_neighbor_graph(X)
    -X: list of data
compute_laplacian(W)
    -W: np.array of adjacency matrix
get_eigvecs(L, k)
    -L: np.array of graph Laplacian
    -k: integer number of clusters
kmeans_clustering(X, k)
    -X: np.array of data
    -k: integer number of clusters
spectral_clustering(X, k)
    -X: list of data
    -k: integer number of clusters
'''

def pairwise_distances(X, Y):

    #Calculate distances from every point of X to every point of Y

    #start with all zeros
    distances = np.empty((X.shape[0], Y.shape[0]), dtype='float')

    #compute adjacencies
    for i in range(X.shape[0]):
        for j in range(Y.shape[0]):
            distances[i, j] = np.linalg.norm(X[i]-Y[j])

    return distances

def nearest_neighbor_graph(X):
    '''
    Calculates nearest neighbor adjacency graph.
    '''
    X = np.array(X)

    # for smaller datasets use sqrt(#samples) as n_neighbors. max n_neighbors = 10
    n_neighbors = min(int(np.sqrt(X.shape[0])), 10)

    #calculate pairwise distances
    A = pairwise_distances(X, X)

    #sort each row by the distance and obtain the sorted indexes
    sorted_rows_ix_by_dist = np.argsort(A, axis=1)

    #pick up first n_neighbors for each point (i.e. each row)
    #start from sorted_rows_ix_by_dist[:,1] because because sorted_rows_ix_by_dist[:,0] is the point itself
    nearest_neighbor_index = sorted_rows_ix_by_dist[:, 1:n_neighbors+1]

    #initialize an nxn zero matrix
    W = np.zeros(A.shape)

    #for each row, set the entries corresponding to n_neighbors to 1
    for row in range(W.shape[0]):
        W[row, nearest_neighbor_index[row]] = 1

    #make matrix symmetric by setting edge between two points if at least one point is in n nearest neighbors of the other
    for r in range(W.shape[0]):
        for c in range(W.shape[0]):
            if(W[r,c] == 1):
                W[c,r] = 1

    return W

def compute_laplacian(W):
    # calculate row sums
    d = W.sum(axis=1)

    #create degree matrix
    D = np.diag(d)
    L =  D - W
    return L

def get_eigvecs(L, k):
    '''
    Calculate Eigenvalues and EigenVectors of the Laplacian Matrix.
    Return k eigenvectors corresponding to the smallest k eigenvalues.
    Uses real part of the complex numbers in eigenvalues and vectors.
    The Eigenvalues and Vectors will be complex numbers when using
    NearestNeighbor adjacency matrix for W.
    '''

    eigvals, eigvecs = np.linalg.eig(L)
    # sort eigenvalues and select k smallest values - get their indices
    ix_sorted_eig = np.argsort(eigvals)[:k]

    #select k eigenvectors corresponding to k-smallest eigenvalues
    return eigvecs[:,ix_sorted_eig]

def k_means_pass(X, k, n_iters):
    '''
    Run a single pass of K-Means
        X: Input data nxm matrix. n samples, m features per sample.
        k: Number of required clusters.
        n_iters: Iterations to run for centroid convergence.
    Returns: centers, labels
        centers: Centroids of the clusters.  shape=(k,m)
        labels:  Labels of each data sample in X. Shape (n,), each label value 0..k-1
    '''

    #generate random k indexes
    rand_indexes = np.random.permutation(X.shape[0])[:k]

    #pick random k initial centroids
    centers = X[rand_indexes]

    for iteration in range(n_iters):
        #calculate distances for every point in X to each of the k centers
        distance_pairs = pairwise_distances(X, centers)

        #assign label to each point - index of the centroid with smallest distance
        labels = np.argmin(distance_pairs, axis=1)
        new_centers = [np.nan_to_num(X[labels == i].mean(axis=0)) for i in range(k)]
        new_centers = np.array(new_centers)

        #check for convergence of the centers
        if np.allclose(centers, new_centers):
            break

        #update centers for next iteration
        centers = new_centers


    return centers, labels

def cluster_distance_metric(X, centers, labels):
    '''
    Metric to evaluate how close points in the clusters are to their centroid
    Returns sum of all distances of points to their corresponding centroid
    '''
    return sum(np.linalg.norm(X[i]-centers[labels[i]]) for i in range(len(labels)))

def k_means_clustering(X, k):
    solution_labels = None
    current_metric = None

    #run k_means pass, so that each pass starts at a different initial random point.
    for pass_i in range(10):
        #perform a pass
        centers, labels = k_means_pass(X, k, 1000)

        #calculate distance metric for the solution
        new_metric = cluster_distance_metric(X, centers, labels)
        #keep track of the smallest metric and its solution
        if current_metric is None or new_metric < current_metric:
            current_metric = new_metric
            solution_labels = labels

    return solution_labels


def spectral_clustering(X, k):

    #create weighted adjacency matrix
    W = nearest_neighbor_graph(X)

    #create unnormalized graph Laplacian matrix
    L = compute_laplacian(W)

    #create projection matrix with first k eigenvectors of L
    E = get_eigvecs(L, k)

    #return clusters using k-means on rows of projection matrix
    f = k_means_clustering(E, k)
    return np.ndarray.tolist(f)