import functools
import math
from functools import lru_cache

MOD = 10**9 + 7
n, l, r = tuple(map(int, input().split()))

ll = l % 3
r = r - l + ll
l = ll

div3 = r // 3 + int(l == 0)
div2 = r // 3 + int(r % 3 == 2)
div1 = r // 3 + int(r % 3 >= 1) - int(l % 3 == 2)

d = [(div3, div1,div2)]

while (len(d) < n):
    next0 = d[-1][0]*div3 + d[-1][1]*div2 + d[-1][2]*div1
    next1 = d[-1][0] * div1 + d[-1][1] * div3 + d[-1][2] * div2
    next2 = d[-1][0] * div2 + d[-1][1] * div1 + d[-1][2] * div3

    d.append((next0%MOD,next1%MOD,next2%MOD))

print(d[-1][0])
# def soft_m(a, b):
#     if a == -1 or b == -1:
#         return 0
#     if a == 0 and b == 0:
#         return 0
#     else:
#         a = max(a, 1)
#         b = max(b, 1)
#
#     return a * b
#
#
# @lru_cache(maxsize=None)
# def comb(n, k):
#     if k > n - k:
#         return comb(n, n - k)
#     if k == 0:
#         return 1
#     up = functools.reduce(lambda x, y: x * y, list(range(n-k + 1, n+1)))
#     return up / math.factorial(k)
# @lru_cache(maxsize=None)
# def kwr(n, k):
#     if n == 0:
#         return 0
#     return comb(n+k-1, k) % MOD
#
# @lru_cache(maxsize=None)
# def sets_of3(distinct, size):
#     return kwr(distinct, size)
#
# @lru_cache(maxsize=None)
# def sets_of_12pairs(ones, twos, size):
#     if size %2:
#         return -1
#
#     if size == 0:
#         return 0
#     return (kwr(size//2, ones) * kwr(size//2, twos))%MOD
# @lru_cache(maxsize=None)
# def sets_of_triplets(distinct, size):
#     if size %3:
#         return -1
#
#     if size == 0:
#         return 0
#     return kwr(size, distinct)
#
# @lru_cache(maxsize=None)
# def sets_of12(ones, twos, size):
#     sum = 0
#     if size == 0:
#         return 0
#
#
#     for i in range(0,size+2, 2):
#         sot = sets_of_12pairs(ones, twos, i)
#         sum += soft_m(sot, sets_of_triplets(ones, size-i))
#         sum += soft_m(sot, sets_of_triplets(twos, size-i))
#         sum = sum%MOD
#
#     return sum
#
# def sets(ones, twos, trees, n):
#     sum = 0
#     for i in range(n+1):
#
#         a = sets_of12(ones, twos, i)
#         b = sets_of3(trees, n-i)
#
#         print(i , 'in sets of 12', sets_of12(ones, twos, i), sets_of3(trees, n-i))
#         if a == 0 and b == 0:
#             continue
#         else:
#             a = max(a, 1)
#             b = max(b, 1)
#         sum += a*b
#     return sum%MOD
#
#
# print(sets(div1, div2, div3, n))