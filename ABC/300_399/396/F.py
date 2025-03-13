from sortedcontainers import SortedSet


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

N, M = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
bit = Bit(max(A)+1)
# もともとの転倒数
origin = 0
for i, a in enumerate(A):
    origin += i - bit.sum(a+1)
    bit.add(a, 1)

data = SortedSet()
for idx in range(N):
    a = A[idx]
    tmp = M - A[idx]
    data.add((tmp, idx))
# print(data)
result = []
for m in range(M):
    while True:
        if len(data) == 0:
            break
        num, idx = data.pop(0)
        if num > m:
            data.add((num, idx))
            break
        else:
            origin = origin - (N - idx - 1) + idx
    result.append(origin)
    # print(origin, data)
for r in result:
    print(r)
