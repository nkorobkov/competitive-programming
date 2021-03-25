
def f(n, d):

    p = []
    to_resolve = 1

    for i in range(n):
        candidates = d[to_resolve]
        if candidates[1] in d[candidates[0]]:
            to_resolve = candidates[0]
        else:
            to_resolve = candidates[1]
        p.append(to_resolve)

    return p