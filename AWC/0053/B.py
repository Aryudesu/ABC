def calcDif(X: list[int], mid: int)->int:
    result = 0
    for x in X:
        result += abs(x - mid)
    return result

N = int(input())
X = list(map(int, input().split()))
X.sort()
mid = N//2
result = calcDif(X, X[mid])
if N % 2 == 0:
    result = min(calcDif(X, X[mid-1]), result)
print(result)
