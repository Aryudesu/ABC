import random


def userInput():
    return int(input())


def yamanote(N):
    dat = list(range(1, 2 * N + 2))
    while True:
        taka = random.choice(dat)
        print(taka)
        dat.remove(taka)
        user = userInput()
        if user == 0:
            break
        dat.remove(user)


N = int(input())
yamanote(N)
