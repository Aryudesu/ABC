_ = input()
A = list(map(int, input().split()))
result = []
for a in A:
    if not result or result[-1] != a:
        result.append(a)
print(*result, sep="\n")
