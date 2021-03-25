from collections import Counter


def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

def solve(a):
    result = 1
    ca = a.copy()
    a.sort()
    primes = []
    for i in range(len(a)):
        #print(a, result)
        if a[i] == 1:
            continue
        else:
            result *= a[i]
            if not isPrime(a[i]):
                return -1
            primes.append(a[i])
            for j in range(i+1, len(a)):
                #print(a, result, a[i], j)

                if a[j] % a[i] == 0:
                    a[j] = a[j] // a[i]
    c = Counter(primes)
    la = 1
    if result == max(ca):
        ma = min(ca)
        result = result*ma

        c[ma] +=1
    for  v in c.values():
        la*=(v+1)

    la = la-2
    #print(primes,la)

    if la != len(a):
        return -1

    return result



n = int(input())

for i in range(1, n+1):
    k = int(input())
    a = list(map(int, input().split()))

    x = solve(a)


    print(x)
