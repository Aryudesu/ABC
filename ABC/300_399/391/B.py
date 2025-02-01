def isOk(y, x, N, M, S, T):
    for dy in range(M):
        for dx in range(M):
            if S[y + dy][x + dx] != T[dy][dx]:
                return False
    return True

def calc(N, M, S, T):
    for y in range(N - M + 1):
        for x in range(N - M + 1):
            if isOk(y, x, N, M, S, T):
                return [y, x]
    raise Exception()

N, M = [int(l) for l in input().split()]
S = []
for n in range(N):
    S.append(input())
T = []
for m in range(M):
    T.append(input())
y, x = calc(N, M, S, T)
print(y + 1, x + 1)
