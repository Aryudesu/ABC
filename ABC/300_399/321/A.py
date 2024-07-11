def calc(N):
    for n in range(len(N) - 1):
        if int(N[n]) <= int(N[n + 1]):
            return False
    return True


print("Yes" if calc(list(input())) else "No")
