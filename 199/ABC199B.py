N = int(input())
A = [int(l) for l in input().split()]
B = [int(l) for l in input().split()]
Am = max(A)
Bm = min(B)
print(Bm - Am + 1 if Bm - Am >= 0 else 0)
