from typing import Tuple
def calc(N: int, K: int, data: list[Tuple[int, int]])->int:
    data.sort()    
    for i in range(N):
        s, n = data[i]
        if n == K:
            return i
    raise ValueError()


N, K = map(int, input().split())
S = list(map(int, input().split()))
data= []
for i in range(N):
    data.append((S[i], i + 1))
print(calc(N, K, data))
