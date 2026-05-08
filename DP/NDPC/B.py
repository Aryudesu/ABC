from collections import defaultdict

def reachableCount(N: int, graph: dict[int, list[int]])->list[int]:
    result = [0] * N
    memo = {0}
    bfs = {0}
    while bfs:
        nextBFS = set()
        for node in bfs:
            for nextNode in graph[node]:
                result[nextNode] += 1
                if nextNode in memo:
                    continue
                memo.add(nextNode)
                nextBFS.add(nextNode)
        bfs = nextBFS
    return result

def calc(N: int, graph: dict[int, list[int]])->int:
    MOD = 998244353
    result = [0] * N
    result[0] = 1

    inCount = reachableCount(N, graph)

    counter = [0] * N
    counter[0] += 1
    dp = {0}

    while dp:
        nextDP = set()
        for node in dp:
            for nextNode in graph[node]:
                counter[nextNode] += 1
                result[nextNode] = (result[nextNode] + result[node]) % MOD
                if counter[nextNode] == inCount[nextNode]:
                    nextDP.add(nextNode)
        dp = nextDP
    return result[N-1]

result = []
T = int(input())
for _ in range(T):
    graph = defaultdict(list)
    N, M = map(int, input().split())
    for m in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
    result.append(calc(N, graph))
for r in result:
    print(r)
