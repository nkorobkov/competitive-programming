from collections import Counter

def solve(n):
	r = []
	if n%2 == 0: 
		if (n-2) % 4 == 0:
			r = [2,(n-2)//2,(n-2)//2]
		else:
			r = [n//4,n//4,n//2]
	else:
		r = [1, (n-1)//2,(n-1)//2]

	return r

def solve2(n, k):

	overk = k-3
	r = [1]*overk
	nn = n -overk
	r = r + solve(nn)
	return ' '.join(map(str, r))


cases = int(input())
for ii in range(cases):
	m,n = list(map(int, input().split()))
	print(solve2(m, n))


