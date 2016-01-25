'''
two features, one class label
'''
def loadDataSet():
	dataMat = []; labelMat= []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat

def sigmoid(inX):
	return 1.0/(1+exp(-inX))



'''
Note: numpy matrix is different from numpy 2D array

dataMat numpy matrix 100*3 
classlabels 1*100
'''
def gradAscent(dataMatIn, classLabels):
	dataMatrix = mat(dataMatIn)
	labelMat = mat(classLabels).transpose()
	m,n = shape(dataMatrix)
	alpha = 0.001 # learning rate
	maxCycles = 500 # iteration number
	weights = ones((n,1))
	for k in range(maxCycles):
		h = sigmoid(dataMatrix*weights)
		error = label-h
		weights = weights + alpha*dataMatrix*error
	return weights




