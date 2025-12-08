class Nabeatsu:
    def __init__(self):
        self.num = ["", "ｲﾁ", "ﾆ", "ｻﾝ", "ﾖﾝ", "ｺﾞ", "ﾛｸ", "ﾅﾅ", "ﾊﾁ", "ｷｭｰ"]
        self.keta1 = ["", "ｼﾞｭｰ", "ﾋｬｸ", "ｾﾝ", "ｾﾞﾝ"]
        self.keta2 = ["", "ﾏﾝ", "ｵｸ", "ﾁｮｰ", "ｹｰ", "ｶﾞｲ", "ｼﾞｮ", "ｼﾞｮｰ", "ｺｰ", "ｶﾝ", "ｾｰ", "ｻｲ", "ｺﾞｸ", "ｺｰｶﾞｼｬ", "ｱｿｰｷﾞ", "ﾅﾕﾀ", "ﾌｶｼｷﾞ", "ﾑﾘｮｰﾀｲｽｰ"]
        self.zero_str = "ｾﾞﾛ"
        self.minus = "ﾏｲﾅｽ"

    def isAho(self, num: int)-> bool:
        if num % 3 == 0:
            return True
        if "3" in str(num):
            return True
        return False

    def makeStr(self, num: int)-> str:
        if not self.isAho(num):
            return str(num)
        if num == 0:
            return self.zero_str
        result = []
        if num < 0:
            result.append(self.minus)
            num = -num
        keta_counter = len(str(num))
        keta_pow = 10 ** (len(str(num))-1)
        while keta_pow > 0:
            n = num // keta_pow
            if (keta_counter % 4 == 1 and n == 1) or n != 1:
                result.append(self.num[n])
            if n != 0 and not (keta_counter == 1 and n == 1):
                if (keta_counter-1)%4 == 3 and n == 3:
                    result.append(self.keta1[-1])
                else:
                    result.append(self.keta1[(keta_counter-1)%4])
            if (keta_counter-1)%4 == 0:
                result.append(self.keta2[(keta_counter-1)//4])
            keta_counter -= 1
            num %= keta_pow
            keta_pow //= 10
        return "".join(result)

L = 100001010000
R = 100001010010
nb = Nabeatsu()
for i in range(L, R + 1):
    print(nb.makeStr(i))
