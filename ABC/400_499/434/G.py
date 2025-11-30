MOD = 998244353
N, Q = map(int, input().split())
data = []
num = 0
for q in range(Q):
    n, a, b = map(int, input().split())
    if n == 1:
        x, c = a, b
    elif n == 2:
        l, r = a, b
