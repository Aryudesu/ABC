class NodeData:
    def __init__(self, s):
        self.st = s
        self.next = dict()
        self.isX = False
        self.count = 0

tree = dict()
result = 0
Q = int(input())
res = []
for q in range(Q):
    T, S = input().split()
    if T == "1":
        tr = tree
        c = 0
        for idx in range(len(S)):
            s = S[idx]
            tre = tr.get(s)
            if tre is None:
                tre = NodeData(s)
            tr[s] = tre

            if tre.isX:
                c += tre.count
            tre.count += 1

            tr = tre.next
        tmp = (tre.count - c)
        result -= max(tmp, 0)
        tre.isX = True
    elif T == "2":
        flag = True
        tr = tree
        for idx in range(len(S)):
            s = S[idx]
            tre = tr.get(s)
            if tre is None:
                tre = NodeData(s)
            tr[s] = tre
            tr = tre.next
            if flag:
                tre.count += 1
            if tre.isX:
                flag = False
                break
        if flag:
            result += 1
    else:
        raise Exception()
    res.append(result)
for r in  res:
    print(r)
