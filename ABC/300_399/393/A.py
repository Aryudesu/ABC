S1, S2 = [l == "sick" for l in input().split()]
if S1 and S2:
    print(1)
elif S1:
    print(2)
elif S2:
    print(3)
else:
    print(4)
