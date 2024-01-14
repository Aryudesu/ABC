N = int(input())
w = 0
b = 0
for n in range(N):
    if input() == "black":
        b += 1
    else:
        w += 1
print("white" if w > b else "black")
