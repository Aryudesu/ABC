import heapq

N = int(input())
SC = dict()
S = []
heapq.heapify(S)
for n in range(N):
    s, c = [int(l) for l in input().split()]
    SC[s] = c
    heapq.heappush(S, s)
# 小さい順に並び替え
S.sort()
idx = 0
while S:
    sz = heapq.heappop(S)
    # そのサイズの個数
    tmp = SC.get(sz, 0)
    # 合成できなかったら次
    if tmp // 2 == 0:
        idx += 1
        continue
    # 合成できたら合成からあぶれたやつが残る
    SC[sz] = tmp % 2
    # まだ存在してない大きさなら追加する
    if SC.get(sz * 2) is None:
        heapq.heappush(S, sz * 2)
    SC[sz * 2] = SC.get(sz * 2, 0) + tmp//2
    idx += 1
result = 0
for s in SC:
    result += SC.get(s, 0)
print(result)
