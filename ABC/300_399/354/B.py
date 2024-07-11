N = int(input())
SC = []
t = 0
for n in range(N):
    s, c = [l for l in input().split()]
    cint = int(c)
    t += cint
    SC.append([s, cint])
SC.sort()
print(SC[t % N][0])
