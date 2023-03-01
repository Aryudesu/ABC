N, K = [int(l) for l in input().split()]
S = input()
count = 0
result = []
for s in S:
    if s == "o":
        if count < K:
            result.append("o")
            count += 1
        else:
            result.append("x")
    else:
        result.append("x")
print("".join(result))
