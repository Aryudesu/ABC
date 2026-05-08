def calc(N: int)->int:
    pass

result = []
T = int(input())
for _ in range(T):
    N = int(input())
    result.append(calc(N))

for r in result:
    print(r)
