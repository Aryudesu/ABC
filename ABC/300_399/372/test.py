from sortedcontainers import SortedSet as sset

data1 = sset([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
data2 = sset([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
data = data2.update(data1)
print(data)
data3 = sset(data[-10:])
print(len(data3), data3)
