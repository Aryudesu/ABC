N, M = map(int, input().split())
W = []
if N > 1:
    W = list(map(int, input().split()))
elif N == 1:
    print(1)
    exit(0)
else:
    raise ValueError()
m = 0
result = 0
for i in range(1, N):
    if W[i-1] == 1:
        if m == M:
            break
        m += 1
    result = i
print(result + 1)
