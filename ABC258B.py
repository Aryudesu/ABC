N = int(input())
A= []
for n in range(N):
    tmp = [int(l) for l in input()]
    A.append(tmp)
max = 0
for i in range(N):
    for j in range(N):
        for x in range(3):
            for y in range(3):
                if x == 1 and y == 1:
                    continue
                tmp = 0
                for n in range(N):
                    tmp = tmp * 10 + A[(i + (x-1) * n) % N][(j + (y-1) * n) % N]
                if max < tmp:
                    max = tmp
print(max)
