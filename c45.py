'''
A new version of decision tree
with Tree pruning and feature engineering

C4.5

Pseudo Code

generate d_tree
create node N
if all in same class:
  return N
if attr_list is empty:
  return majority
best feature = findBestFeat()
mark N as best feature
if best feature is discrete and multi-class:
  remove from feature list
for each class from split:
  D is a subset
  if D is empty:
    create a node that is marked with best feature
  else
    recursively call d_tree, attach the node on N
return N
'''

#Calculate the entropy, or, the Info of dataset
def calcEntropy(dataSet):
  numEntries = len(dataSet)
  labelCounts ={}
  for featVec in dataSet:
    currentLabel = featVec[-1]
    if currentLabel not in labelCounts:
      labelCounts[currentLabel]=0
    labelCounts[currentLabel]+=1
  Ent = 0.0
  for key in labelCounts:
    prob = float(labelCounts[key])/numEntries
    Ent-=prob*log(prob)
  return Ent


#Apply Info Gain Ratio
def findBestSplit(dataSet):
  numFeatures = len(dataSet)-1
  baseEntropy = calcEntropy(dataSet)
  bestRatio=0.0
  bestFeat =-1
  for i in range(numFeatures):
		featValues = [example[i] for example in dataSet]
		uniqueFeatValues = set(featValues)
		newEntropy = 0.0
		for val in uniqueFeatValues:
			subDataSet = splitData(dataSet,i,val)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob*calcShannonEnt(subDataSet)
		gain = baseEntropy - newEntropy	
		if ( gain / newEntropy) > bestRatio:
			bestRatio = gain / newEntropy
			baseFeat = i
	return bestFeat
  
  return bestFeat
