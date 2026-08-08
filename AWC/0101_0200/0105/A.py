N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = input()
result = 0
idx = 0
for s in S:
    match s:
        case "L":
            idx = (idx - 1) % N
            result += A[idx]
        case "R":
            idx = (idx + 1) % N
            result += A[idx]
        case _:
            raise ValueError()
print(result)
