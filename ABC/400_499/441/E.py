from collections import defaultdict
class arrayUtility:
    """配列で便利な機能等まとめたい"""
    def __init__(self, a: list = []):
        self.data = a

    def append(self, d):
        self.data.append(d)

    def inversion(self):
        """転倒数の計算"""
        if not self.data:
            return 0
        tmp = sorted(self.data)
        num = {tmp[i]: i + 1 for i in range(len(tmp))}
        compressed = [num[val] for val in self.data]
        n = len(compressed)
        bit = [0] * (n + 1)
        inv_count = 0
        def add(index, value):
            while index <= n:
                bit[index] += value
                index += index & -index
        def sum(index):
            s = 0
            while index > 0:
                s += bit[index]
                index -= index & -index
            return s
        for i in range(n - 1, -1, -1):
            inv_count += sum(compressed[i] - 1)
            add(compressed[i], 1)
        return inv_count

def prefix_sum(data):
    """累積和"""
    result = []
    s = 0
    for i in range(len(data)):
        s += data[i]
        result.append(s)
    return result

N = int(input())
S = input()
data = [0]
for s in S:
    if s == "A":
        data.append(-1)
    elif s == "B":
        data.append(+1)
    elif s == "C":
        data.append(0)
    else:
        raise Exception()
ps = prefix_sum(data)
au = arrayUtility(ps)
print(au.inversion())
# print(ps)
