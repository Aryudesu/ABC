from collections import defaultdict
from functools import cmp_to_key
import bisect


class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


class manhattanMST():
    def __init__(self, points, inf=10**10):
        """
        Parameters
        ---------------------
        points: [(x, y), ...]
        """
        self.points = points
        self.inf = inf
        edges = []
        n = len(points)
        ids = [0 for _ in range(n)]
        for ph in range(4):
            ids.sort(key=cmp_to_key(self.comp))
            xv_s = set()
            for ps in points:
                xv_s.add(ps[0])
            xv = list(xv_s)
            xv.sort()
            fen = [(-self.inf, -1) for _ in range(n)]
            for id in ids:
                xi = int(self.lower(xv, ps[id][0]) - xv[0])
                ma = (-inf, -1)
                ma = self.ma_calc(xi, ma, fen)
                if ma[1] != -1:
                    edges.append((id, ma[1]))

    def ma_calc(xi, ma, fen):
        i = xi + 1
        while i > 0:
            if ma[0] <= fen[i-1][0]:
                ma = fen[i-1]
            i -= i & -i
        return ma

    def lower(a, num):
        idx = bisect.bisect_left(a, num)
        return a[idx]

    def comp(x, y):
        """ソート用比較関数"""
        ixy = x[0] + x[1]
        jxy = y[0] + y[1]
        tmpx = (ixy, x[1])
        tmpy = (jxy, y[1])
        if tmpx == tmpy:
            return 0
        elif tmpx > tmpy:
            return -1
        else:
            return 1

    def calc():
        pass


# # 呼び出し
# n = 5
# uf = UnionFind(n)
# uf.unite(1, 2)
# uf.unite(4, 3)
# uf.unite(4, 5)

# uf.find(1)
# uf.find(4)

# uf.same(1, 2)
# uf.same(1, 3)
