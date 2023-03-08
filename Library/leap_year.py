def is_leap_year(y):
    return not(y % 4) and (y % 100) or not (y % 400)


print("YES" if is_leap_year(int(input())) else "NO")
