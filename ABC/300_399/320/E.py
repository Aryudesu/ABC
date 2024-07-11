import heapq

N, M = [int(l) for l in input().split()]
result = [0] * N

# いる人一覧
iru = [l for l in range(N)]
heapq.heapify(iru)
# 出ていって戻る時間
next_modoru = []
heapq.heapify(next_modoru)
modoru_set = set()
deru_list = dict()
for m in range(M):
    T, W, S = [int(l) for l in input().split()]
    if next_modoru:
        while next_modoru:
            tmp = heapq.heappop(next_modoru)
            if tmp > T:
                heapq.heappush(next_modoru, tmp)
                break
            modop = deru_list.get(tmp, [])
            for p in modop:
                heapq.heappush(iru, p)
    if iru:
        top = heapq.heappop(iru)
        result[top] += W
        ts = T + S
        if not ts in modoru_set:
            heapq.heappush(next_modoru, ts)
            modoru_set.add(ts)
        tmp = deru_list.get(ts, [])
        tmp.append(top)
        deru_list[ts] = tmp

for r in result:
    print(r)
