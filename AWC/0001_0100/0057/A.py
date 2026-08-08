N, X = map(int, input().split())
A = list(map(int, input().split()))
B = [A[0]]
for i in range(1, N-1):
    if A[i-1] == A[i+1] and A[i-1] != A[i]:
        B.append(0)
    else:
        B.append(A[i])
if N > 1:
    B.append(A[-1])
result = X
for b in B:
    result ^= b
print(result)
