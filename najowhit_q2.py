"""
CREATED BY: NATHAN WHITE
"""
import sys

f = open('house-votes-84.data.txt', 'r')
temp = sys.stdout
sys.stdout = open('itemset.txt', 'w')
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
    print(*newline, sep=',')
sys.stdout.close()
sys.stdout = temp