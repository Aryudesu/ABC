def calc(N, A):
    for n in range(N - 1):
        if A[n] != A[n+1]:
            return False
    return True


N = int(input())
A = [int(l) for l in input().split()]
print("Yes" if calc(N, A) else "No")
