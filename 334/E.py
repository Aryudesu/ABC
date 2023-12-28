import math
from collections import defaultdict


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
            self.rank[x] += self.rank[y]
            self.root[y] = x
        else:
            self.rank[y] += self.rank[x]
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


def calcXYtoNum(x, y, w):
    return y * w + x


def inverseMod(num, MOD):
    return pow(num, MOD-2, MOD)



# 呼び出し
MOD = 998244353
H, W = [int(l) for l in input().split()]
N = H * W
S = []
for h in range(H):
    S.append(input())
uf = UnionFind(H * W - 1)
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            continue
        n1 = calcXYtoNum(w, h, W)
        if w > 0:
            if S[h][w - 1] == "#":
                n2 = calcXYtoNum(w - 1, h, W)
                uf.unite(n1, n2)
        if w + 1 < W:
            if S[h][w + 1] == "#":
                n2 = calcXYtoNum(w + 1, h, W)
                uf.unite(n1, n2)
        if h > 0:
            if S[h - 1][w] == "#":
                n2 = calcXYtoNum(w, h - 1, W)
                uf.unite(n1, n2)
        if h + 1 < H:
            if S[h + 1][w] == "#":
                n2 = calcXYtoNum(w, h + 1, W)
                uf.unite(n1, n2)

greenIslands = set()
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            n1 = calcXYtoNum(w, h, W)
            tmp = uf.find(n1)
            greenIslands.add(tmp)
GNum = len(greenIslands)
denom = 0
mole = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == "#":
            continue
        denom += 1
        islandPatterns = set()
        n1 = calcXYtoNum(w, h, W)
        if w > 0:
            if S[h][w - 1] == "#":
                n2 = calcXYtoNum(w - 1, h, W)
                islandPatterns.add(uf.find(n2))
        if w + 1 < W:
            if S[h][w + 1] == "#":
                n2 = calcXYtoNum(w + 1, h, W)
                islandPatterns.add(uf.find(n2))
        if h > 0:
            if S[h - 1][w] == "#":
                n2 = calcXYtoNum(w, h - 1, W)
                islandPatterns.add(uf.find(n2))
        if h + 1 < H:
            if S[h + 1][w] == "#":
                n2 = calcXYtoNum(w, h + 1, W)
                islandPatterns.add(uf.find(n2))
        mole += GNum - len(islandPatterns) + 1
g = math.gcd(mole, denom)
mole = mole//g
denom = denom//g
print((mole * inverseMod(denom, MOD)) % MOD)
