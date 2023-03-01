def is_leap_year(value):
    return True if value % 400 == 0 else False if value % 100 == 0 else True if value % 4 == 0 else False


print("YES" if is_leap_year(int(input())) else "NO")
