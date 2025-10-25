def calc(N: int, A: list[int], target: int) -> bool:
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if A[i] + A[j] + A[k] == target:
                    return True
    return False

N = int(input())
A = [int(l) for l in input().split()]
print("Yes" if calc(N, A, 1000) else "No")
