def calc(N, A):
    for i in range(N - 2):
        if A[i] == A[i + 1] and A[i + 1] == A[i + 2]:
            return True
    return False

N = int(input())
A = [int(l) for l in input().split()]
print("Yes" if calc(N, A) else "No")
