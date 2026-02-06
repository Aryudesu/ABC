N, K = map(int, input().split())
res = N
count = N
while count < K:
    res += 1
    count += res
print(res - N)
