N, T, C, D = map(int, input().split())
W = list(map(int, input().split()))
c1 = 0
c2 = 0
for i in range(N):
    w = W[i]
    if w >= T:
        c1 += D
        c2 += C
print(min(c1, c2))
