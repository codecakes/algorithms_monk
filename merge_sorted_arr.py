# In the previous problem Chandu bought some unsorted arrays and sorted them (in non-increasing order). Now, he has many sorted arrays to give to his girlfriend. But, the number of sorted arrays are very large so Chandu decided to merge two sorted arrays into one sorted array. But he is too lazy to do that. So, he asked your help to merge the two sorted arrays into one sorted array (in non-increasing order).

# Input:
# First line contains an integer T, denoting the number of test cases.
# First line of each test case contains two space separated integers N and M, denoting the size of the two sorted arrays.
# Second line of each test case contains N space separated integers, denoting the first sorted array A.
# Third line of each test case contains M space separated integers, denoting the second array B.

# Output:
# For each test case, print (N + M) space separated integer representing the merged array.

# Constraints:
# 1 <= T <= 100
# 1 <= N, M <= 5*104
# 0 <= Ai, Bi <= 109


def merge(arr1, N1, arr2, N2):
	N = N1+N2
	aux = [0] * N
	mid = N1-1
	end = N2-1
	startL = startR = 0

	for i in xrange(N):
		if startR>end:
			aux[i] = str(arr1[startL])
			startL += 1
		elif startL > mid:
			aux[i] = str(arr2[startR])
			startR += 1
		elif arr1[startL] > arr2[startR]:
			aux[i] = str(arr1[startL])
			startL += 1
		else:
			aux[i] = str(arr2[startR])
			startR += 1

	return aux