from math import lcm, gcd

N = int(input())
p, q = map(int, input().split())
d = p
n = q
for _ in range(N-1):
    p, q = map(int, input().split())
    d = lcm(d, p)
    n = gcd(n, q)
    g = gcd(d, n)
    d //= g
    n //= g
print(d, n)
