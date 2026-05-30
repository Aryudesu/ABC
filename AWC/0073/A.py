K, M = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))
result = 0
for a in A:
    result += a in B
print(result)
