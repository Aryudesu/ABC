from collections import defaultdict

N = int(input())
S = input()
all = ((N+1) * (N+2)) // 2
ABnum = [0]
BCnum = [0]
CAnum = [0]
ABCnum = [(0, 0, 0)]
a, b, c = 0, 0, 0
for s in S:
    if s == "A":
        a += 1
    elif s == "B":
        b += 1
    elif s == "C":
        c += 1
    else:
        raise ValueError()
    ABnum.append(a-b)
    BCnum.append(b-c)
    CAnum.append(c-a)
    m = min(a, b, c)
    ABCnum.append((a-b, b-c, c-a))
# print(ABnum)
# print(BCnum)
# print(CAnum)
# print(ABCnum)
ABData = defaultdict(int)
BCData = defaultdict(int)
CAData = defaultdict(int)
ABCData = defaultdict(int)
res = 0
for i in range(N + 1):
    ab = ABnum[i]
    bc = BCnum[i]
    ca = CAnum[i]
    abc = ABCnum[i]

    ABData[ab] += 1
    BCData[bc] += 1
    CAData[ca] += 1
    ABCData[abc] += 1

    res += ABData[ab]
    res += BCData[bc]
    res += CAData[ca]
    res -= ABCData[abc] * 2
    # print(res)

# print(ABnum)
# print(BCnum)
# print(CAnum)
# print(ABCnum)
# print("res", res, all, deb)
print(all - res)
