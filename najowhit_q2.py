"""
CREATED BY: NATHAN WHITE
"""

f = open('house-votes-84.data.txt', 'r')
lines = f.readlines()
for line in lines:
    strpline = line.rstrip()
    arr = strpline.split(',')
    newline = [];
    for i in range(len(arr)):
        if arr[i] == 'y':
            newline.append(i)
    if arr[0] == 'republican':
        newline.append(100)
    else:
        newline.append(200)
    print(newline, sep=',')