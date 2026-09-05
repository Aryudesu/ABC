N = int(input())
L = list(map(int, input().split()))
S = sum(L)
result = 10 ** 18
l = 0
for n in L:
    l += n
    r = S - l
    result = min(result, abs(r-l))
print(result)
