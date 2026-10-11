from sortedcontainers import SortedList

N, K = map(int, input().split())
A = list(map(int, input().split()))
L = [True]
R = [True]
for i in range(1, N):
    L.append(L[i-1] and A[i-1] <= A[i])
for i in range(N-2, -1, -1):
    R.append(R[-1] and A[i] <= A[i+1])
R.reverse()

data = SortedList()
for k in range(K):
    data.add(A[k])
isOk = False
isOk = R[K] and data[-1] <= A[K]
# print(0, K, data)
for i in range(K, N):
    data.add(A[i])
    data.discard(A[i-K])
    if i + 1 < N:
        isOk = isOk or (R[i+1] and L[i-K] and A[i-K] <= data[0] and data[-1] <= A[i+1])
    # print(i-K, i, data, isOk)
isOk = isOk or (L[N-1-K] and A[N-1-K] <= data[0])
print("Yes" if isOk else "No")
