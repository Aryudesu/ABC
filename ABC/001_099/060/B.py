from math import gcd

A, B, C = map(int, input().split())
G = gcd(A, B)
print("YES" if C % G == 0 else "NO")
