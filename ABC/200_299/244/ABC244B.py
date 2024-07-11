def takahashi(T):
    tmp = T.split("R")
    x = 0
    y = 0
    count = 0
    for t in tmp:
        if count == 0:
            x += len(t)
        elif count == 1:
            y -= len(t)
        elif count == 2:
            x -= len(t)
        elif count == 3:
            y += len(t)
        count += 1
        if count == 4:
            count = 0
    print(str(x) + " " + str(y))


N = int(input())
T = input()
takahashi(T)
