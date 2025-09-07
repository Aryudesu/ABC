N, M = [int(l) for l in input().split()]
data = [0] * N
S = input()
T = input()
for m in range(M):
    l, r = [int(l) - 1 for l in input().split()]
    data[l] += 1
    if r + 1 < N:
        data[r + 1] -= 1
s = 0
for idx in range(N):
    s += data[idx]
    if s % 2 == 0:
        print(S[idx], end="")
    else:
        print(T[idx], end="")
print()
