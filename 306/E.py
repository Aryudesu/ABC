import heapq


class Multiset:
    def __init__(self) -> None:
        self.data = []
        self.d = dict()
        self.size = 0

    def insert(self, x):
        heapq.heappush(self.data, x)
        self.size += 1
        if x not in self.d:
            self.d[x] = 1
        else:
            self.d[x] += 1

    def erase(self, x):
        if x not in self.d or self.d[x] == 0:
            raise Exception()
        else:
            self.d[x] -= 1
            self.size -= 1

        while len(self.data) != 0:
            if self.d[self.data[0]] == 0:
                heapq.heappop(self.h)
            else:
                break

        while len(self.data) != 0:
            if self.d[self.data[-1]] == 0:
                heapq.heappop(self.data)
            else:
                break

    def is_exist(self, x):
        return x in self.d and self.d[x] != 0

    def get_size(self):
        return self.size

    def get_min(self):
        return self.data[0]

    def get_max(self):
        return self.data[-1]


N, K, Q = [int(l) for l in input().split()]
data = [0] * N
X = Multiset()
Y = Multiset()
for q in range(Q):
    x, y = [int(l) for l in input().split()]
    Y.insert(y)
    print("max, min", Y.get_max(), Y.get_min())
