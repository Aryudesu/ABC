def calc(N, A):
    for idx in range(N - 1):
        if A[idx] >= A[idx + 1]:
            return False
    return True


N = int(input())
A = [int(l) for l in input().split()]
print("Yes" if calc(N, A) else "No")

