N = int(input())
LR = []
for _ in range(N):
    l, r = input().split()
    LR.append((l, r))
result = 0
for i in range(N-1):
    if LR[i][1] == LR[i+1][0]:
        result += 1
print(result)
