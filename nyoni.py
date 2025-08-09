N = 100
for a in range(-N, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(-N, N + 1):
            for d in range(c + 1, N + 1):
                if a * b * c * d == 0:
                    continue
                if (a*a + b * b) * c * d + (c * c + d * d) * a * b == 13:
                    print(a, b, c, d)
