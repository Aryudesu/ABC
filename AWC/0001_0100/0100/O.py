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

def calc(l: int, r: int, ps: PrefixSum)->int:
    if r - l == 1:
        return 0
    originalSum = ps[l:r]
    prefMin = 10 ** 18
    bestIdx = 0
    for idx in range(l, r):
        s1 = ps[l: idx+1]
        s2 = originalSum - s1
        if abs(s1 - s2) < prefMin:
            prefMin = abs(s1 - s2)
            bestIdx = idx
        else:
            break
    result = originalSum
    result += calc(l, bestIdx+1, ps) + calc(bestIdx+1, r, ps)
    return result

N = int(input())
A = list(map(int, input().split()))
ps = PrefixSum(A)
res = calc(0, N, ps)
print(res)
