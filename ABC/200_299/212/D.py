from heapq import heappop, heappush

class QueryingMultiset:
    def __init__(self):
        self.data = []
        self.commonNum = 0

    def addData(self, x):
        heappush(self.data, x-self.commonNum)
    
    def addNum(self, x):
        self.commonNum += x

    def pop(self):
        return heappop(self.data) + self.commonNum


qm = QueryingMultiset()
result = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        n, x = query
        qm.addData(x)
    elif query[0] == 2:
        n, x = query
        qm.addNum(x)
    elif query[0] == 3:
        n = query[0]
        result.append(qm.pop())
    else:
        raise Exception("想定外のクエリ")
for r in result:
    print(r)
