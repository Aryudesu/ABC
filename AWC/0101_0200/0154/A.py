from fractions import Fraction

N, P = map(int, input().split())
data = []
for n in range(N):
    x, v = map(int, input().split())
    if x != P:
        data.append(v/abs(P - x))
print(sum(data))
