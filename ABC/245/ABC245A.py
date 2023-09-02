A, B, C, D = [int(l) for l in input().split()]
Taka = 10000 * A + B * 100
Aoki = 10000 * C + D * 100 + 1
if Taka > Aoki:
    print("Aoki")
else:
    print("Takahashi")
