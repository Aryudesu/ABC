from itertools import permutations

N = int(input())
A = []
for idx in range(2*N - 1):
    A.append([int(l) for l in input().split()])

result = 0
for data in permutations(range(2*N - 1), 2*N - 1):
    print(data)
    tmp = 0
    f = False
    if data[0] % 2:
        continue
    for idx in range(N - 1):
        a = data[2*idx]
        b = data[2*idx + 1]
        if a > b:
            f = True
            break
        d = A[a][b-a-1]
        if idx == 0:
            tmp = d
        else:
            tmp = tmp ^ d
    a = data[2*N - 4]
    b = 2 * N - 1
    d = A[a][b - a + 1]
    if a > b:
        continue
    if f:
        continue
    if result < tmp:
        result = tmp
print(result)
