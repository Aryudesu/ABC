from itertools import permutations


def calc_cost(N, graphMG, graphMH, nums, cost_data) -> int:
    """
       Gのノード(0, 1, ..., N)に対応する数列nums(P1, P2, ..., PN)に変換する際のコスト計算
       nums: G -> H
    """
    result = 0
    for n in range(N):
        # Gのノード
        i = n
        # Hのノード
        j = nums[n]
        mg_dat = graphMG.get(i, set())
        mh_data = graphMH.get(j, set())
        mg_data = set()
        for dat in mg_dat:
            mg_data.add(nums[dat])
        # MGにあってMHにない辺
        mg_mh = mg_data - mh_data
        # MHにあってMGにない辺
        mh_mg = mh_data - mg_data
        for dat in mg_mh:
            a = min([dat, j])
            b = max([dat, j])
            # print("a b", a, b - a - 1)
            result += cost_data[a][b - a - 1]
        for dat in mh_mg:
            a = min([dat, j])
            b = max([dat, j])
            # print("a b", a, b - a - 1)
            result += cost_data[a][b - a - 1]
    return result


N = int(input())

MG = int(input())
graphMG = dict()
for mg in range(MG):
    u, v = [int(l) - 1 for l in input().split()]
    tmp = graphMG.get(u, set())
    tmp.add(v)
    graphMG[u] = tmp
    tmp = graphMG.get(v, set())
    tmp.add(u)
    graphMG[v] = tmp

MH = int(input())
graphMH = dict()
for mh in range(MH):
    u, v = [int(l) - 1 for l in input().split()]
    tmp = graphMH.get(u, set())
    tmp.add(v)
    graphMH[u] = tmp
    tmp = graphMH.get(v, set())
    tmp.add(u)
    graphMH[v] = tmp

A = []
for n in range(N-1):
    A.append([int(l) for l in input().split()])

# print(graphMG, graphMH, A)

result = 10**10
for index in permutations(range(N)):
    tmp = calc_cost(N, graphMG, graphMH, index, A)
    result = min([result, tmp])
print(result // 2)
