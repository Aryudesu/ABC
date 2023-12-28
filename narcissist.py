from Library.calc_time import calc_time


def isNarcissist1(num):
    nstr = str(num)
    k = len(nstr)
    tmp = num
    res = 0
    while tmp != 0:
        res += (tmp % 10) ** k
        tmp //= 10
    return res == num

@calc_time
def calc1(N):
    result = []
    for i in range(1, N + 1):
        if isNarcissist1(i):
            result.append(i)
    return result


N = 100000
print(calc1(N))
