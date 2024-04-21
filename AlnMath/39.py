N, Q = [int(l) for l in input().split()]
data = [0] * N
resData = [0] * N
for q in range(Q):
    L, R, X = [int(l) for l in input().split()]
    data[L-1] += X
    if R < N:
        data[R] -= X
s = 0
for i in range(N):
    s += data[i]
    resData[i] = s
result = []
for i in range(N - 1):
    if resData[i] > resData[i+1]:
        result.append(">")
    elif resData[i] < resData[i+1]:
        result.append("<")
    else:
        result.append("=")
print("".join(result))
