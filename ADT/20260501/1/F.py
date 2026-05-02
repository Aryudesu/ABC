from collections import deque, defaultdict
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

def calc(XYS: list[Tuple[int, int, str]])->bool:
    data = defaultdict(RunLength)
    for y, x, s in XYS:
        data[y].appendRight(s, 1)
    for y, dat in data.items():
        if len(dat.data) > 2:
            return True
        if len(dat.data) == 1:
            continue
        sec = dat.popRight(1)
        if sec[0][0] == "L":
            return True
    return False


N = int(input())
XY = []
for n in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
S = input()
XYS = []
for n in range(N):
    x, y = XY[n]
    s = S[n]
    XYS.append((y, x, s))
XYS.sort()
print("Yes" if calc(XYS) else "No")
