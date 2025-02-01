def get_maxindex(arr):
    result = set()
    max_num = 0
    for i in range(len(arr)):
        if arr[i] > max_num:
            result = {i}
            max_num = arr[i]
        elif arr[i] == arr[result]:
            result.add(i)
    return result

N, X = [int(l) for l in input().split()]
# dp[カロリー] = [ビタミン1, ビタミン2, ビタミン3]
dp = {0: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}
result = 0
for x in range(X):
    new_dp = dict()
    v, a, c = [int(l) for l in input().split()]
    for k, v in dp:
        vtmp = dp.get(k, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        tmp = [[vtmp[0][i] for i in range(3)], [vtmp[1][i] for i in range(3)], [vtmp[2][i] for i in range(3)]]

        newvtmp = new_dp.get(k + c, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        newtmp = [[newvtmp[0][i] for i in range(3)], [newvtmp[1][i] for i in range(3)], [newvtmp[2][i] for i in range(3)]]
        for i in range(3):
            tmp[i][v - 1] += a
        for i in range(3):
            if tmp[i][0] <= tmp[i][1] and tmp[i][0] <= tmp[i][2]:
                if newtmp[0][0] <= tmp[i][0]:
                    newtmp[0] = []
    dp = new_dp
