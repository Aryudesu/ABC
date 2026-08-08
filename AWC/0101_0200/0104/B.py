N, T = map(int ,input().split())
A = list(map(int, input().split()))
result = 10**18
for a in A:
    result = min(result, ((T + a - 1) // a) * a)
print(result)
