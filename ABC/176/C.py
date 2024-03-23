N = int(input())
A = [int(l) for l in input().split()]
l = A[0]
result = 0
for a in A:
    if a < l:
        result += l - a
    if a > l:
        l = a
print(result)
