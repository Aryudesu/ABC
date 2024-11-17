from atcoder.dsu import DSU

N, Q = [int(l) for l in input().split()]
# data[代表] = [色, 要素数, 最小, 最大]
data = dict()
# color[色] = マスの数
color = dict()
dsu = DSU(N)
result = []
for q in range(Q):
    query = [int(l) - 1 for l in input().split()]
    if query[0] == 0:
        n, x, c = query
        # 代表元取得
        leader = dsu.leader(x)
        # その範囲のデータ取得
        leader_data = data.get(leader, [leader, 1, leader, leader])
        # 現在の色の代表元取得後に代表元から削除
        now_color = leader_data[0]
        color[now_color] = color.get(now_color, 1) - leader_data[1]
        color[c] = color.get(c, 1) + leader_data[1]
        # 塗り替え予定の代表元取得
        newcolor_leaders:set = color.get(c)
        # 色を塗り替える
        new_data = [c, leader_data[1], leader_data[2], leader_data[3]]
        new_leader = leader
        if leader_data[2] > 0:
            left = leader_data[2] - 1
            left_leader = dsu.leader(left)
            left_data = data.get(left_leader, [left_leader, 1, left_leader, left_leader])
            if left_data[0] == new_data[0]:
                # 代表元から削除
                left_color = left_data[0]
                color[left_color] = color.get(left_color, 1) - left_data[1]
                color[c] = color.get(c, 1) + left_data[1]
                new_data[2] = left_data[2]
                new_data[1] += left_data[1]
                dsu.merge(leader, left_leader)
                new_leader = dsu.leader(leader)
        if leader_data[3] < N - 1:
            right = leader_data[3] + 1
            right_leader = dsu.leader(right)
            right_data = data.get(right_leader, [right_leader, 1, right_leader, right_leader])
            if right_data[0] == new_data[0]:
                # 代表元から削除
                right_color = right_data[0]
                color[right_color] = color.get(right_color, 1) - right_data[1]
                color[c] = color.get(c, 1) + right_data[1]
                new_data[3] = right_data[3]
                new_data[1] += right_data[1]
                dsu.merge(new_leader, right_leader)
                new_leader = dsu.leader(leader)
        data[new_leader] = new_data
    elif query[0] == 1:
        n, c = query
        result.append(color.get(c, 1))

for r in result:
    print(r)
