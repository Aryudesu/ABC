from sortedcontainers import SortedSet

def debug(data: list[list[int]]):
    for d in data:
        print(*d)

def calc(N: int, M: int, X: list[int], Y: list[int]):
    result = [[None] * M for _ in range(N)]
    nums = SortedSet(range(1, N * M + 1))
    xmemo = dict()
    for idx in range(N):
        xmemo[X[idx]] = idx
    for idx in range(M):
        if Y[idx] in xmemo:
            idx2 = xmemo[Y[idx]]
            result[idx2][idx] = Y[idx]
    debug(result)

result = []
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    calc(N, M, X, Y)
