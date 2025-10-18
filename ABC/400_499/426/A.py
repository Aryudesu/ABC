data = dict()
data["Ocelot"] = 0
data["Serval"] = 1
data["Lynx"] = 2

X, Y = input().split()
print("Yes" if data[X] >= data[Y] else "No")
