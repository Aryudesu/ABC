N = 25
tmp = 1
for n in range(N):
    tmp = (tmp * N) % 100
print(tmp)
