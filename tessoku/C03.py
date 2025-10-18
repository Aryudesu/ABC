data = []
D = int(input())
data.append(int(input()))
for d in range(1, D):
    data.append(data[-1] + int(input()))
Q = int(input())
for q in range(Q):
    s, t = [int(l) for l in input().split()]
    if data[s-1] < data[t-1]:
        print(t)
    elif data[s-1] > data[t-1]:
        print(s)
    else:
        print("Same")
