def calc(A: list[int], D: list[int])->int:
    result = 0
    for a, d in zip(A, D):
        if a < d:
            return -1
        result += a - d
    return result

N, M = map(int, input().split())
A = list(map(int, input().split()))
D = list(map(int, input().split()))
A.sort(reverse=True)
D.sort(reverse=True)
print(calc(A, D))
