N = [int(l) for l in input().split()]
A = [int(l) for l in input().split()]
A.sort()
dat = list(set(A))
count = 0
for num in dat:
    if count != num:
        print(count)
        break
    count += 1
if count == len(dat):
    print(count)
