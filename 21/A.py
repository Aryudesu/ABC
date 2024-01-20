def calc(N):
    tmpN = N
    c = 8
    result = []
    while tmpN:
        if tmpN >= c:
            result.append(c)
        else:
            while True:
                if tmpN >= c:
                    result.append(c)
                    break
                c //= 2
        tmpN -= c
    return result


N = int(input())
result = calc(N)
print(len(result))
for r in result:
    print(r)
