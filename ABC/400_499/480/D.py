from bisect import bisect_left

# 大抵のクラスは以下を使用
# https://github.com/Aryudesu/myLibrary

class PrefixSum:
    """1次元累積和ライブラリ"""
    def __init__(self, arr: list[int]):
        self.pref = [0]
        for x in arr:
            self.pref.append(self.pref[-1] + x)

    def sum(self, l: int, r: int) -> int:
        """[l, r)の累積和を計算します"""
        return self.pref[r] - self.pref[l]

    def allSum(self) -> int:
        """全ての和を計算します"""
        return self.pref[-1]
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            l = 0 if key.start is None else key.start
            r = len(self.pref)-1 if key.stop is None else key.stop
            return self.pref[r] - self.pref[l]
        return self.pref[key]

def calc(idx: int)->int:
    if idx < 0:
        return 0
    index = bisect_left(IDX_DATA, idx)
    baseIdx = 0
    if index > 0:
        baseIdx = IDX_DATA[index - 1]
    result = SUM_DATA[index]
    # print(baseIdx, result)
    if baseIdx == idx:
        return result
    return result - PS[idx - baseIdx: IDX_DATA[index] - baseIdx]
    


N, Q = map(int, input().split())
A = list(map(int, input().split()))
PS = PrefixSum(A)
IDX_DATA = [0]
SUM_DATA = [0]
idx = 0
for n in range(N):
    idx += n + 1
    IDX_DATA.append(idx)
    if len(SUM_DATA) == 0:
        SUM_DATA.append(A[0])
    else:
        SUM_DATA.append(SUM_DATA[-1] + PS[0: n+1])
# print(IDX_DATA)
# print(SUM_DATA)
result = []
for _ in range(Q):
    l, r = map(int, input().split())
    result.append(calc(r) - calc(l-1))
print(*result, sep="\n")
