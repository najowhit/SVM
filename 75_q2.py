"""
CREATED BY: NATHAN WHITE
"""

import numpy

raw_data = numpy.genfromtxt('75rules.txt', delimiter=",", dtype=int, usecols=(0, 1, 2, 3, 4, 5, 6))

labels = raw_data[:, 0]
data = raw_data[:, 1:]

rows, columns = numpy.shape(data)
new_data = numpy.zeros((rows, rows+1))


i = 0
for transaction in data:
    j = 0
    for feature in data:
        if numpy.allclose(transaction, feature):
            new_data[i][j] = 1
        j+= 1
    new_data[i][j] = labels[i]
    i+=1

print(new_data)