N, K = map(int, input().split())
A = list(map(int, input().split()))
x = 0
for a in A:
    x ^= (a % (K + 1))
print("Takahashi" if x else "Aoki")
