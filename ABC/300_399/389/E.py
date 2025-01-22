from sortedcontainers import SortedList


# 個数考える (元値, 対象となる値, 取れる最大値)
def binary_search(p, target, sup):
    t = min([target, sup])
    ok, ng = 0, t * 2
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        price = p * (mid * 2 - 1)
        if price <= t:
            ok = mid
        else:
            ng = mid
    return ng


N, M = [int(l) for l in input().split()]
# 値段, 元値, 買った個数
P = SortedList([tuple([int(l), int(l), 0]) for l in input().split()])
money = 0
count = 0
while money <= M:
    # 一番安いものを取得
    p, m, n = P.pop(0)
    tn = binary_search(m, P[0][0], max([M - money, 0]))
    if tn == n:
        break
    money += m * (tn ** 2) - m * (n ** 2)
    P.add(tuple([m * (2 * tn + 1), m, tn]))
    count += tn - n
if money > M:
    count -= 1
print(count)
