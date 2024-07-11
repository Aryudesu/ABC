N, S, M, L = [int(l) for l in input().split()]
result = 10**10
for s in range(21):
    for m in range(21):
        for l in range(21):
            if 6*s + 8*m + 12*l >= N:
                r = S * s + M * m + L * l
                if r < result:
                    result = r
print(result)
