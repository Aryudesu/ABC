class RestorePartition:
    def __init__(self, N: int, A: list[int], maxSum: int = -1):
        """
        復元可能部分和問題．
        長さNの数列Aのうち解がSになる組み合わせが存在するか確認し，
        するならば復元できるようにする．
        最大maxSum以降は考慮しないようにするが，maxSum <= 0の場合は全組み合わせを考慮する．
        """
        self.N = N
        self.A = A
        self.maxSum = maxSum
        self.data = self._calcPartition()

    def _calcPartition(self) -> dict[int, int|None]:
        """
        事前計算を行います．
        """
        # 値　追加した結果その値になったもの
        parent = {0: None}
        for idx, a in enumerate(self.A):
            new_data = parent.copy()
            for k in parent:
                nxt = k + a
                if self.maxSum > 0 and self.maxSum < nxt:
                    continue
                if not nxt in new_data:
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
        Sになる組み合わせの0-basedであるIndex配列を返却します．
        存在しない場合は空配列を返却します．
        """
        result = []
        if not S in self.data:
            return result
        tmpS = S
        while tmpS > 0:
            prevIdx = self.data[tmpS]
            if prevIdx is None:
                raise RuntimeError("再構築時エラー（逆伝搬時Noneエラー）")
            result.append(prevIdx)
            tmpS -= self.A[prevIdx]
        if tmpS != 0:
            raise RuntimeError("再構築時エラー（逆伝搬の結果0に戻らなかった）")
        result.reverse()
        return result
    
    def makeValues(self, S) -> list[int]:
        """合計がSになる組み合わせを1つ返却します．"""
        dat = self.makeData(S)
        return [self.A[idx] for idx in dat]

# == 競技プログラミングの鉄則B18
N, S = map(int, input().split())
A = [int(l) for l in input().split()]
rp = RestorePartition(N, A, S)
if rp.isExists(S):
    res = rp.makeData(S)
    data = [r + 1 for r in res]
    print(len(data))
    print(*data)
else:
    print(-1)
