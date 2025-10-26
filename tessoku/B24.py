import sys
import bisect

input = sys.stdin.readline

N = int(input())
boxes = []
for _ in range(N):
    x, y = map(int, input().split())
    boxes.append((x, y))

# (x昇順, xが同じならy降順) でソート
boxes.sort(key=lambda p: (p[0], -p[1]))

# y だけ取り出す
ys = [y for _, y in boxes]

# ys の「厳密昇順」LIS長を O(N log N) で求める
tails = []
for val in ys:
    # val を入れられる位置を探す
    # 厳密増加にしたいので、同じ値は上書き側に入れる
    # → bisect_leftでOK
    pos = bisect.bisect_left(tails, val)
    if pos == len(tails):
        tails.append(val)
    else:
        tails[pos] = val

print(len(tails))