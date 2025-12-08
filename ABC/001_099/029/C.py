from itertools import product
data = []
for dat in product(["a", "b", "c"], repeat=int(input())):
    data.append("".join(dat))
data.sort()
for d in data:
    print(d)
