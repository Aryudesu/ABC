K = int(input())
C = [int(l) for l in input().split()]
pascal = []
pascal.append([1])
print(pascal)
for i in range(26):
    p = pascal[-1]
    tmp = []
    for j in range(len(p) - 1):
        tmp.append(p[j] + p[j + 1])
    tmp.append(1)
    pascal.append(tmp)
print(pascal)
