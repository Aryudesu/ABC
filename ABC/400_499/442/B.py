Q = int(input())
result = []
volume = 0
music = False
for _ in range(Q):
    a = int(input())
    if a == 1:
        volume += 1
    elif a == 2:
        volume = max(0, volume - 1)
    elif a == 3:
        music = not music
    else:
        raise Exception()
    result.append("Yes" if volume >= 3 and music else "No")
for r in result:
    print(r)
