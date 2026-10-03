from math import gcd

N = int(input())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))

result = 0
for i in range(N):
    count = dict()
    counter = [0, 0, 0, 0]
    for j in range(N):
        if i == j:
            continue
        dx, dy = XY[j][0] - XY[i][0], XY[j][1] - XY[i][1]
        num = (dx % 2) * 2 + (dy % 2)
        match num:
            case 0:
                result += counter[0] + counter[1] + counter[2] + counter[3]
            case 1:
                result += counter[0] + counter[1]
            case 2:
                result += counter[0] + counter[2]
            case 3:
                result += counter[0] + counter[3]
            case _:
                raise ValueError()
        g = gcd(dx, dy)
        x, y = dx//g, dy//g
        if y < 0:
            x, y = -x, -y
        elif y == 0 and x < 0:
            x, y = -x, -y
        key = (x, y)
        c = count.get(key, 0)
        result -= c
        count[key] = c + 1
        counter[num] += 1
print(result//3)
