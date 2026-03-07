from collections import defaultdict


def calc(N, M, P, S, T, graph):
    # BitDPか！！！違うわorz
    # やりたいこととしては，SからTについての経路全てのパターンについて最短距離を計算し，
    # 利得を足したものからWの総和を引いたものが答えかなと思うんだよぉぉぉ
    INF = 10 ** 18
    value = [0] * (1 << N)
    for i in range(1 << N):
        val = 0
        for j in range(N):
            if (1 << j) & i != 0:
                val += P[j]
        value[i] = val

    result = -10 ** 18
    dp = defaultdict(lambda: INF)
    # (mask, 最終到達地点)
    # 戻って来るの考えてなかった・・・・・・orz
    # 終わりです　お疲れ様でした
    # うあぁぁぁ
    dp[(1 << S, S)] = 0
    for n in range(N):
        nextDP = defaultdict(lambda: INF)
        for mask, pos in dp:
            cost = dp[(mask, pos)]
            for nextPos, w in graph[pos]:
                if (1 << nextPos) & mask != 1:
                    nextMask = mask | (1 << nextPos)
                    if (nextMask & (1 << S)) and (nextMask & (1 << T)):
                        result = max(result, value[nextMask] - cost - w)
                    nextDP[(nextMask, nextPos)] = min(nextDP[(nextMask, nextPos)], cost + w)
        dp = nextDP
    return result


N, M = map(int, input().split())
P = list(map(int, input().split()))
S, T = map(int, input().split())
graph = defaultdict(list)
for m in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))
print(calc(N, M, P, S - 1, T - 1, graph))
