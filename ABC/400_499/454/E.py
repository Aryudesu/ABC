def calc(n: int, a: int, b: int)->str|None:
    if n % 2:
        return None
    if a % 2 == b % 2:
        return None
    result = ""
    y = 1
    x = 1
    rf = True
    snf = False
    while y != n and x != n:
        if rf:
            x += 1
        else:
            x -= 1
    

T = int(input())
result = []
for _ in range(T):
    n, a, b = map(int, input().split())
    res = calc(n, a, b)
    if res is None:
        result.append("No")
    else:
        result.append("Yes")
        result.append(res)

for r in result:
    print(r)
