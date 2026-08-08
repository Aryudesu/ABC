def calcKetawa(num: int)->int:
    result = 0
    while num:
        result += num%10
        num //= 10
    return result

N = 10
K = 100
for k in range(1, K + 1):
    for i in range(2, N):
        l = calcKetawa(i-1)
        c = calcKetawa(i)
        r = calcKetawa(i+1)
        if l % k == c % k == r % k:
            print(i, k, r, r % k)

