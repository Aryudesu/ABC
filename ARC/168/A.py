N = int(input())
S = input()
result = 0
count = 0
for s in S:
    if s == ">":
        count += 1
    else:
        count = 0
    result += count
print(result)