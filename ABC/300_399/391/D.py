class BlockData:
    def __init__(self, n, y, x):
        self.n = n
        self.y = y
        self.x = x
        # 消えない場合何段目に積まれるか
        self.xc = None
        # 落ちきるまでの時間
        self.time = None
        self.delete_time = None

    def set_xc_time(self, xc):
        self.xc = xc
        self.time = self.y - xc

    def set_delete_time(self, time):
        self.delete_time = time

    def __lt__(self, other):
        return self.y < other.y

    def __str__(self):
        return f"[n:{self.n}, y:{self.y}, x:{self.x}, xc:{self.xc}, time:{self.time}, delete:{self.delete_time}]"

def set_data(block):
    # ブロックが消えない場合何段目に落ち着くのか
    x_count = [0] * W
    for n in range(N):
        bd = block[n]
        bd.set_xc_time(x_count[bd.x])
        x_count[bd.x] += 1
    return x_count

N, W = [int(l) for l in input().split()]
# ブロック情報取得
block = []
for n in range(N):
    x, y = [int(l) - 1 for l in input().split()]
    bd = BlockData(n, y, x)
    block.append(bd)
# 高さ順に並び替え
block.sort()
x_count = set_data(block)
# 最後に消える高さ
y_max = min(x_count)
# 揃う秒数
y_time = [0] * y_max

for d in block:
    if y_max > d.xc:
        y_time[d.xc] = max([d.time, y_time[d.xc]])

del_y_time = [0] * y_max
for y in range(y_max):
    if y > 0:
        if del_y_time[y-1] >= y_time[y]:
            del_y_time[y] = del_y_time[y-1] + 1
        else:
            del_y_time[y] = y_time[y]
    else:
        del_y_time[y] = y_time[y]

for b in block:
    if b.xc < y_max:
        b.set_delete_time(del_y_time[b.xc])

data = dict()
for b in block:
    if not b.delete_time is None:
        data[b.n] = b.delete_time + 1

# for b in block:
#     print(b)

# print(data)

Q = int(input())
for _ in range(Q):
    t, a = [int(l) for l in input().split()]
    if data.get(a - 1, 10000000000) > t:
        print("Yes")
    else:
        print("No")
