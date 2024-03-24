def calc(x):
    a, b, c = x
    # 揃ってるものは0
    if a == b and b == c:
        return 0
    # 偶奇が異なると駄目
    if a % 2 != b % 2 or b % 2 != c % 2 or a % 2 != c % 2:
        return -1
    # 正規化
    x.sort()
    y = [0, (x[1] - x[0])//2, (x[2] - x[0])//2]
    if (y[0] + y[1] + y[2]) % 3 != 0:
        return -1
    if y[1] == 0:
        return (y[2] // 3) * 2
    if 2*y[1] < y[2]:
        return y[1] + ((y[2] - 2 * y[1])//3) * 2
    return (y[2] - y[1]) + ((y[2] - 2 * (y[2] - y[1]))//3) * 2


T = int(input())
result = []
for t in range(T):
    x = [int(l) for l in input().split()]
    result.append(calc(x))
for r in result:
    print(r)
