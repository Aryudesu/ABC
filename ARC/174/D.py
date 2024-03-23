def isPrefix(a, b):
    """aがbの接頭辞か"""
    s = len(str(a))
    t = len(str(b))
    tmp = b // (10 ** (t - s))
    return a == tmp

def sq(num):
    l = 1
    r = num + 1
    while l <= r:
        tmp = (l + r) // 2
        if tmp**2 <= num:
            l = tmp + 1
        else:
            r = tmp - 1
    return r

data = []
for n in range(1, 10**6 + 1):
    tmp = sq(n)
    if isPrefix(tmp, n):
        data.append(n)
print(data)
