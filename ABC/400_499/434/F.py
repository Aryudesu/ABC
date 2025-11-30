def next_permutation(data):
    size = len(data)
    left = size - 2
    while left >= 0 and data[left] >= data[left + 1]:
        left -= 1
    if left < 0:
        return 0
    right = size - 1
    while data[left] >= data[right]:
        right -= 1
    data[left], data[right] = data[right], data[left]
    left += 1
    right = size - 1
    while left < right:
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return 1

T = int(input())
for _ in range(T):
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    data = dict()
    revData = dict()
    c = 0
    for i in range(N):
        if S[i] in data:
            continue
        data[S[i]] = c
        revData[c] = S[i]
        c += 1
    prev = []
    M = c
    for s in S:
        prev.append(data[s])
    for i in prev:
        print(revData[i], end = "")
    print()
