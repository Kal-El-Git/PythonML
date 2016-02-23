# K Nearest Neighbor classifier
import numpy as np

def distance(p0,p1):
	return np.sum((p0-p1)**2)

def nn_classify(training_set, training_labels,new_example):
	dists= np=np.array([distance(t,new_example) 
		for t in training_set])
	nearest = dists.argmin()
	return training_labels[nearest]

# normalize with Z distribution
features -= features.mean(axis=0)
features /= features.std(axis=0)

