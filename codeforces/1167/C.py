n, m = list(map(int, input().split()))
import sys
sys.setrecursionlimit(5 * 10**5)

from collections import defaultdict


def resolve(i):
    if i in index:
        if index[i] == i:
            return i
        return resolve(index[i])

    return -1


index = {}
for i in range(m):
    k = list(map(int, input().split()))
    if k[0] == 0:
        continue
    else:
        k = k[1:]

    if k[0] not in index:

        group_head = k[0]
    else:
        group_head = resolve(k[0])

    index[k[0]] = group_head

    f = False
    for s in k[1:]:
        if f:
            if resolve(s) == s:
                index[group_head] = s
                group_head = s
            else:

                index[s] = group_head
            continue

        if s not in index:
            index[s] = group_head
        else:
            index[group_head] = index[s]
            group_head = resolve(s)
            f = True

heads = defaultdict(int)
for i in range(0, n):
    h = resolve(i + 1)
    if h > 0:
        index[i + 1] = h
    else:
        index[i + 1] = i + 1
    heads[index[i + 1]] += 1

ans = []
for i in range(n):
    ans.append(heads[index[i + 1]])

print(' '.join(list(map(str, ans))))
