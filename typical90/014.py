N = int(input())
A = [int(l) for l in input().split()]
A_DATA = [(A[i], i) for i in range(N)]
A_DATA.sort()
B = [int(l) for l in input().split()]
B.sort()
result = 0
for i in range(N):
    a, num = A_DATA[i]
    b = B[i]
    result += abs(a-b)
print(result)
