N = int(input())
H = list(map(int, input().split()))
INF = 10 ** 10
data = [INF]
result = 0
for h in H:
    while data:
        if data[-1] < h:
            data.pop()
        elif data[-1] > h:
            data.append(h)
            break
        else:
            break
    result += len(data) - 2
print(result)
