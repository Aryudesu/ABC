N, K = map(int, input().split())
S = input()
T = input()
result = 0
for s, t in zip(S, T):
    result += (s == t)
print(max((N-result)-K, 0))
