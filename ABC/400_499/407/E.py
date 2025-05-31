import sys

import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(10**6)


DATA = []
MEMO = dict()
def calc(idx, a, s):
    tmp = (idx, a)
    if tmp in MEMO:
        r, s2 = MEMO[tmp]
        return r - s2 + s
    if idx == len(DATA) and a == 0:
        return s
    elif idx == len(DATA):
        return 0
    # idx: 今見ているインデックス
    # a: (のスタック数
    # data: Aのデータ
    # s: それまでの総和
    res = 0
    # (を追加して大丈夫なら追加したパターンを考える
    if len(DATA) - idx - 1 >= a:
        res = max(res, calc(idx + 1, a + 1, s + DATA[idx]))
    # )を追加して大丈夫なら追加したパターンを考える
    if a - 1 >= 0:
        res = max(res, calc(idx + 1, a - 1, s))
    MEMO[(idx, a)] = (res, s)
    return res

T = int(input())
result = []
for t in range(T):
    DATA = []
    N = int(input())
    MEMO = dict()
    for n in range(2 * N):
        DATA.append(int(input()))
    res = calc(0, 0, 0)
    result.append(res)
for r in result:
    print(r)
