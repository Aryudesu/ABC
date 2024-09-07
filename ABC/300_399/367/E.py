def replace(A, B):
    """AをBについての位置の入れ替えを行います"""
    result = [None] * len(A)
    for n in range(len(A)):
        result[A[n]] = B[n]
    return result

N, K = [int(l) for l in input().split()]
X = [int(l)-1 for l in input().split()]
A = [int(l) for l in input().split()]
print(X)
print(replace(X, X))
