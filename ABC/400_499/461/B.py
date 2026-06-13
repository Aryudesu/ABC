def isOk(N : int, A: list, B: list)->bool:
    for idx in range(N):
        if  B[A[idx]-1] - 1 != idx:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print("Yes" if isOk(N, A, B) else "No")
