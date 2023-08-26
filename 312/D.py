S = input()
data = dict()
data[0] = 1
mod = 998244353
for s in S:
    new_data = dict()
    for key in data:
        if s == ")":
            if key - 1 >= 0:
                tmp = data.get(key, 0)
                tmp2 = new_data.get(key-1, 0)
                new_data[key - 1] = (tmp + tmp2) % mod
        elif s == "(":
            tmp = data.get(key, 0)
            tmp2 = new_data.get(key+1, 0)
            new_data[key + 1] = (tmp + tmp2) % mod
        elif s == "?":
            tmp = data.get(key, 0)
            if key - 1 >= 0:
                tmp2 = new_data.get(key-1, 0)
                new_data[key - 1] = (tmp + tmp2) % mod
            tmp2 = new_data.get(key+1, 0)
            new_data[key + 1] = (tmp + tmp2) % mod
    data = new_data
    # print(data)
result = data.get(0, 0)
print(result)
