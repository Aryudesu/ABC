A = []
while True:
    num = int(input())
    A.append(num)
    if num == 0:
        break
A.reverse()
for a in A:
    print(a)
