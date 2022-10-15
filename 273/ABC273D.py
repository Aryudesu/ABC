import bisect


def get_block_w(R, r, c, l, W, left=True):
    b_list = R.get(r, [])
    if left:
        idx = bisect.bisect_left(b_list, c)
    else:
        idx = bisect.bisect_right(b_list, c)
    if idx >= len(b_list):
        return W - 1
    if left:
        if b_list[idx] < c - l:
            return c - l
        if b_list[idx] > c:
            if c - l < 0:
                return 0
            return c - l
        return b_list[idx] + 1
    else:
        if b_list[idx] > c + l:
            return c + l
        if b_list[idx] < c:
            if c + l >= W:
                return W - 1
            else:
                return c + l
        return b_list[idx] - 1


def get_block_h(C, r, c, l, H, up=True):
    b_list = C.get(c, [])
    if up:
        idx = bisect.bisect_left(b_list, r)
    else:
        idx = bisect.bisect_right(b_list, r)
    if idx >= len(b_list):
        return H - 1
    if up:
        if b_list[idx] < r - l:
            return r - l
        if b_list[idx] > r - l:
            if r - l < 0:
                return 0
            return r - l
        return b_list[idx] + 1
    else:
        if b_list[idx] > r + l:
            return r + l
        if b_list[idx] < r + l:
            if r + l >= H:
                return H - 1
            return r + l
        return b_list[idx] - 1


H, W, rs, cs = [int(l) for l in input().split()]
rs -= 1
cs -= 1
R = dict()
C = dict()
N = int(input())
for n in range(N):
    r, c = [int(l) for l in input().split()]
    r -= 1
    c -= 1
    tmpr = R.get(r, [])
    bisect.insort_left(tmpr, c)
    R[r] = tmpr
    tmpc = C.get(c, [])
    bisect.insort_left(tmpc, r)
    C[c] = tmpc
print(R)
print(C)
Q = int(input())
res = []
for q in range(Q):
    D, L = [l for l in input().split()]
    if D == 'U':
        rs = get_block_h(C, rs, cs, int(L), H, True)
    elif D == 'D':
        rs = get_block_h(C, rs, cs, int(L), H, False)
    elif D == 'L':
        cs = get_block_w(R, rs, cs, int(L), W, True)
    elif D == 'R':
        cs = get_block_w(R, rs, cs, int(L), W, False)
    res.append([rs + 1, cs + 1])
for r in res:
    print(*r)
