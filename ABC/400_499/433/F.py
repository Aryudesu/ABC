class BinomialCoefficient:
    def __init__(self, n: int, mod: int=998244353):
        self.mod = mod
        self.n = n
        self.inv_data = []
        self.data = []
        self.init_data()

    def init_data(self):
        tmp = 1
        for i in range(1, self.n + 1):
            self.data.append(tmp)
            tmp = (tmp * i) % self.mod
        self.data.append(tmp)
        tmp = pow(tmp, self.mod - 2, self.mod)
        for i in range(self.n):
            self.inv_data.append(tmp)
            tmp = (tmp * (self.n - i)) % self.mod
        self.inv_data.append(tmp)
        self.inv_data.reverse()

    def calc(self, n, k):
        if n == 0 and k == 0:
            return 1
        if k < 0:
            return 0
        if n >= 0:
            if n < k:
                return 0
            return (((self.data[n] * self.inv_data[n-k]) % self.mod) * self.inv_data[k]) % self.mod
        if n < 0:
            return self.calc(k-n-1, k) if k % 2 == 0 else -self.calc(k-n-1, k)

MOD = 998244353
MaxNum = 10**6 + 5
bc = BinomialCoefficient(MaxNum)
S = input()
dataL = [[0] * 10 for _ in range(len(S))]
dataR = [[0] * 10 for _ in range(len(S))]
dataL = [0] * 10
dataR = [0] * 10
# 一旦全部の個数をカウントする
for s in S:
    dataR[int(s)] += 1
# 計算する
result = 0
for idx in range(len(S)):
    n = int(S[idx])
    # n文字目でのカウント更新
    dataL[n] += 1
    dataR[n] -= 1
    if n == 9:
        continue
    # L文字目にnを追加した場合，それより右のn+1の個数との兼ね合いを考える
    # 左右の小さい方の個数分が考える最大の文字の使用数
    # 左側は新しく追加した分を元に考えるため Σ_{m} ({}_(最小) C_{m-1} *  {}_{最小} C_m)を考える必要がある
    # 短い方は2^kでいけそう
    # 長い方は？
    # minNum = min(dataL[n], dataR[n])
    # if dataL[n] < dataR[n]:
    #     pass

    # この式変形は思いつきたかった・・・・・・・・・・・・・・・・・・・・・・
    result = (result + bc.calc(dataL[n]-1 + dataR[n+1], dataL[n])) % MOD
print(result)
