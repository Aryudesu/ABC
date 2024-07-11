H = int(input())
i = 0
tmp = 0
while tmp <= H:
    tmp += (1 << i)
    i += 1
print(i)
