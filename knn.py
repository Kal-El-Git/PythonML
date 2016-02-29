
# KNN  K-Nearest-Neighbor implementation in Python

'''
Pros: high accuracy, insensitive to outliers, no data entry assumption
Cons: high time complexity, high space complexity
suitable for: numerical, category  

'''

# usually k<=20
'''
Process Description
1) collect data 
2) data integration
3) analyzed
4) training
5) testing
6) use algorithm to classify
'''

# load data (dataset and labels)
from numpy import *
import operator
def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

'''
Algorithm Description
1) calculate distance between known points and test points
2) sort in ASC order
3) pick k points that have smallest distance
4) calculate frequency of labels
5) return the highest frequency as label

'''

def classfiy(inX, dataSet,labels,k):
	#Calculate the distance 
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX, (dataSetSize,1))- dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	#Count the labels and sort
	classCount={}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]] 
		classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
	#Sort the dictionary by key and return the key with largest vote
	return sortedClassCount[0][0]
