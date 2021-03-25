
import math

def primeFactors(n):
    # Print the number of two's that divide n
    b =  []
    c = 0
    while n % 2 == 0:
        c+=1
        n = n / 2
    b.append((c*2, 2, c))
    c = 0
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        c = 0
        while n % i == 0:
            c+=1
            n = n / i
        b.append((i*c, i, c))

            # Condition if n is a prime
    # number greater than 2
    if n > 2:

        b.append((n, n, 1))

    return sorted(b, reverse=True)

def count_ss_in_1_n(s, n, mult):
    if s > n:
        return 0

    res = n//s

    res += count_ss_in_1_n(s*mult, n, mult)
    return res

def solve(n, b):


    pf = primeFactors(b)
    mpf = max(pf)
    maxbf = mpf[1]
    countmbf = mpf[2]
    ans = int(count_ss_in_1_n(maxbf, n, maxbf)//countmbf)
    i = 1
    try:
        while pf[i][1]*2 > maxbf:
            if pf[i][2] > 0:



                ans = min(int(count_ss_in_1_n(pf[i][1], n, pf[i][1])//pf[i][2]),ans)
                i+=1
            else:
                break
    except IndexError:
        pass

    return ans


if __name__ == '__main__':
    n, b = list(map(int, input().split()))

    print(solve(n, b))