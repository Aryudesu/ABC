import bisect


def calc_min_day(N, n, hd):
    if n in hd:
        return 0
    tmp = bisect.bisect_left(hd, n)
    res1 = (hd[tmp] - n) % N
    res2 = (n - hd[tmp-1]) % N
    return res1 if res1 < res2 else res2


N = int(input())
A = [int(l) for l in input().split()]
hd = [0, N]
# なんか起こって奇跡的に通って・・・・・・
# 初期値計算
now_max = 0
for n in range(N):
    x = calc_min_day(N, n, hd)
    if x != 0:
        now_max += A[x-1]
# 2日目から順に考える
for n in range(1, N):
    new_hd = [i for i in hd]
    # n日目に休日を入れた場合
    bisect.insort(new_hd, n)
    t_result = 0
    # 入れた場合の効率計算
    for k in range(N):
        x = calc_min_day(N, k, new_hd)
        if x != 0:
            t_result += A[x-1]
    # 効率が良くなれば更新
    if now_max < t_result:
        now_max = t_result
        hd = new_hd
print(now_max)
