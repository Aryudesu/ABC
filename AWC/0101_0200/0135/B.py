from fractions import Fraction

N = int(input())
data = []
for n in range(N):
    p, s = map(int, input().split())
    data.append((Fraction(s, p), -n))
data.sort()
# print(data)
print(-data[-1][1] + 1)
