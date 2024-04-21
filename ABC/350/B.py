N, Q = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]

data = [1] * (N + 1)
data[0] = 0

for t in T:
    data[t] = 1 - data[t]
print(sum(data))
