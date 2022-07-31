Y = int(input())
res = Y
if Y % 4 == 0:
    res += 2
elif Y % 4 == 1:
    res += 1
elif Y % 4 == 3:
    res += 3
print(res)
