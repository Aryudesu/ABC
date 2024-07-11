N, A = [int(l) for l in input().split()]
T = [int(l) for l in input().split()]
time = -1
for t in T:
    if time == -1:
        time = t + A
    elif time > t:
        time += A
    else:
        time = t + A
    print(time)
