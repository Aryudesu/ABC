def isOk(num: int)-> bool:
    m = 0
    ns = str(num)
    for s in ns:
        i = int(s)
        if i < m:
            return False
        m = i
    return True

def calcYakusu(num: int)->list[int]:
    result = []
    for i in range(1, num):
        if i * i == num:
            result.append(i)
            break
        if i * i > num:
            break
        if num % i == 0:
            result.append(i)
            result.append(num//i)
    result.sort()
    return result

for i in range(1000):
    if isOk(i):
        print(calcYakusu(i))
