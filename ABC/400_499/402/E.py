N, X = [int(l) for l in input().split()]
SCP = []
for n in range(N):
    SCP.append([int(l) for l in input().split()])
result = 0
for n in range(N):
    for m in range(N):
        if n != m:
            result += (SCP[n][0] + SCP[m][0]) * (SCP[n][1] * SCP[m][1])/10000
        else:
            result += SCP[n][0] * (SCP[n][1] * SCP[m][1])/10000
print(result)
