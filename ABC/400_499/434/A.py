W, B = map(int, input().split())
Wg = 1000 * W
for n in range(200000):
    if B * n > Wg:
        print(n)
        break
