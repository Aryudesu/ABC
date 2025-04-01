from collections import defaultdict


def calc(N, A):
    data = defaultdict(list)
    for idx in range(2 * N):
        a = A[idx]
        data[a].append(idx)
    memo = set()
    result = 0
    for num in range(1, N + 1):
        i1, i2 = data[num]
        if abs(i1 - i2) == 1:
            continue
        if i1 - 1 >= 0:
            num1 = A[i1 - 1]
            j1, j2 = data[num1]
            if abs(j1 - j2) == 1:
                continue
            if abs(i1 - j1) == 1 and abs(i2 - j2) == 1 and not (num, num1) in memo:
                result += 1
                memo.add((num, num1))
                memo.add((num1, num))
                # print(num, num1)
        if i1 + 1 < N:
            num1 = A[i1 + 1]
            j1, j2 = data[num1]
            if abs(j1 - j2) == 1:
                continue
            if abs(i1 - j1) == 1 and abs(i2 - j2) == 1 and not (num, num1) in memo:
                result += 1
                memo.add((num, num1))
                memo.add((num1, num))
    #             print(num, num1)
    # print(memo)
    return result


T = int(input())
result = []
for t in range(T):
    N = int(input())
    A = [int(l) for l in input().split()]
    result.append(calc(N, A))
for r in result:
    print(r)
