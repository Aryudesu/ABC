N, R, C = [int(l) for l in input().split()]
S = list(input())
data = set()
data.add((0, 0))
t_R = 0
t_C = 0
p_R = R
p_C = C
result = ""
for idx in range(N):
    s = S[idx]
    if s == "N":
        t_R += 1
        p_R += 1
    elif s == "W":
        t_C += 1
        p_C += 1
    elif s == "S":
        t_R -= 1
        p_R -= 1
    elif s == "E":
        t_C -= 1
        p_C -= 1
    data.add((t_R, t_C))
    # print(data, p_R, p_C)
    if (p_R, p_C) in data:
        result += "1"
    else:
        result += "0"
print(result)
