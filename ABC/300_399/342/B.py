N = int(input())
P = [int(l) for l in input().split()]
data = dict()
for idx in range(N):
    data[P[idx]] = idx
result = []
Q = int(input())
for _ in range(Q):
    A, B = [int(l) for l in input().split()]
    if data[A] < data[B]:
        result.append(A)
    else:
        result.append(B)
for r in result:
    print(r)
