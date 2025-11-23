def calc1(N: int, A: list[int]):
    s = sum(A)
    if s % N != 0:
        print(-1)
        return
    r = s // N
    data = dict()
    

N = int(input())
A = list(map(int, input().split()))
