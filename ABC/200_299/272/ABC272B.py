N, M = [int(l) for l in input().split()]
person = []
for i in range(N):
    person.append([0 for l in range(N)])
KX = []
for m in range(M):
    KX.append([int(l) for l in input().split()])

for kx in KX:
    # print(kx)
    for i in range(1, kx[0] + 1):
        for j in range(1, kx[0] + 1):
            person[kx[i]-1][kx[j]-1] += 1
            person[kx[j]-1][kx[i]-1] += 1
# print(person)
for i in range(N):
    for j in range(N):
        if person[i][j] == 0:
            print('No')
            exit()
print('Yes')
