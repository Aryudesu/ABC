N, X, Y = [int(l) for l in input().split()]
PT = []
for n in range(N - 1):
    PT.append([int(l) for l in input().split()])

data = []
# 時刻表作成
# 3 * 5 * 7 * 8 = 840周期のはず（しらんけど）
for t in range(840):
    tm = t
    for pt in PT:
        p, tt = pt
        if tm % p:
            tm += p - (tm % p)
        tm += tt
    tm -= t
    data.append(tm)

result = []
Q = int(input())
for q in range(Q):
    qq = int(input())
    result.append(qq + X + data[(qq + X) % 840] + Y)
for r in result:
    print(r)
