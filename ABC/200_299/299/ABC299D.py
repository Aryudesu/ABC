N = int(input())
L = 0
R = N - 1
for i in range(20):
    tmp = (L + R)//2
    print("?", str(tmp + 1))
    data = int(input())
    if data == 1:
        R = tmp
    else:
        L = tmp
    if L + 1 == R:
        break
print("!", L + 1)
