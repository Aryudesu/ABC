import sys

N = list(input())
N.sort()
print("Yes" if "".join(N) == "122333" else "No")
