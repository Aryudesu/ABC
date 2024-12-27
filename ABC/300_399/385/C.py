N = int(input())
H = [int(l) for l in input().split()]
result = 1
for i in range(N):
    # 間隔
    for j in range(1, N):
        tmp = 0
        for k in range(i, N, j):
            if H[k] == H[i]:
                tmp += 1
            else:
                break
        result = max([result, tmp])
print(result)
