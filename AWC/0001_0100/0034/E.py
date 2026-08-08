N = int(input())
P = list(map(int, input().split()))
W = list(map(int, input().split()))

# data[mask][prev] = 評価値
data = [[None] * N for _ in range(1 << N)]
for i in range(N):
    data[1 << i][i] = 0

for mask in range((1 << N)-1):
    for prev in range(N):
        if data[mask][prev] is None:
            continue
        for nxt in range(N):
            b = 1 << nxt
            if mask & b != 0:
                continue
            value = data[mask][prev]
            nextMask = mask | b
            nextValue = value + abs(P[prev] - P[nxt]) * W[mask.bit_count() - 1]
            if data[nextMask][nxt] is None or data[nextMask][nxt] < nextValue:
                data[nextMask][nxt] = nextValue
print(max(data[-1]))
# 5完できました！　ありがとうございました！！
