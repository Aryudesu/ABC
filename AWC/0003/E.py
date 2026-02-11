import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

def dfs(depth: int, N: int, M: int, trackData: list[int], W: list[int], C: list[int], dfsMemo = set())->bool:
    ttd = tuple(trackData)
    if ttd in dfsMemo:
        return False
    dfsMemo.add(ttd)
    if N == depth:
        return True
    w = W[depth]
    memo = set()
    for m in range(M):
        if trackData[m] + w > C[m]:
            continue
        if C[m] - trackData[m] in memo:
            continue
        memo.add(C[m] - trackData[m])
        trackData[m] += w
        if dfs(depth + 1, N, M, trackData, W, C, dfsMemo):
            return True
        trackData[m] -= w
    return False

N, M = map(int, input().split())
W = list(map(int, input().split()))
C = list(map(int, input().split()))
W.sort(reverse=True)
C.sort(reverse=True)
trackData = [0] * M
if dfs(0, N, M, trackData, W, C):
    print("Yes")
else:
    print("No")
