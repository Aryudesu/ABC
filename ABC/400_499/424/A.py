abc = [int(l) for l in input().split()]
abc.sort()
if abc[0] == abc[1] or abc[1] == abc[2]:
    print("Yes")
else:
    print("No")
