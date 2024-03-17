def kaibun(n):
    tmp = str(n)
    for i in range(len(tmp)):
        if tmp[i] != tmp[len(tmp) - i - 1]:
            return False
        if i >= len(tmp) - i - 1:
            break
    return True

N = int(input())
result = 1
for i in range(1, 10**6 + 1):
    tmp = i ** 3
    if tmp > N:
        break
    if kaibun(tmp):
        result = tmp
print(result)
