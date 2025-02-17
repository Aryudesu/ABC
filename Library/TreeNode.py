from __future__ import annotations


class DigraphTreeNode:
    """
    向き付き木構造のノードについてのクラス

    Parameters
    ----------
    n : int
        ノード番号
    data : object
        ノードに乗せるデータ
    next : list[int]
        隣接するノード
    """
    def __init__(self, n: int = None):
        """
        ノードの作成を行います

        Parameters
        ----------
        n : int = None
            ノード番号
        """
        self.n: int = n
        self.data: object = None
        self.next: list[DigraphTreeNode] = []

    def add_node(self, tn: DigraphTreeNode):
        """
        ノードの追加を行います

        Parameters
        ----------
        tn: DigraphTreeNode
            隣接する木構造
        """
        self.next.append(tn)

    def set_data(self, data):
        """
        データを設定します

        Parameters
        ----------
        data: object
            ノードに設定するデータ
        """
        self.data = data

# === ABC391E ===

def make_graph(N, A):
    if N == 0:
        tn = DigraphTreeNode()
        tn.set_data(int(A))
        return tn
    tmp = DigraphTreeNode()
    dt = [0, 0]
    for i in range(3):
        B = A[3**(N-1) * i: 3**(N-1) * (i+1)]
        d = make_graph(N - 1, B)
        tmp.add_node(d)
        dt[d.data] += 1
    tmp.set_data(1 if dt[0] < dt[1] else 0)
    return tmp

def calc(N: int, tn: DigraphTreeNode, num: int):
    if N == 0:
        # 同じであればそれを変える必要がある
        return 1 if num == tn.data else 0
    res = 0
    count = 0
    dat = []
    for i in range(3):
        if tn.next[i].data == num:
            tmp = calc(N-1, tn.next[i], num)
            count += 1
            dat.append(tmp)
    if count == 2:
        res = min(dat)
    elif count == 3:
        res = sum(dat) - max(dat)
    return res

N = int(input())
A = input()
tree = make_graph(N, A)
result = calc(N, tree, tree.data)
print(result)
