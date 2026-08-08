S = input()
N = len(S)
result = 0
for center in range(N):
    l = 0
    f = False
    count = 0
    while 0 <= center - l <= center + l < N:
        if S[center - l] != S[center + l]:
            if not f:
                f = True
            else:
                break
        count += 1
        l += 1
    result += count
for center in range(N-1):
    l = 0
    f = False
    count = 0
    while 0 <= center - l <= center + 1 + l < N:
        if S[center - l] != S[center + 1 + l]:
            if not f:
                f = True
            else:
                break
        count += 1
        l += 1
    result += count
print(result)
