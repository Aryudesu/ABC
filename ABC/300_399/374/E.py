def is_cost_ok(a, p, b, q, num, w, cost):
    tmp_w = w - num * a
    c = num * p
    if tmp_w <= 0:
        if c <= cost:
            return True
        else:
            return False
    if tmp_w % b:
        ()


def calc_cost(a, p, b, q, cost, max_cost):
    ok = -1
    ng = max_cost + 1
    while abs(ok - ng) > 1:
        pass

def is_ok(APBQ, mid, X):
    cost_total = 0
    for a, p, b, q in APBQ:
        tmp1 = mid // a
        tmp_cost1 = tmp1 * p
        if tmp1 * a < mid:
            if tmp1 * a + b >= mid:
                tmp_cost1 += min([p, q])
            else:
                tmp_cost1 += p
        tmp2 = mid // b
        tmp_cost2 = tmp2 * q
        if tmp2 * b < mid:
            if tmp2 * b + a >= mid:
                tmp_cost2 += min([p, q])
            else:
                tmp_cost2 += q
        cost_total += min([tmp_cost1, tmp_cost2])
        if cost_total > X:
            return False
    return True


def binary_search(N, X, APBQ, maxW):
    ok = -1
    ng = maxW + 1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(APBQ, mid, X):
            ok = mid
        else:
            ng = mid
    return ok


N, X = [int(l) for l in input().split()]
APBQ = []
maxW = 10**10
for n in range(N):
    A, P, B, Q = [int(l) for l in input().split()]
    APBQ.append([A, P, B, Q])
print(binary_search(N, X, APBQ, maxW))

