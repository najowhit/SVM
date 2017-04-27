"""
CREATED BY: NATHAN WHITE
"""
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


def svm_classify(training1, training2, training_labels1, training_labels2, test_data, test_labels):

    combined_train = numpy.concatenate((training1, training2))
    combined_labels = numpy.concatenate((training_labels1, training_labels2))

    linear_svm.fit(combined_train, combined_labels)
    linear_svm.predict(test_data)
    accuracy = linear_svm.score(test_data, test_labels)
    return accuracy



# Fold1 as test, Fold2 & Fold3 as training
fold23 = numpy.concatenate((fold2, fold3))
labels23 = numpy.concatenate((labels2, labels3))
linear_svm.fit(fold23, labels23)

linear_svm.predict(fold1)
print(linear_svm.score(fold1, labels1))
print(svm_classify(fold2, fold3, labels2, labels3, fold1, labels1))

# Fold2 as test, Fold1 & Fold3 as training
fold13 = numpy.concatenate((fold1, fold3))
labels13 = numpy.concatenate((fold1, fold3))

linear_svm.predict(fold2)



