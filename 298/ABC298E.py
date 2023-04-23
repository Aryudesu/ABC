N, A, B, P, Q = [int(l) for l in input().split()]
mab = max([A, B])
data = []
for i in range(mab + 1):
    if i < A:
        data.append([0, 1])
    elif i == A:
        data.append([1, 1])
    elif i > A and i <= A + P:
        data.append([P - i + A + 1, P])
    else:
        data.append([0, 1])
for i in range(mab + 1, N):
    pass
