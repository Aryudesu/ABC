S, T, K = map(int, input().split())
count = 0
num = S
while num < T:
    num *= 2
    count += 1
if count <= K and num == T:
    print(count)
else:
    print(-1)
