from typing import Tuple

class RollingHash:
    """
    ダブルローリングハッシュライブラリ
    Edited by Aryu
    """
    def __init__(self, S: str|list[int], base1=37, MOD1=10**9 + 9, base2=157, MOD2 = 10**9 + 7):
        self.base1 = base1
        self.MOD1 = MOD1
        self.base2 = base2
        self.MOD2 = MOD2
        # 元データ
        self.N = len(S)
        # ハッシュ計算
        self.hash1 = []
        self.powData1 = []

        self.hash2 = []
        self.powData2 = []
        if isinstance(S, str):
            vals = [ord(c) for c in S]
        else:
            vals = list(S)
        self.powData1 = [1] * (self.N + 1)
        self.hash1 = [0] * (self.N + 1)

        self.powData2 = [1] * (self.N + 1)
        self.hash2 = [0] * (self.N + 1)
        for i in range(self.N):
            self.powData1[i+1] = (self.powData1[i] * self.base1) % self.MOD1
            self.hash1[i+1] = (self.hash1[i] * self.base1 + vals[i]) % self.MOD1
            self.powData2[i+1] = (self.powData2[i] * self.base2) % self.MOD2
            self.hash2[i+1] = (self.hash2[i] * self.base2 + vals[i]) % self.MOD2
    
    def get(self, l: int, r: int)-> Tuple[int, int]:
        """[l, r)のハッシュ値を2つ返却"""
        assert 0 <= l <= r <= self.N
        res1 = self.hash1[r] - self.hash1[l] * self.powData1[r-l]
        res2 = self.hash2[r] - self.hash2[l] * self.powData2[r-l]
        return (res1 % self.MOD1, res2 % self.MOD2)

    def hashAll(self) -> Tuple[int, int]:
        """全体のハッシュ"""
        return (self.hash1[-1], self.hash2[-1])
    
    def find(self, pattern: "RollingHash")->int:
        """最初に出現する位置の探索を行います．"""
        if len(self) < len(pattern) or len(pattern) == 0:
            return -1
        target = pattern.hashAll()
        for idx in range(len(self) - len(pattern) + 1):
            if self.get(idx, idx + len(pattern)) == target:
                return idx
        return -1
    
    def findAll(self, pattern: "RollingHash")->list[int]:
        """出現する位置の探索を行います．"""
        if len(self) < len(pattern) or len(pattern) == 0:
            return []
        result = []
        target = pattern.hashAll()
        for idx in range(len(self) - len(pattern) + 1):
            if self.get(idx, idx + len(pattern)) == target:
                result.append(idx)
        return result
    
    def lcp(self, other: "RollingHash")->int:
        """最長共通接頭辞の長さを返却します．"""
        l = 0
        r = min(len(self), len(other)) + 1
        while r - l > 1:
            mid = (r + l) // 2
            if self.get(0, mid) == other.get(0, mid):
                l = mid
            else:
                r = mid
        return l

    def contains(self, pattern: "RollingHash")->bool:
        """包括確認を行います．"""
        return self.find(pattern) != -1
    
    def __contains__(self, pattern: "RollingHash")->bool:
        """包括確認を行います．"""
        return self.contains(pattern)

    def __len__(self):
        """代入された文字列長を返却します．"""
        return self.N


from collections import deque
from typing import Any, Tuple

class RunLength:
    """
    ランレングス符号クラス
    Edited by Aryu
    """
    def __init__(self, data: list[Any]|str|None = None) -> None:
        self.data: deque[Tuple[Any, int]] = deque()
        self.size = 0
        if data is None:
            return
        if len(data) == 0:
            return
        prev = data[0]
        cnt = 0
        for dat in data:
            if dat == prev:
                cnt += 1
            else:
                self.data.append((prev, cnt))
                cnt = 1
            prev = dat
        self.data.append((prev, cnt))
        self.size = len(data)

    def appendRight(self, x: Any, n: int)->None:
        """右からxをa個追加"""
        if self.data and self.data[-1][0] == x:
            v, c = self.data[-1]
            self.data[-1] = (v, c + n)
        else:
            self.data.append((x, n))
        self.size += n
    
    def appendLeft(self, x: Any, n: int)->None:
        """左からxをa個追加"""
        if self.data and self.data[0][0] == x:
            v, c = self.data[0]
            self.data[0] = (v, c + n)
        else:
            self.data.appendleft((x, n))
        self.size += n

    def popRight(self, n: int)->list[Tuple[Any, int]]:
        """右側からn個取得．個数が不足している場合は全て取得．"""
        if n == 0 or self.size == 0:
            return []
        num = min(n, self.size)
        result: list[Tuple[Any, int]] = []
        self.size -= num
        while num > 0:
            v, c = self.data[-1]
            if c > num:
                self.data[-1] = (v, c - num)
                result.append((v, num))
            else:
                result.append(self.data.pop())
            num -= c
        return result

    def popLeft(self, n: int)->list[Tuple[Any, int]]:
        """左側からデータをn個取得"""
        if n == 0 or self.size == 0:
            return []
        num = min(n, self.size)
        result: list[Tuple[Any, int]] = []
        self.size -= num
        while num > 0:
            v, c = self.data[0]
            if c > num:
                self.data[0] = (v, c - num)
                result.append((v, num))
            else:
                result.append(self.data.popleft())
            num -= c
        return result

    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return self.size
    
    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return f"RunLength({self.data}, size={self.size})"


def calc(M: int, rl: RunLength)->int:
    if len(rl.data) == 0:
        return 0
    if len(rl.data) == 1:
        dat = rl.data.pop()
        if not dat[0]:
            return 0
        if dat[1] == M + 1:
            return dat[1]
        if dat[1] > M:
            return M
        return dat[1]
    result = 0
    cNum = 0
    if rl.data:
        edge = rl.data.pop()
        if edge[0]:
            if cNum + edge[1] > M:
                return M
            else:
                result += edge[1]
                cNum += edge[1]
    if rl.data:
        edge = rl.data.popleft()
        if edge[0]:
            if cNum + edge[1] > M:
                return M
            else:
                result += edge[1]
                cNum += edge[1]
    nums = []
    for dat in rl:
        if dat[0]:
            nums.append(dat[1])
    nums.sort()
    while nums:
        num = nums.pop()
        c = min(M-cNum, num + 1)
        result += c - 1
        cNum += c
        if cNum >= M:
            break
    return result


N, M = map(int, input().split())
S = input()
T = "ATCODER"
L = len(T)
sHash = RollingHash(S)
targetHash = RollingHash(T)
rl = RunLength()
n = 0
while n < N:
    if n + L <= N and sHash.get(n , n + L) == targetHash.hashAll():
        rl.appendRight(True, 1)
        n += len(T)-1
    else:
        rl.appendRight(False, 1)
    n += 1
res = calc(M, rl)
print(res)
