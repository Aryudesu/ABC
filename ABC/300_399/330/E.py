from sortedcontainers import SortedSet


class SectionMex:
    # lの一覧
    indexData = SortedSet()
    # 区間 [L, R)
    sectionData = dict()
    def __init__(self):
        pass

    # 値を挿入
    def insert(self, x):
        idx = self.getLt(x)
        # print("===")
        # self.print()
        tmpR = x + 1
        if idx is None:
            self.indexData.add(x)
            self.sectionData[x] = x + 1
        else:
            L = self.indexData[idx]
            # 無効なインデックス
            if x < L:
                self.indexData.add(x)
                # x + 1に区間が設定されて無い場合
                if self.sectionData.get(x + 1) is None:
                    self.sectionData[x] = x + 1
            else:
                R = self.sectionData.get(L)
                if x == R:
                    self.sectionData[L] = x + 1
                elif x > R:
                    self.indexData.add(x)
                    self.sectionData[x] = x + 1
            # x + 1に区間が設定されている場合
            if not self.sectionData.get(x + 1) is None:
                self.sectionData[x] = self.sectionData[x + 1]
                tmpR = self.sectionData[x + 1]
                self.sectionData[x + 1] = None
                self.indexData.remove(x + 1)
            # 左側の連結について
            idx = self.getLt(x)
            # self.print()
            # print("idx", idx)
            if idx > 0:
                L = self.indexData[idx - 1]
                R = self.sectionData.get(L)
                if x == R:
                    self.sectionData[L] = tmpR
                    if not self.sectionData.get(x) is None:
                        self.sectionData[x] = None
                        self.indexData.remove(x)
            # self.print()

    # 要素削除
    def delete(self, x):
        idx = self.getLt(x)
        L = self.indexData[idx]
        if x < L:
            L = self.indexData[idx - 1]
        # print("x, L", x, L)
        R = self.sectionData.get(L)
        self.sectionData[L] = x
        self.sectionData[x + 1] = R

    # x以下の最大のLのインデックスを取得
    def getLt(self, x):
        if len(self.indexData) == 0:
            return None
        # x未満の要素の個数
        idx = self.indexData.bisect_left(x)
        if len(self.indexData) > idx:
            if self.indexData[idx] == x:
                return idx
            elif self.indexData[idx] > x:
                return idx
            return idx - 1
        return len(self.indexData) - 1

    # x以上の最小のインデックスの取得
    def getRt(self, x):
        if len(self.indexData) == 0:
            return None
        idx = self.indexData.bisect_right(x)
        if idx == 0:
            return 0
        if len(self.indexData) > idx:
            pass

    # MEXの取得
    def getMEX(self):
        # print("MEX")
        # self.print()
        tmp = self.sectionData.get(0)
        if tmp is None:
            return 0
        return tmp

    # 配列セット
    def setArray(self, A):
        for a in A:
            self.insert(a)

    # データ出力（デバッグ用）
    def print(self):
        print(self.indexData, self.sectionData)


N, Q = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
numData = dict()
result = []
S = SectionMex()
S.setArray(A)

# indexメモ
for i in range(N):
    numData[A[i]] = numData.get(A[i], 0) + 1

for q in range(Q):
    i, x = [int(l) for l in input().split()]
    idx = i - 1
    prevData = A[idx]
    num = numData.get(prevData) - 1
    if num == 0:
        S.delete(prevData)
    S.insert(x)
    A[idx] = x
    numData[prevData] = numData.get(prevData, 0) - 1
    numData[x] = numData.get(x, 0) + 1
    result.append(S.getMEX())

for r in result:
    print(r)

