from collections import defaultdict

N, Q = map(int, input().split())
S = input()

for _ in range(Q):
    l, r = map(int, input().split())
    l, r = l - 1, r - 1
