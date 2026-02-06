N = int(input())
A = list(map(int, input().split()))
data = []
for a in A:
    if len(data) == 0:
        data.append((a, 1))
    else:
        c, n = data.pop()
        if c == a:
            n += 1
            if n < 4:
                data.append((c, n))
        else:
            data.append((c, n))
            data.append((a, 1))
result = 0
for c, n in data:
    result += n
print(result)
