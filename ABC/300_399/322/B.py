N, M = [int(l) for l in input().split()]
S = input()
T = input()
res = 3
if T[:len(S)] == S:
    res -= 2
if T[-len(S):] == S:
    res -= 1
print(res)
