N = int(input())
B = []
C = []
for n in range(N):
    ipt = input()
    tmp = []
    for ip in ipt:
        tmp.append(ip)
    B.append(tmp)

data = []
for idx in range(N - 1):
    data.append(B[0][idx])
for idx in range(N - 1):
    data.append(B[idx][N - 1])
for idx in range(N - 1):
    data.append(B[N - 1][-idx - 1])
for idx in range(N - 1):
    data.append(B[-idx - 1][0])

ld = len(data)
count = -1
for idx in range(N - 1):
    B[0][idx] = data[count]
    count = (count + 1) % ld
for idx in range(N - 1):
    B[idx][N - 1] = data[count]
    count = (count + 1) % ld
for idx in range(N - 1):
    B[N - 1][-idx - 1] = data[count]
    count = (count + 1) % ld
for idx in range(N - 1):
    B[-idx - 1][0] = data[count]
    count = (count + 1) % ld
for b in B:
    print("".join(b))
