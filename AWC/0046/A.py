N, L = map(int, input().split())
D = list(map(int, input().split()))
res = -2
for i in range(N):
    if D[i] <= L:
        if res < 0:
            res = i
            continue
        if D[res] < D[i]:
            res = i
        
print(res + 1)
