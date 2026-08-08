N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
count = 0
result = 0
prev = 0
while A:
    count += 1
    prev = A.pop()
    if count == K:
        break
while A and prev == A[-1]:
    count += 1
    prev = A.pop()
print(count)
