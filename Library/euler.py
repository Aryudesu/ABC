import math

N = 160


def Ei(x):
    result = 0
    sgn = -1
    denom = x
    m = 1
    for i in range(1, math.floor(x) + 1):
        if sgn == -1:
            tmp -= m/denom
        else:
            tmp += m/denom
        result += tmp
        denom *= x
        sgn = -sgn
        m *= i
    return math.exp(-x) * result


def gamma(x):
    result = Ei(-x) - math.log(x)
    tmp = 0
    denom = 1
    mole = x
    sgn = -1
    for i in range(1, N + 1):
        denom *= i
        if sgn == -1:
            tmp -= mole/(denom * i)
        else:
            tmp += mole/(denom * i)
        sgn = -sgn
        mole *= x
    return result - tmp


print(gamma(20.1))
