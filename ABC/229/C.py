N, W = [int(l) for l in input().split()]
AB = [[int(l) for l in input().split()] for _ in range(N)]
AB.sort(reverse=True)
result = 0
Wsum = 0
for a, b in AB:
    if Wsum + b <= W:
        result += a * b
        Wsum += b
    else:
        Wtmp = W - Wsum
        result += Wtmp * a
        Wsum += Wtmp
print(result)
