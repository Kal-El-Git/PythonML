from math import log

# data structures
'''
    dataSet = m * (n+1) matrix. M entries, N features, 1 class label
    features = list of feature names
    classList = list of classes, duplicate elements

'''

#Pseudo Code
'''
Check if every item in the dataset is in the same class: If so return the class label
Else
find the best feature to split the data split the dataset
create a branch node
for each split
call createBranch and add the result to the branch node
return branch node

'''
def createDataSet():
	dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
	features = ['no surfacing', 'flippers']
	return dataSet, features


def treeGrowth(dataSet, features):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0])==len(classList):
		return classList[0]
	if len(dataSet[0]) == 1 # only a class label is left
		return classify(classList)# find the majority class

	bestFeat = findBestSplit(dataSet)
	bestFeatLabel = features[bestFeat]
	myTree ={bestFeatLabel:{}}
	featValues = [example[bestFeat] for example in dataSet]
	uniqueFeatValues =set(featValues)
	del features[bestFeat]
	for values in uniqueFeatValues:
		subDataSet = splitDataSet(dataSet,bestFeat,values)
		myTree[bestFeatLabel][values] =treeGrowth(subDataSet,features)

	return myTree


#return majority of the class list
#class with the most votes 
def classify(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote]=0
		classCount[vote]+=1
	sortedClassCount = sorted(classCount.iteritems(),key=operator.itermgetter(1),reverse=True)
	return sortedClassCount[0][0]


def findBestSplit(dataSet):
	numFeatures = len(dataSet[0])-1
	baseEntropy= calcShannonEnt(dataSet)
	bestInfoGain =0.0
	bestFeat =-1
	#Calculate info gain
	for i in range(numFeatures):
		featValues = [example[i] for example in dataSet]
		uniqueFeatValues = set(featValues)
		newEntropy = 0.0
		for val in uniqueFeatValues:
			subDataSet = splitData(dataSet,i,val)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calcShannonEnt(subDataSet)
		if ( baseEntropy - newEntropy) > bestInfoGain:
			bestInfoGain = baseEntropy - newEntropy
			baseFeat = i
	return bestFeat

#Calculate Shannon Entropy
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts= {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts: # increment hash value
			labelCounts[currentLabel]=0
		labelCounts[currentLabel]+=1
	shannonEnt =0.0
	for key in labelCounts: # in the keys
		prob = float(labelCounts[key])/numEntries # explicit casting
		shannonEnt +=(-1)*prob*log(prob)
	return shannonEnt


#feat -- the index of features
#values -- a specific value for feature "feat"
#This function removes the target feature from the feature list
def splitDataSet(dataSet,feat,values):
	retDataSet = []
	for featVev in dataSet:
		if featVec[feat] == values:
			reducedFeatVec = featVec[:feat]
			reducedFeatVec.extend(featVec[feat+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

#predict function for new datast
def predict(tree, newObject):
	while(isinstance(tree,dict)):
		key = tree.keys()[0]
		tree = tree[key][newObject]
	return tree


