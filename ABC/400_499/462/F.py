def calc(S: str, K: int)->int:
    dp = list(range(1, len(S) + 1))

T = int(input())
result = []
for _ in range(T):
    S = input()
    K = int(input())
x