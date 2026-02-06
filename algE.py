class RunLength:
    """
    ランレングス符号クラス
    Edited by Aryu
    """
    def __init__(self) -> None:
        self.data = []
        self.pointer = 0

    def insert(self, x, n):
        """xをa個追加"""
        if len(self.data):
            if self.data[-1][0] == x:
                self.data[-1][1] += n
            else:
                self.data.append([x, n])
        else:
            self.data.append([x, n])

    def popData(self, n):
        """末尾からn個取得"""
        tmpN = n
        result = []
        while True:
            if self.data[-1][1] > tmpN:
                self.data[-1][1] -= tmpN
                result.append([self.data[-1][0], tmpN])
                return result
            elif self.data[-1][1] == tmpN:
                result.append([self.data[-1][0], tmpN])
                self.data.pop()
                return result
            else:
                tmpN -= self.data[-1][1]
                result.append([self.data[-1][0], self.data[-1][1]])
                self.data.pop()
        return result

    def deque(self, n):
        """先頭からデータをn個取得"""
        tmpN = n
        result = []
        while True:
            pointer = self.pointer
            if len(self.data) <= pointer:
                break
            if self.data[pointer][1] > tmpN:
                self.data[pointer][1] -= tmpN
                result.append([self.data[pointer][0], tmpN])
                return result
            elif self.data[pointer][1] == tmpN:
                result.append([self.data[pointer][0], self.data[pointer][1]])
                self.pointer += 1
                return result
            else:
                tmpN -= self.data[pointer][1]
                result.append([self.data[pointer][0], self.data[pointer][1]])
                self.pointer += 1
        return result

    def show(self):
        """デバッグ用表示"""
        print(self.data)
        print(self.pointer)


rl = RunLength()
S = input()
for s in S:
    rl.insert(s, 1)
result = []
for k, n in rl.data:
    result.append(str(k))
    result.append(str(n))
print(" ".join(result))
