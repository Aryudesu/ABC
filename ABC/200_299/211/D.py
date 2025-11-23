from collections import defaultdict

N, M = map(int, input().split())
MOD = 10**9 + 7
graph = defaultdict(list)
for m in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
memo = {1}
nodes = {1}
dp = [0] * (N + 1)
dp[1] = 1
while nodes:
    nextDp = set()
    for node in nodes:
        nextNodes = graph[node]
        for nextNode in nextNodes:
            if nextNode in memo:
                continue
            dp[nextNode] = (dp[nextNode] + dp[node]) % MOD
            nextDp.add(nextNode)
    memo.update(nextDp)
    nodes = nextDp
print(dp[N])
