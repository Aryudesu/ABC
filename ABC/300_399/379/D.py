from heapq import heappop, heappush

class HomeGarden:
    def __init__(self):
        self.data = []
        self.base = 0

    def addVal(self):
        heappush(self.data, self.base)
    
    def addAll(self, x: int):
        self.base += x
    
    def countGt(self, x: int):
        result = 0
        while self.data:
            h = self.base - heappop(self.data)
            if h < x:
                heappush(self.data, self.base - h)
                break
            result += 1
        return result

Q = int(input())
hg = HomeGarden()
result = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        hg.addVal()
    elif query[0] == 2:
        T = query[1]
        hg.addAll(T)
    elif query[0] == 3:
        H = query[1]
        res = hg.countGt(H)
        result.append(res)
    else:
        raise Exception()

for r in result:
    print(r)
