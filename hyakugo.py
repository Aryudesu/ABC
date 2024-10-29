def ext_gcd(a: int, b: int, x: list, y: list):
    """拡張ユークリッドの互除法"""
    if b == 0:
        x[0] = 1
        y[0] = 0
        return a
    d = ext_gcd(b, a % b, y, x)
    y[0] -= (a // b) * x[0]
    return d

def calc105(data):
    """i≠jのときgcd(m_i, m_j) = 1となるm_1, m_2, ..., m_nに対して a≡a_1 mod m_1, a≡a_2 mod m_2, ..., a≡a_n mod m_n を解く"""
    # 計算
    allProd = 1
    for dat in data:
        allProd *= dat[0]
    result = 0
    for dat in inData:
        a = allProd//dat[0]
        b = dat[0]
        x, y = [0], [0]
        ext_gcd(a, b, x, y)
        result += a * x[0] * dat[1]
    return result % allProd

# データ入力
inData = []
while True:
    # xで割るとy余る
    try:
        x, y = [int(l) for l in input().split()]
        inData.append((x, y))
    except:
        break

print("Ans.", calc105(inData))
