data = []


def makeData(N, num):
    if N == 0:
        data.append(num)
    n = num % 10
    for i in range(n):
        makeData(N-1, num * 10 + i)


for i in range(10):
    for j in range(10):
        makeData(i, j)
data.sort()
print(data[int(input())])
