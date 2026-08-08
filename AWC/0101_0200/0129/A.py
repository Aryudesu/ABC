N = int(input())
groupA = []
groupB = []
for n in range(N):
    s, r = input().split()
    if r == "teacher" or r == "doctor":
        groupA.append(f"{s} sensei")
    elif r == "student" or r == "other":
        groupB.append(f"{s} san")
for s in groupA:
    print(s)
for s in groupB:
    print(s)
