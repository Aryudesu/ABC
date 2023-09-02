def calcShampoo(VABC):
    Nokori = VABC[0] % (VABC[1] + VABC[2] + VABC[3])
    Nokori -= VABC[1]
    if Nokori < 0:
        return "F"
    Nokori -= VABC[2]
    if Nokori < 0:
        return "M"
    Nokori -= VABC[3]
    return "T"


VABC = [int(l) for l in input().split()]
res = calcShampoo(VABC)
print(res)
