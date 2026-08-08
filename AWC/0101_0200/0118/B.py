N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
result = 0
while A:
    a = A.pop()
    if A and abs(A[-1] - a) <= K:
        result += 1
        A.pop()
print(result)
