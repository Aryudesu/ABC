A, B = map(int, input().split())
T = input()
r = 0
b = 0
rResult = 0
bResult = 0
prev = ""
for t in T:
    match t:
        case "R":
            r += 1
            if "R" != prev:
                rResult += 1
        case "B":
            b += 1
            if "B" != prev:
                bResult += 1
        case _:
            raise ValueError()
    prev = t
if r != A or b != B:
    print(-1)
    exit(0)

if rResult == 1 and bResult == 1 and T[0] == "R" and T[-1] == "B":
    print(0)
    exit(0)

if T[-1] == "B":
    bResult -= 1
if T[0] == "R":
    rResult -= 1
print(min(rResult, bResult))
