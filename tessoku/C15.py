N = int(input())
K = int(input())
AB = []
for n in range(N):
    l, r = map(int, input().split())
    AB.append((r + K, l, n + 1))
AB.sort(reverse=True)
print(AB)
for r, l, n in AB:
    pass
