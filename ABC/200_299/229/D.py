def calc(S, K):
    data = []
    count = 0
    for s in S:
        if s == "X":
            count += 1
        else:
            data.append(count)
            count = 0
    data.append(count)
    if len(data) <= K + 1:
        return len(S)
    result = 0
    num = 0
    for k in range(K + 1):
        num += data[k]
    result = num
    for k in range(K + 1, len(data)):
        num -= data[k - K - 1]
        num += data[k]
        if result < num:
            result = num
    return result + K


S = input()
K = int(input())
print(calc(S, K))
