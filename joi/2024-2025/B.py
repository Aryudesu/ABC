N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
data = list(zip(A, B))
data.sort()
result = 0
s = 0
for a, b in data:
    result = max(a - s, result)
    s += b
print(result)
