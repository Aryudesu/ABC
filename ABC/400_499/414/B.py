N = int(input())
CL = []
co = 0
for n in range(N):
    c, l = input().split()
    CL.append([c, int(l)])
    co += int(l)
if co > 100:
    print("Too Long")
else:
    result = ""
    for c, l in CL:
        result += c * l
    print(result)
