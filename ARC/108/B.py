N = int(input())
S = input()
data = [0]
memo = 0
for s in S:
    if s == "f":
        data.append(1)
    elif data[-1] == 1 and s == "o":
        data[-1] += 1
    elif data[-1] == 2 and s == "x":
        data.pop()
        memo += 3
    else:
        data.append(0)
print(len(S) - memo)
