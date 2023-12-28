N = int(input())
result = 0
for n in range(N):
    p, q = [int(l) for l in input().split()]
    result += q / p
print(result)
