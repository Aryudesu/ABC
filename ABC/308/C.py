class Person(object):
    def __init__(self, a, b, num) -> None:
        self.A = a
        self.B = b
        self.N = num

    def __lt__(self, other):
        tmp = self.A*(other.A + other.B) - other.A * (self.A + self.B)
        if tmp == 0:
            return self.N > other.N
        else:
            return tmp < 0

    def getN(self):
        return self.N


N = int(input())
data = []
for n in range(N):
    A, B = [int(l) for l in input().split()]
    data.append(Person(A, B, n + 1))
data.sort(reverse=True)
result = []
for dat in data:
    result.append(dat.getN())
print(*result)
