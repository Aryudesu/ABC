data = set(list("abcdefghijklmnopqrstuvwxyz"))
for s in input():
    data.discard(s)
print(data.pop())
