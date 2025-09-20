a, b = [int(l) for l in input().split("-")]
b+=1
if b == 9:
    b = 1
    a += 1
print(f"{a}-{b}")
