def calc(S, T):
    sdat = tuple(list(S))
    goal = tuple(list(T))
    if sdat == goal:
        return True
    for idx in range(len(S) - 1):
        s_data = list(S)
        s_data[idx], s_data[idx + 1] = s_data[idx + 1], s_data[idx]
        data = tuple(s_data)
        if data == goal:
            return True
    return False


S = input()
T = input()
print("Yes" if calc(S, T) else "No")
