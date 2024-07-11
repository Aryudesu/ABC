S = input()
count = 1
result = True
for s in S:
    if count == 0 and s == "1":
        result = False
    count = 1 - count
print("Yes" if result else "No")
