d = 0
for i in range(3):
    ipt = input()
    d += sum([1 << (i * 3 + j) if ipt[j] == "#" else 0 for j in range(3)])
f = 0
for e in [7, 56, 73, 84, 448, 146, 273, 292]:
    f += 0 if (d & e) ^ e else 1
print(f)
