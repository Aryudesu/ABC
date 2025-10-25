def calc(N: int, S: int, A: list[int]) -> dict[int, int|None]:
    # 値　追加した結果その値になったもの
    data = {0: None}
    for idx in range(N):
        a = A[idx]
        new_data = dict()
        for k in data:
            new_data[k] = data[k]
            if k + a in new_data:
                continue
            new_data[k + a] = idx
        data = new_data
        if S in data:
            return data
    return None


def printData(A: int, S: int, resData: list[int]|None):
    if resData is None:
        print(-1)
        return
    result = []
    tmpS = S
    while True:
        # 何を入れてその値になったかを取得
        prevIdx = resData[tmpS]
        if prevIdx is None:
            break
        result.append(prevIdx + 1)
        tmpS -= A[prevIdx]
    result.sort()
    print(len(result))
    print(*result)

N, S = map(int, input().split())
A = [int(l) for l in input().split()]
resData = calc(N, S, A)
printData(A, S, resData)
