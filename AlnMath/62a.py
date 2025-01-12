class Graph:
    def __init__(self, A):
        """グラフ配列A[]を設定"""
        self.data = [a - 1 for a in A]
        self.N = len(A)

    def moveK(self, K, s = 1):
        """sから初めてk回遷移した場合の到着点"""
        p = s - 1
        count = 0
        cData = dict()
        while True:
            count += 1
            p = self.data[p]
            if count == K:
                return p + 1
            if p in cData:
                if (K - count) % (count - cData[p]) == 0:
                    return p + 1
            cData[p] = count

N, K = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
gp = Graph(A)
print(gp.moveK(K, 1))
