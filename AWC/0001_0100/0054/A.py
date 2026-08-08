from collections import defaultdict

N = int(input())
data = defaultdict(int)
for _ in range(N):
    S = input()
    data[S[0]] += 1
print(max(i for k, i in data.items()))
