from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.nears = []
        self.sign = -1  # 木の根側のノード
        self.depth = -1  # ノードの深さ

    def __repr__(self):
        return f'Node index:{self.index} nears:{self.nears} sign:{self.sign} depth:{self.depth}'


N = int(input())  # 入力1
TKA = [list(map(int, input().split()))for _ in range(N)]  # 入力2

nodes = []
for i in range(N+1):
    nodes.append(Node(i))  # ノードの作成0~Nで0は使わない

for i in range(1, N+1):
    for j in range(TKA[i-1][1]):
        # nodes[始点].nears.append(終点)　指向性なしなら逆も書く
        nodes[i].nears.append(TKA[i-1][j+2])

queue = deque()
queue.append(nodes[N])  # queue.append(nodes[スタートする点])
nodes[N].depth = 0  # スタートの深さを0にする
while queue:
    node = queue.popleft()  # .pop()にするとdfsになる、bfsは幅優先、dfsは深さ優先
    nears = node.nears
    for near in nears:
        if nodes[near].sign == -1:
            queue.append(nodes[near])
            nodes[near].sign = node.index  # sign格納
            nodes[near].depth = node.depth + 1  # depth格納

# ここ移行は調べたいものを書く
ans = 0
for i in range(1, N):
    if nodes[i].sign != -1:
        ans += TKA[i-1][0]

ans += TKA[N-1][0]

print(ans)
