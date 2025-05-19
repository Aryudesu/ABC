def rotate(A):
    N = len(A)
    result = []
    for w in range(N):
        tmp = []
        for h in range(N):
            tmp.append(A[N-h-1][w])
        result.append(tmp)
    return result

def calcDiff(A, B):
    N = len(A)
    result = 0
    for h in range(N):
        for w in range(N):
            if A[h][w] != B[h][w]:
                result += 1
    return result

N = int(input())
S = []
T = []
result = N ** 2
for n in range(N):
    S.append(list(input()))
for n in range(N):
    T.append(list(input()))
result = min(result, calcDiff(S, T))
U = rotate(S)
result = min(result, 1 + calcDiff(U, T))
U = rotate(U)
result = min(result, 2 + calcDiff(U, T))
U = rotate(U)
result = min(result, 3 + calcDiff(U, T))
print(result)
