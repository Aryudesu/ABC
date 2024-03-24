class StackData:
    def __init__(self, A=[]):
        self.pointer = -1
        self.data = []
        for a in A:
            self.data.append(a)
            self.pointer += 1

    def push(self, a):
        """末尾にデータを追加します"""
        if self.pointer + 1 < len(self.data):
            self.data[self.pointer + 1] = a
            self.pointer += 1
        else:
            self.data.append(a)
            self.pointer += 1

    def pop(self):
        """末尾を1つ取り出します"""
        res = self.data[self.pointer]
        self.pointer -= 1
        return res

    def getLast(self):
        """末尾の要素を取得します"""
        return self.data[self.pointer]

    def getIndex(self, index):
        assert index <= self.pointer
        return self.data[index]

Q = int(input())
result = []
st = StackData()
for q in range(Q):
    query = [l for l in input().split()]
    if query[0] == "1":
        st.push(query[1])
    elif query[0] == "2":
        result.append(st.getLast())
    elif query[0] == "3":
        st.pop()
for r in result:
    print(r)
