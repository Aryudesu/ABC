N = int(input())
S = input()
x = 0
result = 0
for s in S:
    if s == "I":
        x += 1
    elif s == "D":
        x -= 1
    else:
        raise Exception()
    result = max(result, x)
print(result)
