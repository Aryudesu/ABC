N = int(input())
A = [int(l) for l in input().split()]
count = 1
for a in A:
    if a == count:
        count += 1
result = N - count + 1
print(result if count > 1 else -1)
