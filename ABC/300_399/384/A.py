N, c1, c2 = input().split()
S = input()
result = ""
for s in S:
    if s == c1:
        result += c1
    else:
        result += c2
print(result)
