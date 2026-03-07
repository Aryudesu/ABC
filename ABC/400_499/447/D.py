AIdx = []
BIdx = []
CIdx = []
S = input()
for idx in range(len(S)):
    if S[idx] == "A":
        AIdx.append(idx)
    if S[idx] == "B":
        BIdx.append(idx)
    if S[idx] == "C":
        CIdx.append(idx)
result = 0
while AIdx and BIdx and CIdx:
    if AIdx[-1] > BIdx[-1]:
        AIdx.pop()
        continue
    elif BIdx[-1] > CIdx[-1]:
        BIdx.pop()
        continue
    result += 1
    # print(AIdx)
    # print(BIdx)
    # print(CIdx)
    AIdx.pop()
    BIdx.pop()
    CIdx.pop()

print(result)
