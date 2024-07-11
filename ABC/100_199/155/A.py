data = [int(l) for l in input().split()]
data.sort()
print("Yes" if data[0] == data[1] and data[1] != data[2] or data[1] == data[2] and data[0] != data[1] else "No")

