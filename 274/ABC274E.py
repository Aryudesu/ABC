def calc(N, M, XY):
    min = 10 ** 10
    data = [min] * (2**(N + M))
    print(data)


N, M = [int(l) for l in input().split()]
XY = []
for n in range(N + M):
    XY.append([int(l) for l in input().split()])
print(calc(N, M, XY))
