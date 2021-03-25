

n, k = map(int, input().split())

for al in range(1, n+1):
    if n%al:
        continue

    bet = n//al

    if bet >= k:
        continue
    x = al*k + bet
    break

print(x)

