from collections import defaultdict

def calc(S: str):
    data = defaultdict(int)
    for s in S:
        data[s] += 1
    for key in data:
        if data[key] == 1:
            print(key)
            return
    print(-1)

S = input()
calc(S)
