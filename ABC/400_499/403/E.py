class Node:
    def __init__(self):
        self.nextNode = dict()
        self.isX = False
        self.endYCount = 0

class TrieTree:
    def __init__(self):
        self.root = Node()

    def addX(self, X: str)->bool:
        node = self.root
        for x in X:
            nextNode: Node = node.nextNode.get(x, Node())
            nextNode.isX = True
            node.nextNode[x] = nextNode
            node = nextNode
        node.endXCount += 1
        return not node.isY

    def addY(self, Y: str)->int:
        node = self.root
        result = 0
        for y in Y:
            nextNode = node.nextNode.get(y, Node())
            nextNode.isY = True
            result += nextNode.endXCount
            node.nextNode[y] = nextNode
            node = nextNode
        return result

trie = TrieTree()
Q = int(input())
xCount = 0
res = []
for q in range(Q):
    T, S = input().split()
    if T == "1":
        tmp = trie.addX(S)
        if tmp:
            xCount += 1
    elif T == "2":
        tmp = trie.addY(S)
        xCount -= tmp
    else:
        raise Exception()
    res.append(xCount)
for r in  res:
    print(r)
