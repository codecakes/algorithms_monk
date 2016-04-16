from collections import deque
from math import log, ceil
from numpy import array, int64

# def split_arr(ar, br, lo, hi, N):
# 	if lo<hi:
# 		mid = (lo+hi)/2
# 		# O(lgN)
# 		a = split_arr(ar, br, lo, mid, N)
# 		b = split_arr(ar, br, mid+1, hi, N)
# 		return a if a>b else (b if b > -1 else 0)
# 	else:
# 		maximus = float('-inf')
# 		b_num = br[lo]
# 		# O(N)
# 		for index in xrange(N):
# 			if lo >= index and b_num >= ar[index]:
# 				res = lo - index
# 				if res > maximus:
# 					maximus = res
# 			elif b_num < ar[index] and lo <= index:
# 				return maximus
# 		return maximus

# bad solution
def split_arr2(ar, b_index, b_num, lo, hi, N):
	s = deque(array([], dtype=int64), int(ceil(log(N, 2)))**2)
	s.appendleft([lo, hi])
	res = 0
	maximus = float('-inf')
	while s:
		lo, hi = s.pop()
		if lo<hi:
			mid = (lo+hi)/2
			s.append([lo, mid])
			s.append([mid+1, hi])
		else:
			if b_index >= lo and b_num >= ar[lo]:
				res = b_index - lo
				if res > maximus:
					maximus = res
			elif b_num < ar[lo] and b_index <= lo:
				return maximus
	return maximus

# the good mysterious solution
def split_arr1(ar, br, lo, hi, N):
	s = deque(array([], dtype=int64), int(ceil(log(N, 2)))**2)
	s.appendleft([lo, hi])
	maximus = float('-inf')
	res = 0
	# O(lgN)
	while s:
		lo, hi = s.pop()
		if lo<hi:
			mid = (lo+hi)/2
			s.append([lo, mid])
			s.append([mid+1, hi])
		else:
			b_num = br[lo]
			# O(lgN)
			if b_num >= ar[lo]:
				t = 0
				while t <= lo:
					if b_num >= ar[t]:
						res = lo - t
						if res > maximus:
							maximus = res
					t += 1
			# res = split_arr2(ar, lo, b_num, 0, N-1, N)
			# if res > maximus: maximus = res
	return maximus if maximus > -1 else 0

def split_arr(ar, br, N):
	maximus = float('-inf')
	res = 0
	# O(NlgN)
	for i in xrange(N):
		# print "for i=%s"%i
		a_num = ar[i]
		lo, hi = 0, N-1
		while lo <= hi:
			mid = (lo+hi)/2
			b_num = br[mid]
			if b_num >= a_num:
				res = mid - i
				if res > maximus:
					# assert mid >= i # solution would break for the clause j >= i
					# print "bi,mid=%s ai=%s"%(mid, i)
					maximus = res
				lo = mid + 1
			else:
				hi = mid - 1
	# print maximus if maximus > -1 else 0
	return maximus if maximus > -1 else 0

if __name__ == "__main__":
	ar = [7, 7, 3, 3, 3, 2, 2, 2, 1]
	br = [8, 8, 7, 7, 5, 5, 4, 3, 2]
	N = 9
	# print split_arr(ar, br, N)
	assert split_arr(ar, br, N) == 5


	ar = [6, 5, 4, 4, 4, 4]
	br = [2, 2, 2, 2, 2, 2]
	N = 6
	assert split_arr(ar, br, N) == 0

	ar = [10, 9, 9, 2, 1]
	br = [10, 9, 7, 5, 1]
	N = 5
	assert split_arr(ar, br, N) == 0

	import os
	from cStringIO import StringIO

	with open(os.path.join(os.getcwd(), 'max_index_tests', "test1.txt"), 'r') as f:
		s = StringIO(f.read())


	with open( os.path.join(os.getcwd(), 'max_index_tests', r"test1ans.txt"), 'r' ) as f:
		ans = StringIO(f.read())

	T = int(s.readline().strip("\n"))

	for _ in xrange(T):
		N = int(s.readline().strip("\n"))
		ar = map(int, s.readline().strip("\n").split())
		br = map(int, s.readline().strip("\n").split())
		print split_arr(ar, br, N)
