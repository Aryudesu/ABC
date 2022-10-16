N = int(input())
abc = []
for n in range(N):
    abc.append([int(l) for l in input().split()])
taro = [[0, 0, 0] for n in range(N)]
taro[0] = abc[0]
for n in range(1, N):
    for k in range(3):
        for l in range(3):
            if k == l:
                continue
            taro[n][k] = max([taro[n][k], taro[n-1][l] + abc[n][k]])
print(max(taro[-1]))
