class Manhattan:
    def __init__(self):
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        self.data = []

    def add_point(self, y, x):
        self.data.append([y, x])
        new_x = x + y
        new_y = x - y
        if not self.min_x is None:
            self.min_x = min(self.min_x, new_x)
        if not self.max_x is None:
            self.max_x = max(self.max_x, new_x)
        if not self.min_y is None:
            self.min_y = min(self.min_y, new_y)
        if not self.max_y is None:
            self.max_y = max(self.max_y, new_y)
        if self.min_x is None:
            self.min_x = new_x
        if self.max_x is None:
            self.max_x = new_x
        if self.min_y is None:
            self.min_y = new_y
        if self.max_y is None:
            self.max_y = new_y

    def get_point(self, a):
        return self.data[a]

    def get_max_dist(self, y, x):
        u = x + y
        v = x - y
        return max(abs(u-self.max_x), abs(u-self.min_x), abs(v-self.max_y), abs(v-self.min_y))

N, Q = [int(l) for l in input().split()]
mht = Manhattan()
PData = []
for n in range(N):
    x, y = [int(l) for l in input().split()]
    mht.add_point(y, x)

result = []
for _ in range(Q):
    q = int(input()) - 1
    x, y = mht.get_point(q)
    result.append(mht.get_max_dist(y, x))

for r in result:
    print(r)
