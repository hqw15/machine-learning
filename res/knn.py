import numpy as np


def distance(newData, dataSet):

	diff = np.tile(newData, (dataSet.shape[0], 1)) - dataSet
	diff = np.sqrt( (diff**2).sum(axis = 1) )

	return diff


		




def KNN(dataSet, labels, newData, k):

	assert k <= dataSet.shape[0]

	diff = distance(newData, dataSet)

	indexs = np.argsort(diff)

	counter = {}
	for i in range(k):
		label = labels[indexs[i]]
		counter[label] = counter.get(label, 0) + 1

	counter = sorted(counter.items(), key = lambda x:x[1], reverse = True)

	return counter[0][0]





dataSet = np.ones([3,4])
labels = [1,2,1]

newData = [1,2,3,4]

label = KNN(dataSet, labels, newData, 3)
print (label)