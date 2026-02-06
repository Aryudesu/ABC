def np_solve(N, W, pv):
    pass

N, M = map(int, input().split())
# data[値段] = 最大価値
data = set()
for i in range(N):
    data.add((i+1, 0))
for n in range(N):
    nextData = data.copy()
    p, v = map(int, input().split())
    for d, c in data:
        pass
