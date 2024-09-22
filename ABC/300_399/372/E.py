from atcoder.dsu import DSU


class DebugIO:
    DEBUG = 0
    RELEASE = 1
    def __init__(self, mode=RELEASE) -> None:
        self.result = []
        self.mode = mode

    def print(self, data) -> None:
        if self.mode == self.DEBUG:
            self.result.append(data)
        elif self.mode == self.RELEASE:
            print(data)

    def debug_print(self) -> None:
        if self.mode == self.DEBUG:
            for r in self.result:
                print(r)


dio = DebugIO(DebugIO.RELEASE)
N, Q = [int(l) for l in input().split()]
dsu = DSU(N + 1)
data = dict()
result = []
for q in range(Q):
    n, u, v = [int(l) for l in input().split()]
    if n == 1:
        ul = dsu.leader(u)
        vl = dsu.leader(v)
        dsu.merge(u, v)
        ml = dsu.leader(u)
        if ul != vl:
            dat_u: list = data.get(ul, [u])
            dat_v: list = data.get(vl, [v])
            tmp = dat_u + dat_v
            data[ml] = sorted(tmp, reverse=True)[:10]
    elif n == 2:
        ul = dsu.leader(u)
        dat_u = data.get(ul, [u])
        if len(dat_u) < v:
            dio.print(-1)
        else:
            dio.print(dat_u[v-1])
dio.debug_print()
