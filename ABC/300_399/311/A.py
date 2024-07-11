N = int(input())
S = input()
c = 0
result = 0
for s in S:
    result += 1
    if s == "A":
        c |= 1
    elif s == "B":
        c |= 2
    elif s == "C":
        c |= 4
    if c == 7:
        break
print(result)
