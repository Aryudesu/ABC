def calc(N: int, M: int, A: list[int], B: list[int])->int:
    A.sort()
    B.sort()
    if M == 0:
        pass
    elif A[0] < B[0] < A[-1]:
            return -1
    elif A[0] < B[-1] < A[-1]:
        return -1
    elif A[0] <= A[-1] < B[0]:
        pass
    elif B[-1] < A[0] <= A[-1]:
        pass
    else:
        isOk = False
        for idx in range(M-1):
            if A[0] < B[idx]:
                continue
            if B[idx] < A[0] <= A[-1] < B[idx+1]:
                isOk = True
        if not isOk:
            return -1
    mid = A[N//2]
    result = 0
    for a in A:
        result += abs(a - mid)
    return result

N, M = map(int, input().split())
A = list(map(int, input().split()))
if M > 0:
    B = list(map(int, input().split()))
else:
    B = []
print(calc(N, M, A, B))
