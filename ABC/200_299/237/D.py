import sys

import pypyjit

sys.setrecursionlimit(10**7)
pypyjit.set_param('max_unroll_recursion=-1')


N = int(input())
S = input()

def calc(num):
    if num >= N:
        print(num, end="")
        return
    if S[num] == "L":
        calc(num + 1)
        print(" ", end="")
        print(num, end="")
    else:
        print(num, end="")
        print(" ", end="")
        calc(num + 1)

calc(0)
print()
