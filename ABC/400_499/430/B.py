N, M = map(int, input().split())
S = []
for n in range(N):
    S.append(input())

data = set()
for y in range(N-M+1):
    for x in range(N-M+1):
        tmp1 = 0
        for dy in range(M):
            for dx in range(M):
                tmp2 = 1 if S[y+dy][x+dx]=="#" else 0
                tmp1 = tmp1 * 2 + tmp2
        data.add(tmp1)
print(len(data))
