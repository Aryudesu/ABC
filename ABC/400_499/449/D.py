def debugPrint(mes1: str = "debug", mes2: str = ""):
    """デバッグ用"""
    if ISDEBUG:
        print(mes1, mes2)

def calcBasicRectAngle(U: int, R: int):
    """y軸を含まない第一象限の個数"""
    # (1, 1)から(min(U, R), min(U, R))までの点の個数 + x軸上の点の個数 + 残りの縦/横の点の個数
    result = 0
    W = min(U, R)
    num = W//2
    # (1, 1)から(min(U, R), min(U, R))までの点の個数
    result += (((num-1) * 4 + 3) + 3) * num//2
    result += (max(U, R) - W + 1)//2 * min(U, R)
    return result + W

def containO(L: int, R: int, U: int, D: int) -> bool:
    """原点が含まれるか"""
    if not (L <= 0 <= R):
        return False
    if not (D <= 0 <= U):
        return False
    return True

def calcDai1(Y: int, X: int)-> int:
    """第一象限の計算"""
    return calcBasicRectAngle(Y, X)

def calcDai2(Y: int, X: int)-> int:
    """第二象限の計算"""
    return calcBasicRectAngle(-X, Y)

def calcDai3(Y: int, X: int)-> int:
    """第三象限の計算"""
    return calcBasicRectAngle(-Y, -X)

def calcDai4(Y: int, X: int)-> int:
    """第四象限の計算"""
    return calcBasicRectAngle(X, -Y)

def calcData(Y: int, X: int)->int:
    if X > 0 and Y >= 0:
        return calcDai1(Y, X)
    if X <= 0 and Y > 0:
        return calcDai2(Y, X)
    if X < 0 and Y <= 0:
        return calcDai3(Y, X)
    if X >= 0 and Y < 0:
        return calcDai4(Y, X)

def calc(L: int, R: int, U: int, D: int):
    if R < 0:
        L = -L
        R = -R
    if U < 0:
        U = -U
        D = -D
    result = 0
    if containO(L, R, U, D):
        result += calcData(R, U)
        result += calcData(L, U)
        result += calcData(L, D)
        result += calcData(R, D)
        return result + 1
    if D <= 0 <= U:
        result += calcData(R, U)
        result -= calcData(L-1, U)
        result += calcData(R, D)
        result -= calcData(L-1, D)
        return result
    if L <= 0 <= R:
        result += calcData(R, U)
        result -= calcData(R, D-1)
        result += calcData(L, U)
        result -= calcData(L, D-1)
        return result
    result += calcData(R, U)
    result -= calcData(L-1, U)
    result -= calcData(R, D-1)
    result += calcData(L-1, D-1)
    return result

ISDEBUG = True
L, R, D, U = map(int, input().split())
print(calc(L, R, U, D))
