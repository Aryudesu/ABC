def calc(a: int, b: int, x: int, y: int)-> int:
    if x == y:
        return 2 * x * min(a, b)
    tmp = 2 * x * min(a, b)
    d = y - x
    tmp2 = (d // 2) * 4 * min(a, b)
    tmp2 = min(tmp2, (d // 2) * (a + b))
    if d % 2 == 1:
        tmp2 += min(b, 3 * a)
    return tmp + tmp2

T = int(input())
result = []
for _ in range(T):
    a, b, x, y = map(int, input().split())
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x > y:
        x, y = y, x
        a, b = b, a
    result.append(calc(a, b, x, y))
for r in result:
    print(r)
