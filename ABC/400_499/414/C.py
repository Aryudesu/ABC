def reverseNum(num):
    result = 0
    tmp = num
    while tmp > 0:
        result = result * 10 + tmp % 10
        tmp //= 10
    return result

def base10int(value, base):
    result = []
    tmp = value
    while tmp:
        result.append(tmp % base)
        tmp //= base
    return result

def isKaibun(data):
    for i in range(len(data)//2):
        if data[i] != data[-i-1]:
            return False
    return True

A = int(input())
N = int(input())
result = 0
for i in range(10**6):
    f = False
    # 2倍の長さ
    num = i * (10 ** len(str(i))) + reverseNum(i)
    if num <= N:
        f = True
        b = base10int(num, A)
        if isKaibun(b):
            result += num
    # 2倍-1の長さ
    num = i * (10 ** (len(str(i))-1)) + reverseNum(i//10)
    if num <= N:
        f = True
        b = base10int(num, A)
        if isKaibun(b):
            result += num
    if not f:
        break
print(result)
