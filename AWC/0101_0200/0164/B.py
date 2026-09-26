N, T = map(int, input().split())
S = list(map(int, input().split()))
mx = 0
result = 0
for s in S:
    result += mx >= T and mx > s
    mx = max(s, mx)
print(result)
