from sortedcontainers import SortedList

def calc(N: int, M: int, K: int, H: SortedList[int], B: SortedList[int]):
    idx = M - 1
    count = 0
    # 各頭パーツに対して探索
    for n in range(N):
        if idx < 0:
            break
        if H[- n - 1] > B[idx]:
            continue
        else:
            count += 1
        idx -= 1
    return count >= K


N, M, K = map(int, input().split())
H = SortedList(map(int, input().split()))
B = SortedList(map(int, input().split()))
print("Yes" if calc(N, M, K, H, B) else "No")
