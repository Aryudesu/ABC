N = int(input())
n=1
A = []
B = []
while n*n <= N:
    if N % n == 0:
        A.append(n)
        if n * n == N:
            break
        B.append(N//n)
    n+=1

for a in A:
    print(a)
for idx in range(len(B)):
    print(B[-idx-1])