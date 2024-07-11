D = """
tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
"""
T = D.split("\n")
data = dict()
for s in T:
    d = s.split()
    if len(d) != 2:
        continue
    data[d[0]] = int(d[1])
print(data.get(input()))
