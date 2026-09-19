N, Q, M = map(int, input().split())
A = list(map(int, input().split()))
S = list(input())
result = []
for _ in range(M):
    op = input().split()
    match op[0]:
        case "1":
            p, c = int(op[1]), op[2]
            S[p-1] = c
        case "2":
            pointer = 0
            score = 0
            memo = set()
            for q in range(Q):
                match S[q]:
                    case "L":
                        pointer = max(pointer - 1, 0)
                    case "R":
                        pointer = min(pointer + 1, N - 1)
                    case "P":
                        if pointer not in memo:
                            score += A[pointer]
                            memo.add(pointer)
                    case "B":
                        pointer = 0
                    case _:
                        raise ValueError()
            result.append(score)
        case _:
            raise ValueError()
print(*result, sep="\n")
