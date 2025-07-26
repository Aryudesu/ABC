import heapq

INF = 10 ** 18
H, W = [int(l) for l in input().split()]
A = []
for h in range(H):
    A.append([int(l) for l in input().split()])
P = [int(l) for l in input().split()]
# 最大不足分
data = [[INF for _ in range(W)] for _ in range(H)]
# (不足分, そのマスに到着したときの所持金, y, x)
node = [(0, 0, 0, 0)]
heapq.heapify(node)
update_result = False
while node:
    fusoku, n, y, x = heapq.heappop(node)
    # そのマスを掘る
    new_n = n - A[y][x]
    new_fusoku = max(new_n + P[y+x], fusoku)
    # 既に不足分が下のデータが見つかってる場合は以降の走査を辞める
    if data[y][x] <= new_fusoku:
        continue
    data[y][x] = new_fusoku
    max_fusoku = max(fusoku, new_fusoku)
    new_n += P[y+x]
    # 移動
    if y + 1 < H:
        new_y = y + 1
        new_x = x
        heapq.heappush(node, (max_fusoku, new_n, new_y, new_x))
    if x + 1 < W:
        new_y = y
        new_x = x + 1
        heapq.heappush(node, (max_fusoku, new_n, new_y, new_x))
print(data[-1][-1])
