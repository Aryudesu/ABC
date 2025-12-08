Q = int(input())
stack = list()
result = []
for _ in range(Q):
    S = input()
    if S == "READ":
        result.append(stack.pop())
    else:
        stack.append(S)
for r in result:
    print(r)
