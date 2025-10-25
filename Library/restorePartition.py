class RestorePartition:
    def __init__(self, N: int, A: list[int]):
        """
        復元可能部分和問題．
        長さNの数列Aのうち解がSになる組み合わせが存在するか確認し，
        するならば復元できるようにする．
        """
        self.N = N
        self.A = A
        self.data = self._calcPartition()

    def _calcPartition(self) -> dict[int, int|None]|None:
        """
        事前計算を行います．
        """
        # 値　追加した結果その値になったもの
        parent = {0: None}
        for idx, a in enumerate(self.A):
            new_data = parent.copy()
            for k in parent:
                next = k + a
                if not next in new_data:
                    new_data[k + a] = idx
            parent = new_data
        return parent
    
    def isExists(self, S: int) -> bool:
        """
        Sとなる組み合わせが存在するか調べる
        """
        return S in self.data

    def makeData(self, S: int) -> list[int]:
        """
        Sになる組み合わせのIndex配列を返却します．
        存在しない場合は空配列を返却します．
        """
        result = []
        if not S in self.data:
            return result
        tmpS = S
        while tmpS > 0:
            prevIdx = self.data[tmpS]
            result.append(prevIdx)
            tmpS -= self.A[prevIdx]
        if tmpS < 0:
            raise Exception()
        result.reverse()
        return result

N, S = map(int, input().split())
A = [int(l) for l in input().split()]
rp = RestorePartition(N, A)
if rp.isExists(S):
    res = rp.makeData(S)
    data = [r + 1 for r in res]
    print(len(data))
    print(*data)
else:
    print(-1)
