def popCount(num):
    tmp = num
    result = 0
    while tmp:
        if tmp & 1:
            result += 1
        tmp >>= 1
    return result

def check(a, b, C):
    """a >= b前提で計算行っていく"""
    pc = popCount(C)
    if pc < (a - b):
        return False, pc
    if pc % 2 != (a - b) % 2:
        return False, pc
    return True, pc

def makeAnswer(a, b, C, D):
    """a >= b前提で計算行っていく"""
    maxNum = 2**60
    E = a - b
    aNum = (D + E)//2
    bNum = (D - E)//2
    aCount = 0
    bCount = 0
    aResult = 0
    bResult = 0
    bit = 1
    while aCount < aNum or bCount < bNum:
        if C & bit:
            if aCount < aNum:
                aResult = aResult | bit
                aCount += 1
            else:
                bResult = bResult | bit
                bCount += 1
        bit <<= 1
    bit = 1
    while aCount < a or bCount < b:
        if not (C & bit):
            aResult = aResult | bit
            bResult = bResult | bit
            aCount += 1
            bCount += 1
        bit <<= 1
    if aResult ^ bResult == C and aResult < maxNum and bResult < maxNum and aCount == a and bCount == b:
        return (True, aResult, bResult)
    return (False, aResult, bResult)

def calc(a, b, C):
    rev = False
    if a < b:
        rev = True
        a, b = b, a
    res, D = check(a, b, C)
    if not res:
        print(-1)
        return
    r, X, Y = makeAnswer(a, b, C, D)
    if not r:
        print(-1)
        return
    if rev:
        X, Y = Y, X
    print(X, Y)
    return

a, b, C = [int(l) for l in input().split()]
calc(a, b, C)
