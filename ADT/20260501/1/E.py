from typing import Tuple

def num2YX(N: int, num: int)->Tuple[int, int]:
    return (num//N, num%N)

def calc(N: int, T: int, A: list[int])->int:
    dataH = [0] * N
    dataW = [0] * N
    dataL = 0
    dataR = 0
    for t in range(T):
        a = A[t] - 1
        y, x = num2YX(N, a)
        dataH[y] += 1
        dataW[x] += 1
        if y == x:
            dataL += 1
        if (N-1 - y) == x:
            dataR += 1
        if dataH[y] == N:
            return t + 1
        if dataW[x] == N:
            return t + 1
        if dataL == N:
            return t + 1
        if dataR == N:
            return t + 1
    return -1

N, T = map(int, input().split())
A = list(map(int, input().split()))
print(calc(N, T, A))
