N, M = map(int, input().split())
A = [int(l) for l in input().split()]
data = [M] * N
for a in A:
    data[a-1] -= 1
for d in data:
    print(d)
