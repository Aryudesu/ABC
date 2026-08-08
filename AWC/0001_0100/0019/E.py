N = int(input())
data = []
for n in range(N):
    w, d = map(int, input().split())
    data.append((d, w))
data.sort()
