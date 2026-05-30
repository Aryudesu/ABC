from typing import Tuple
import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10**6)

def div(a: int, b: int)->int:
    if a % b == 0:
        return a // b
    if a * b >= 0:
        return abs(a) // abs(b)
    return - (abs(a) // abs(b))

# 計算結果，次のインデックス
def calc(idx: int, T: list[str], P: set[int])->Tuple[int, int]:
    if T[idx] == "+":
        r1, i1 = calc(idx + 1, T, P)
        r2, i2 = calc(i1, T, P)
        # print("debug", r1, r2, i1, i2)
        if idx + 1 in P:
            return (r1 - r2, i2)
        return (r1 + r2, i2)
    elif T[idx] == "-":
        r1, i1 = calc(idx + 1, T, P)
        r2, i2 = calc(i1, T, P)
        # print("debug", r1, r2, i1, i2)
        if idx + 1 in P:
            return (r1 + r2, i2)
        return (r1 - r2, i2)
    elif T[idx] == "*":
        r1, i1 = calc(idx + 1, T, P)
        r2, i2 = calc(i1, T, P)
        # print("debug", r1, r2, i1, i2)
        if idx + 1 in P:
            return (div(r1, r2), i2)
        return (r1 * r2, i2)
    elif T[idx] == "/":
        r1, i1 = calc(idx + 1, T, P)
        r2, i2 = calc(i1, T, P)
        # print("debug", r1, r2, i1, i2)
        if idx + 1 in P:
            return (r1 * r2, i2)
        return (div(r1, r2), i2)
    else:
        # print("debug", idx)
        return (int(T[idx]), idx + 1)

N = int(input())
T = input().split()
K = int(input())
P = P = set(map(int, input().split())) if K > 0 else set()
res1 = calc(0, T, set())
res2 = calc(0, T, P)
print(res1[0])
print(res2[0])
