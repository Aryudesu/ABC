N = int(input())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
stack = []
for i in range(N):
    a, c = A[i], C[i]
    maxNum = 0
    for page, gold in stack:
        if page < a:
            if maxNum < gold:
                maxNum = gold
    stack.append((a, maxNum + c))
print(sum(C) - max(m for _, m in stack))
