Q = int(input())
minusIdx = -1
data = 0
memo = []
for q in range(Q):
    query = input().split()
    if query[0] == "1":
        if query[1] == "(":
            data += 1
            memo.append(1)
        elif query[1] == ")":
            data += -1
            memo.append(-1)
        else:
            raise Exception()
    else:
        tmp = memo.pop()
        data -= tmp
        if len(memo) < minusIdx:
            minusIdx = -1
    if data < 0 and minusIdx < 0:
        minusIdx = len(memo)
    if data == 0 and minusIdx < 0:
        print("Yes")
    else:
        print("No")
    # print(memo, minusIdx, data)
