N = int(input())
data = []
for n in range(N):
    a, b = map(int, input().split())
    data.append((b, a, -n))
data.sort(reverse=True)
result = [1 - n for b, a, n in data]
for r in result:
    print(r)
