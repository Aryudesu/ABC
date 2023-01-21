from functools import lru_cache
# お願いします通ってください
N, X = [int(l) for l in input().split()]
AB = []
num = 0
for n in range(N):
    AB.append([int(l) for l in input().split()])


@lru_cache(maxsize=None)
def calc(N, X, s, depth):
    if depth == N:
        return False
    for i in range(AB[depth][1] + 1):
        t = s + AB[depth][0] * i
        if t == X:
            return True
        elif t > X:
            return False
        r = calc(N, X, t, depth + 1)
        if r:
            return True
    return False


print('Yes' if calc(N, X, 0, 0) else 'No')
