import bisect


def setOCData(S: str, ot_count: list, sl_p: list):
    o_c = 0
    t_c = 0
    for idx in range(len(S)):
        s = S[idx]
        if s == "1":
            o_c += 1
        elif s == "2":
            t_c += 1
        elif s == "/":
            sl_p.append(idx)
        ot_count.append([o_c, t_c])

def calc(S, L, R, otc, slp):
    idx_l = bisect.bisect_left(slp, L)
    idx_r = bisect.bisect_right(slp, R)
    if len(slp) <= idx_l:
        return 0
    result = 0
    for idx in range(idx_l, idx_r):
        sp = slp[idx]
        oc = otc[sp][0] - otc[L][0]
        if S[L] == "1":
            oc += 1
        tc = otc[R][1] - otc[sp][1]
        if tc * 2 + 1 <= result:
            break
        result = max([result, min([oc, tc]) * 2 + 1])
    return result


N, Q = [int(l) for l in input().split()]
S = input()
otc, slp = [], []
setOCData(S, otc, slp)
# print(otc, slp)

result = []
for q in range(Q):
    L, R = [int(l) - 1 for l in input().split()]
    result.append(calc(S, L, R, otc, slp))

for r in result:
    print(r)
