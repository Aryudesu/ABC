def calc(result):
    N = int(input())
    data = []
    ipt = input().split()
    for i in range(N):
        data.append((int(ipt[i]), i + 1))
    data.sort()
    b, a = data[0]
    count = 1
    for i in range(1, N):
        if b < data[i][0] and a < data[i][1]:
            b = data[i][0]
            a = data[i][1]
            count += 1
    result.append(count)


result = []
T = int(input())
for t in range(T):
    calc(result)
for r in result:
    print(r)
