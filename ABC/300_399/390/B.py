def calc(N, A):
    for i in range(N - 1):
        if A[i] * A[1] != A[i + 1] * A[0]:
            return False
    return True



N = int(input())
A = [int(l) for l in input().split()]
print("Yes" if calc(N, A) else "No")
