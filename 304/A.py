N = int(input())
SA = []
min_idx = 0
for n in range(N):
    S, A = [l for l in input().split()]
    SA.append([S, int(A)])
    if SA[n][1] < SA[min_idx][1]:
        min_idx = n

for n in range(N):
    print(SA[(min_idx + n) % N][0])
