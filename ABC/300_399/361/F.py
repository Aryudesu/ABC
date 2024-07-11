def intLog_bisect(N, a):
    """log_a Nの整数部分"""
    L = -1
    R = 60
    while R - L > 1:
        mid = (R + L) // 2
        if a ** mid < N:
            L = mid
        else:
            R = mid
    return L

N = int(input())
result = 0
for i in range(2, N):
    tmp = intLog_bisect(N, i)
    if tmp == -1 or tmp - 1 == 0:
        break
    result += tmp - 1
print(result + 1)

# data = set()
# for a in range(2, N):
#     if a * a > N:
#         break
#     if a in data:
#         continue
#     for b in range(2, N):
#         tmp = a ** b
#         if tmp > N:
#             break
#         data.add(tmp)

# print(len(data) + 1)
