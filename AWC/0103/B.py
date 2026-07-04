N = int(input())
Asum = 0
Bsum = 0
for n in range(N):
    a, b = map(int, input().split())
    Asum += a
    Bsum += b
print(min(Asum, Bsum))
