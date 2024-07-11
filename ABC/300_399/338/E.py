def calc(F, data, N):
    if F is None:
        return True
    fa, fb = F
    if fa > fb:
        fa, fb = fb, fa
    if fa < N:
        fa, fb = fb, fa
    for n in range(2*N):
        tmp = data.get((fa - 1) % (2 * N))
        if tmp is None:
            raise Exception()
        if tmp == (fb + 1) % (2 * N):
            fa = (fa - 1) % (2 * N)
            fb = tmp
        else:
            return True
    return False


N = int(input())
data = dict()
F = None
for n in range(N):
    a, b = [int(l) - 1 for l in input().split()]
    data[a] = b
    data[b] = a
    if abs(a - b) == 1:
        F = (a, b)
print("Yes" if calc(F, data, N) else "No")

