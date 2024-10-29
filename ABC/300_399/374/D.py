from itertools import permutations


def calc(N, S, T, ABCD, v):
    result = 10 ** 10
    for a in range(1 << N):
        data = []
        tmp = a
        count = 0
        ptx, pty = 0, 0
        tmp_result = 0
        # Bit全探索用に配列作成
        for i in range(N):
            if tmp & 1:
                data.append(1)
            else:
                data.append(0)
            count += 1
            tmp >>= 1
        for n in range(N):
            if data[n] == 1:
                tmp_result += ((ptx - ABCD[v[n]][0]) ** 2 + (pty - ABCD[v[n]][1]) ** 2) ** 0.5 / S
                tmp_result += ((ABCD[v[n]][2] - ABCD[v[n]][0]) ** 2 + (ABCD[v[n]][3] - ABCD[v[n]][1]) ** 2) ** 0.5 / T
                ptx, pty = ABCD[v[n]][2], ABCD[v[n]][3]
            else:
                tmp_result += ((ptx - ABCD[v[n]][2]) ** 2 + (pty - ABCD[v[n]][3]) ** 2) ** 0.5 / S
                tmp_result += ((ABCD[v[n]][2] - ABCD[v[n]][0]) ** 2 + (ABCD[v[n]][3] - ABCD[v[n]][1]) ** 2) ** 0.5 / T
                ptx, pty = ABCD[v[n]][0], ABCD[v[n]][1]
        result = min([result, tmp_result])
    return result


N, S, T = [int(l) for l in input().split()]
ABCD = []
for n in range(N):
    ABCD.append([int(l) for l in input().split()])

result = 10 ** 10
for v in permutations(range(N)):
    result = min([calc(N, S, T, ABCD, v), result])
print(result)
