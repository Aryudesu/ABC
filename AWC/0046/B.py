N = int(input())
if N == 1:
    print(1)
    exit()
countSQ = 0
for i in range(1, N):
    tmp = i * i
    if tmp > N:
        break
    countSQ += 1
print(countSQ)
