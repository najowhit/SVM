import numpy
import pandas
from sklearn import svm

raw_data = numpy.genfromtxt('house-votes-84.data.txt', delimiter=",", dtype=str)

#numpy.random.shuffle(raw_data)
labels = raw_data[:, 0]
data = raw_data[:, 1:]

# Convert data set to numerical values
df = pandas.DataFrame(data)
df = df.replace(['y', 'n', '?'], [1, -1, 0])
data = df.values

fold1 = data[0:108]
labels1 = labels[0:108]

fold2 = data[108:217]
labels2 = labels[108:217]

fold3 = data[218:327]
labels3 = labels[218:327]

fold4 = data[327:436]
labels4 = labels[327:436]


#test = numpy.concatenate((fold1, fold2, fold3, fold4))



# Hypothesis Testing
linear_svm = svm.SVC(C=1, kernel='linear')
linear_svm.fit(fold4, labels4)
linear_svm.predict(fold4)
linear_svm.score(fold4, labels4)

# What about the standard deviation?
