from collections import defaultdict


class UnionFind():
    """Union Find木クラス"""

    def __init__(self, n):
        """初期化"""
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """ノードxの根を見つける"""
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite_root(self, x, y):
        """グループの統合を行いグループの統合先と統合元を返却する"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return x, x
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
            return x, y
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            return y, x

    def unite(self, x, y):
        """木の併合"""
        self.unite_root(x, y)

    def multi_unite(self, xy):
        """複数併合"""
        for dat in xy:
            self.unite(dat[0], dat[1])

    def unite_same(self, x, y):
        """同じグループに属するか判定を行い，属さなければ統合"""
        a, b = self.unite_root(x, y)
        return a == b

    def same(self, x, y):
        """同じグループに属するか判定"""
        return self.find(x) == self.find(y)

    def size(self, x):
        """木のサイズを計算"""
        return -self.root[self.find(x)]

    def roots(self):
        """根のノードを取得"""
        return [i for i, x in enumerate(self.root) if x < 0 and i > 0]

    def max_tree_size(self):
        """最大の木のサイズを取得"""
        return max([self.size(r) for r in self.roots()])

    def group_size(self):
        """グループ数を取得"""
        return len(self.roots())

    def group_members(self):
        """全てのグループごとのノードを取得"""
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


# 呼び出し
N, M = [int(l) for l in input().split()]
uf = UnionFind(N)
uf.multi_unite([[int(l) for l in input().split()] for _ in range(M)])
print(uf.group_size() - 1)
