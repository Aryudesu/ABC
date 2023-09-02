N = int(input())
c = 0
mes = 'No'
for n in range(N):
    D1, D2 = [int(l) for l in input().split()]
    c = c+1 if D1 == D2 else 0
    if c == 3:
        mes = 'Yes'
print(mes)
