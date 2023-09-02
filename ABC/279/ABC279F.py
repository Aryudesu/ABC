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
        else:
            self.root[x] += self.root[y]
            self.root[y] = x
            if(self.rank[x] == self.rank[y]):
                self.rank[x] += 1

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


# 呼び出し
N, Q = [int(l) for l in input().split()]
querys = []
# 入るボールの個数
all_ball = N
for q in range(Q):
    que = [int(l) for l in input().split()]
    if que[0] == 2:
        all_ball += 1
    querys.append(que)
ball = N
# 箱に最初に入っているボールを根とする
boxes = {n + 1: n + 1 for n in range(N)}
# ノードのボールがどの箱番号に対応しているか
rev_boxes = dict()
uf = UnionFind(all_ball + 1)
for query in querys:
    # 移し替え
    if query[0] == 1:
        # 箱のノード番号
        x = boxes.get(query[1])
        y = boxes.get(query[2])
        # 移し替え先の箱が空なら
        if x is None:
            # 対象となる箱のノードをそのままノードにする
            x = y
            boxes[query[1]] = y
            rev_boxes[y] = query[1]
        uf.unite(x, y)
        # 移し替えた後はボールがなくなる
        boxes[query[2]] = None
    # 箱にボールを1つ追加
    elif query[0] == 2:
        # ボール番号を進める
        ball += 1
        # 箱の番号を取得する
        box_number = boxes.get(query[1])
        # 箱にボールが入っていない場合
        if box_number is None:
            # 新たに入るボールの番号をノードとする
            boxes[query[1]] = ball
            box_number = ball
            # その箱の
            rev_boxes[box_number] = query[1]
        else:
            uf.unite(ball, box_number)
    elif query[0] == 3:
        # 箱のノード番号
        tmp = boxes.get(query[1])
        # 移し替えていない場合
        if tmp == query[1]:
            res = tmp
        # 移し替えた後の場合
        else:
            tmp = uf.find(query[1])
            temp = rev_boxes.get(tmp)
            if temp is None:
                res = tmp
            else:
                res = temp
        print(res)
# print(boxes)
