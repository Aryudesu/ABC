from collections import defaultdict

from atcoder.dsu import DSU
from atcoder.scc import SCCGraph


def calc(N, S, T):
    data = defaultdict(set)
    str_to_num = dict()
    num = 0
    for n in range(N):
        s = S[n]
        t = T[n]
        if not s in str_to_num:
            str_to_num[s] = num
            num += 1
        if not t in str_to_num:
            str_to_num[t] = num
            num += 1
        data[s].add(t)
    dsu = DSU(num)
    for k in data:
        if len(data[k]) >= 2:
            return -1
    same_data = set()
    result = 0
    g = SCCGraph(num)
    for k in data:
        next = data[k]
        for n in next:
            if k == n:
                continue
            k_num = str_to_num[k]
            n_num = str_to_num[n]
            if dsu.same(k_num, n_num):
                same_data.add((k_num, n_num))
                same_data.add((n_num, k_num))
            dsu.merge(k_num, n_num)
            g.add_edge(k_num, n_num)
            result += 1
    sc = g.scc()
    dsug = dsu.groups()
    # abcdefghijklmnopqrstuvwxyzからbcdefghijklmnopqrstuvwxyzaのような変換は無理
    if len(sc) == len(dsug) and num == 26 and result > 0:
        return -1
    return result + len(same_data)//2



N = int(input())
S = input()
T = input()
print(calc(N, S, T))
