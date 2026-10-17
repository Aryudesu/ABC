N, K = map(int, input().split())
kategori = [0] * K
for _ in range(N):
    b, d = map(int, input().split())
    kategori[b-1] = max(kategori[b-1], d)
print(sum(kategori))
