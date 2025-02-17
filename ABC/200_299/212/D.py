class Osa_kMethod:
    def __init__(self, n:int = 10 ** 6):
        self.spf = list(range(n))
        for p in range(n):
            if p * p > n:
                break
            for i in range(p, n, p):
                if self.data[i] == i:
                    self.data[i] = p


