from sortedcontainers import SortedSet
from collections import defaultdict

def calc(N: int, M: int, R: list[int])->int:
    dataR = []
    for i in range(N):
        dataR.append((R[i], i))
    dataR.sort(reverse=True)
    persons = set(range(N))

    pairs = defaultdict(SortedSet)
    for _ in range(M):
        u, v = map(int, input().split())
        pairs[u-1].add(v-1)
        pairs[v-1].add(u-1)

    for index in range(N):
        _, person = dataR[index]
        if person in persons:
            persons.discard(person)
            if len(pairs[person]) > 0:
                pair = None
                while pairs[person]:
                    pair = pairs[person][0]
                    if pair in persons:
                        break
                    pairs[person].discard(pair)
                pairs[person].discard(0)
                persons.discard(pair)
                if person == 0:
                    return pair
                if pair == 0:
                    return person
    raise Exception()

N, M = map(int, input().split())
R = list(map(int, input().split()))
print(calc(N, M, R) + 1)
