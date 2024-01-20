def calcBit(N):
    result = []
    if N == 0:
        return [0]
    tmpN = N
    while tmpN:
        result.append(tmpN % 2)
        tmpN >>= 1
    return result


def calc(S, N):
    bitN = calcBit(N)
    if len(bitN) > len(S):
        while len(bitN)>len(S):
            S.append("0")
    elif len(bitN) < len(S):
        while len(bitN) < len(S):
            S.append(0)
    bitN.reverse()
    S.reverse()
    print(bitN)
    print(S)
    lenBN = len(bitN)
    sameF = True
    result = 0
    for _ in range(lenBN):
        pass


S = list(input())
N = int(input())
print(calc(S, N))
