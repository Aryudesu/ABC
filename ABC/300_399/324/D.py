N = int(input())
S = [l for l in input()]
S.sort(reverse=True)
M = int("".join(S))
data = set()


d = []

tmp = int((10 ** (N + 1)) ** 0.5)
i = 0
while i ** 2 <= M:
    dat = i ** 2
    tmp = list(str(dat).zfill(N))
    tmp.sort(reverse=True)
    if tmp == S:
        data.add(dat)
    i += 1
print(len(data))
