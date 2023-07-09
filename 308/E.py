N = int(input())
A = [int(l) for l in input().split()]
S = input()
M = dict()
ME = dict()
MEX = dict()
for idx in range(N):
    s = S[idx]
    if s == "M":
        tmp = M.get(A[idx], 0)
        M[A[idx]] = tmp + 1
    elif s == "E":
        for k in M:
            if k == 0:
                tmp = ME.get((k, A[idx]), 0)
                ME[(k, A[idx])] = tmp + M[k]
            elif k == 1:
                if A[idx] == 0:
                    tmp = ME.get((0, 1), 0)
                    ME[(0, 1)] = tmp + M[k]
                else:
                    tmp = ME.get((k, A[idx]), 0)
                    ME[(k, A[idx])] = tmp + M[k]
            else:
                tmp = ME.get((A[idx], k), 0)
                ME[(A[idx], k)] = tmp + M[k]
    elif s == "X":
        for k in ME:
            if k == (0, 0):
                tmp = MEX.get((0, 0, A[idx]), 0)
                MEX[(0, 0, A[idx])] = tmp + ME[k]
            elif k == (0, 1):
                if A[idx] == 0:
                    tmp = MEX.get((0, 0, 1), 0)
                    MEX[(0, 0, 1)] = tmp + ME[k]
                else:
                    tmp = MEX.get((0, 1, A[idx]), 0)
                    MEX[(0, 1, A[idx])] = tmp + ME[k]
            elif k == (0, 2):
                if A[idx] == 0:
                    tmp = MEX.get((0, 0, 2), 0)
                    MEX[(0, 0, 2)] = tmp + ME[k]
                elif A[idx] == 1:
                    tmp = MEX.get((0, 1, 2), 0)
                    MEX[(0, 1, 2)] = tmp + ME[k]
                elif A[idx] == 2:
                    tmp = MEX.get((0, 2, 2), 0)
                    MEX[(0, 2, 2)] = tmp + ME[k]
            elif k == (1, 1):
                if A[idx] == 0:
                    tmp = MEX.get((0, 1, 1), 0)
                    MEX[(0, 1, 1)] = tmp + ME[k]
            elif k == (1, 2):
                if A[idx] == 0:
                    tmp = MEX.get((0, 1, 2), 0)
                    MEX[(0, 1, 2)] = tmp + ME[k]
            elif k == (2, 2):
                if A[idx] == 0:
                    tmp = MEX.get((0, 2, 2), 0)
                    MEX[(0, 2, 2)] = tmp + ME[k]
result = 0
for key in MEX:
    if key == (0, 0, 0):
        result += 1 * MEX[key]
    elif key == (0, 0, 1):
        result += 2 * MEX[key]
    elif key == (0, 0, 2):
        result += 1 * MEX[key]
    elif key == (0, 1, 1):
        result += 2 * MEX[key]
    elif key == (0, 1, 2):
        result += 3 * MEX[key]
    elif key == (0, 2, 2):
        result += 1 * MEX[key]
print(result)
