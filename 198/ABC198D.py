import itertools
"""
ATCODER ABC198のD問題用に修正したもの
"""


def str2num(S, SD, TPL):
    res = 0
    for s in S:
        res = res * 10 + TPL[SD[s]]
    return res


def is_unsatis(un_zeros, sd, tpl):
    for uz in un_zeros:
        if tpl[sd[uz]] == 0:
            return True
    return False


def input_data(N):
    data = []
    un_zeros_set = set()
    chset = set()
    for n in range(N+1):
        S = input()
        un_zeros_set.add(S[0])
        chset.update(list(S))
        data.append(S)
    chlist = list(chset)
    chd = dict()
    un_zeros = list(un_zeros_set)
    chl = len(chlist)
    for idx in range(chl):
        chd[chlist[idx]] = idx
    return data, chl, chd, un_zeros


def calc(data, chl, chd, un_zeros):
    # ぶん回す
    for itr in itertools.permutations(nums, chl):
        if is_unsatis(un_zeros, chd, itr):
            continue
        numl = []
        for dat in data:
            numl.append(str2num(dat, chd, itr))
        res = 0
        for n in range(N):
            res += numl[n]
        if res == numl[-1]:
            return numl
    return None


N = 2
nums = [l for l in range(10)]
data, chl, chd, un_zeros = input_data(N)

if chl > 10:
    print("UNSOLVABLE")
else:
    numl = calc(data, chl, chd, un_zeros)
    if numl is None:
        print("UNSOLVABLE")
    else:
        for n in numl:
            print(n)
