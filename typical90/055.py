from itertools import combinations

N, P, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
result = 0
for data in combinations(A, 5):
    tmp = 1
    for d in data:
        tmp = (tmp * d) % P
    if tmp == Q:
        result += 1
print(result)
