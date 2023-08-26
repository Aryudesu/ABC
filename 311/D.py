N, M = [int(l) for l in input().split()]
S = []
data = []
person = set()
stoped = set()
for n in range(N):
    S.append(input())
for n in range(N):
    tmp = []
    for m in range(M):
        tmp.append(True)
    data.append(tmp)

dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

person.add((1, 1))
data[1][1] = False
count = 1
while person:
    # print(person)
    new_person = set()
    for p in person:
        x, y = p
        for dd in dxdy:
            px, py = x, y
            dx, dy = dd
            while True:
                if S[py + dy][px + dx] == "#":
                    break
                px += dx
                py += dy
                if data[py][px]:
                    count += 1
                    data[py][px] = False
            if (px, py) not in stoped:
                new_person.add((px, py))
                stoped.add((px, py))
    person = new_person
# for dat in data:
#     tmp = []
#     for d in dat:
#         tmp.append("x" if d else "o")
#     print("".join(tmp))
print(count)
