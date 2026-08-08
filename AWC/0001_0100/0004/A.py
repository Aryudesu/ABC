N, S, T = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
t1 = s // 60
t2 = s % 60
t = t1 * 100 + t2 + S * 100
if T*100 >= t:
    print("Yes")
else:
    print("No")
