from itertools import permutations

data = "HENOS"
for dat in permutations(range(5)):
    res = ""
    for i in range(5):
        res += data[dat[i]]
    if res[0] in "HE":
        continue
    if res[1] in "OE":
        continue
    if res[3] in "OE":
        continue
    if res[4] in "HNS":
        continue
    print(res)
