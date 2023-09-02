N, D = [int(l) for l in input().split()]
D2 = D**2
XY = []
person = set(range(N))
inf_p = {0}
for n in range(N):
    XY.append([int(l) for l in input().split()])

while True:
    next_inf_p = set()
    for ip in inf_p:
        new_person = set()
        for p in person:
            dist = (XY[p][0] - XY[ip][0]) ** 2 + (XY[p][1] - XY[ip][1]) ** 2
            if dist <= D2:
                next_inf_p.add(p)
            else:
                new_person.add(p)
        person = new_person
    if not next_inf_p:
        break
    inf_p = next_inf_p

for i in range(N):
    if i in person:
        print("No")
    else:
        print("Yes")
