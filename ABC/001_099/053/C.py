x = int(input())
res = x // 11
res *= 2
if x % 11 == 0:
    pass
elif x % 11 <= 6:
    res += 1
else:
    res += 2
print(res)
