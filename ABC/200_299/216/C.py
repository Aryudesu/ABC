N = int(input())
result = []
tmp = N
while tmp:
    if tmp & 1:
        result.append("A")
    tmp >>= 1
    if tmp:
        result.append("B")
result.reverse()
print("".join(result))
