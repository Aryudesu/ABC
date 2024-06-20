import sys

sys.setrecursionlimit(10**6)


N = int(input())
A = [int(l) - 1 for l in input().split()]
# data[ノード] = そこからたどり着けるノードの個数
data = [0] * N
# nodes[ノード] = 現探索時の深さ
nodes = [0] * N

def calc(N, A, idx, depth):
    nodes[idx] = depth
    # 次のノード
    a = A[idx]
    # 自己ループ
    if A[idx] == idx:
        data[idx] = 1
        nodes[idx] = 0
        return depth, None
    # 次のノードがすでに辿り着いたことのあるノードの場合
    if nodes[a] != 0:
        # 辿り着いたことがある中でノードの個数が記録されていない場合
        if data[a] == 0:
            data[a] = depth - nodes[a] + 1
        nodes[idx] = 0
        return depth, a
    tmp, b = calc(N, A, a, depth + 1)
    if not b is None:
        data[idx] = data[b]
    else:
        if data[idx] == 0:
            data[idx] = tmp - depth + 1
    if idx == b:
        b = None
    nodes[idx] = 0
    return tmp, b

result = 0
for idx in range(N):
    if data[idx] == 0:
        nodes[idx] = 1
        tmp1, tmp2 = calc(N, A, idx, 1)
        result += tmp1
    else:
        result += data[idx]
print(result)
