D = int(input())
result = D
for i in range(D):
    j = i ** 2
    if j > D:
        break
    r = abs(D - j)
    if result > r:
        result = r

    tmp = int((D - j) ** 0.5)
    r = abs(D - tmp ** 2 - j)
    if result > r:
        result = r

    r = abs(D - (tmp+1) ** 2 - j)
    if result > r:
        result = r

    r = abs(D - (tmp-1) ** 2 - j)
    if result > r:
        result = r
print(result)
