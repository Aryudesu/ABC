N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
pointer = 0
result = []
for _ in range(Q):
    T, x, y = [int(l) for l in input().split()]
    if T == 1:
        x_ = (pointer + x - 1) % N
        y_ = (pointer + y - 1) % N
        A[x_], A[y_] = A[y_], A[x_]
    elif T == 2:
        pointer = (pointer - 1) % N
    elif T == 3:
        result.append(A[(pointer + x - 1) % N])
for r in result:
    print(r)
