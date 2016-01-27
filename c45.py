'''
A new version of decision tree
with Tree pruning and feature engineering

C4.5

'''
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
  
  return bestFeat
