def calc(N, T, A):
    for i in range(N):
        if T[i] == A[i] and T[i] == "o":
            return True
    return False

N = int(input())
T = input()
A = input()
print("Yes" if calc(N, T, A) else "No")
