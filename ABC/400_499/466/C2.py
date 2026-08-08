N = 3
C = [0.0, 0.7, 1.5]
l = 0
r = 0
result = 0
while l < N:
    if l >= r:
        r = l + 1
    while r < N:
        if C[r] - C[l] > 1:
            break
        r += 1
    print(l, r)
    if r > l:
        print("OK")
        result += r - l - 1
    l += 1
print(result)
