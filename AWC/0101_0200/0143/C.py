import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')

N, M = map(int, input().split())
C = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)

result = set(range(N))
memo = [False] * N

def calc(node: int):
    memo[node] = True
    for nextNode in graph[node]:
        if C[node] == C[nextNode]:
            continue
        if memo[nextNode]:
            continue
        calc(nextNode)
calc(0)
S = sum(memo)
if S == N:
    print("COMPLETE")
else:
    disp = []
    for n in range(N):
        if not memo[n]:
            disp.append(n + 1)
    print(*disp)
