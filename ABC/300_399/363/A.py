R = int(input())
if 1 <= R <= 99:
    print(100 - R)
elif 100 <= R <= 199:
    print(200 - R)
elif 200 <= R <= 299:
    print(300 - R)
elif 300 <= R <= 399:
    print(400 - R)
else:
    raise Exception()
