N = int(input())
H = [int(l) for l in input().split()]
Field = [10**18] * N
Field[0] = 0
for n in range(N):
    for k in range(1, 3):
        if n + k < N:
            Field[n + k] = min([Field[n + k], Field[n] + abs(H[n + k] - H[n])])
print(Field[-1])
