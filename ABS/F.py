N = int(input())
A = [int(l) for l in input().split()]
A.sort(reverse=True)
result = 0
f = 1
for a in A:
    result += a * f
    f *= -1
print(result)
