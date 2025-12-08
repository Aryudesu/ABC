class NodeData:
    def __init__(self):
        self.nextData = dict()
        self.isXData = False
        self.isYend = False

class Trie:
    def __init__(self):
        self.base = NodeData()
        self.base.isXData = True
        self.count = 0
        self.result = 0
    
    def addX(self, S: str):
        tre: NodeData = self.base
        for s in S:
            tre.nextData[s] = tre.nextData.get(s, NodeData())
            tre = tre.nextData[s]
            tre.isXData = True
            if tre.isYend:
                self.result += 1
                tre.isYend = False

    def addY(self, S: str):
        tre: NodeData = self.base
        for s in S:
            tre.nextData[s] = tre.nextData.get(s, NodeData())
            tre = tre.nextData[s]
        if tre.isXData:
            self.result += 1
        tre.isYend = True
        


trie = Trie()
Q = int(input())
yCount = 0
res = []
for q in range(Q):
    T, S = input().split()
    if T == "1":
        trie.addY(S)
    elif T == "2":
        trie.addX(S)
        yCount += 1
    else:
        raise Exception()
    res.append(yCount - trie.result)
for r in  res:
    print(r)
