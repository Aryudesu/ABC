from heapq import heappop, heappush

def calc(N: int, A: list[int])->int:
    s = sum(A)
    if s % N:
        return -1
    num = s // N
    result = 0
    # 移動させるケーキの個数
    s = 0
    for i in range(N):
        a = A[i]
        # 目標値に未満の時
        if a < num:
            s -= num - a
        # 目標値以上のとき
        else:
            s += a - num
        # 1個右に移動
        result += abs(s)
    return result

N = int(input())
A = list(map(int, input().split()))
print(calc(N, A))
