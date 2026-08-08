N = int(input())
result = 0
for n in range(N):
    t, p = input().split()
    p = int(p)
    if t == "normal":
        result += p
    elif t == "half":
        result += p//2
    else:
        raise ValueError()
print(result)
