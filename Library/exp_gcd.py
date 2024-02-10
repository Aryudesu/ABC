def ext_gcd(a, b):
    """ 拡張ユークリッドの互助法"""
    if b == 0:
        return (1, 0)
    x, y = ext_gcd(b, a % b, y, x)
    y -= (a // b) * x
    return (x, y)
