# Puchi hates to carry luggage, but unfortunately he got a job to carry the luggage of his N friends in office. Each day, one of his N friends, gives him the luggage of a particular weight to carry. You will be given the weight of luggage of each friend in the array Weight, where Weighti is the weight of luggage of ith friend carried by Puchi on ith day. It is given that all the luggages carried by Puchi are distinct in their weights.
# As Prateek assigned this job to Puchi, so for each day, he wants to know the number of days in future when Puchi will have to carry the luggage , having weight less than the weight of luggage of current day.
# Please help Prateek for the same.

# Input:
# The first line contains a single integer T, denoting the number of test cases. In each test case, the following input will be present:
# First line contains an integer N, where N represents the number of friends.
# Next N line contains N integers, where ith line contains ith integer, which represents Weighti.

# Output:
# Output exactly T lines. Each line contains N integer separated by a space, where ith integer represents the number of luggage of future, which are less than the weight of luggage of the current day.

# Constraints:

# Subtask 1:
# 1 <= T <= 30
# 1<= N <= 104
# 1<= Weighti <= 106
# Subtask 2:
# 1 <= T <= 10
# 1<= N <= 105
# 1<= Weighti <= 106


from copy import copy

def merge(arr, left_lo, left_hi, right_lo, right_hi, dct):
	startL = left_lo
	startR = right_lo
	N = left_hi-left_lo + 1 + right_hi - right_lo + 1
	aux = [0] * N
	res = []
	for i in xrange(N):

		if startL > left_hi:
			aux[i] = arr[startR]
			startR += 1
		elif startR > right_hi:
			aux[i] = arr[startL]
			startL += 1
		elif arr[startL] <= arr[startR]:
			aux[i] = arr[startL]
			startL += 1
			# print aux
		else:
			aux[i] = arr[startR]
			res.append(startL)
			startR += 1
			# print aux

	for index in res:
		for x in xrange(index, left_hi+1):
			dct[arr[x]] += 1

	for i in xrange(left_lo, right_hi+1):
		arr[i] = aux[i - left_lo]
	return


def merge_sort(arr, lo, hi, dct):
    mid = (lo+hi)/2
    if lo<=mid<hi:
		merge_sort(arr, lo, mid, dct)
		merge_sort(arr, mid+1, hi, dct)
		merge(arr, lo, mid, mid+1, hi, dct)
    return

# def binary_search(arr, lo, hi, x):
#     mid = (lo+hi)/2
#     if lo<hi:
#         if arr[mid] == x: return mid
# 	elif x < arr[mid]: return binary_search(arr, lo, mid, x)
# 	elif x > arr[mid]: return binary_search(arr, mid+1, hi, x)
#     elif lo==hi and arr[hi] == x: return hi
#     return -1

def count_inversion(arr, N, dct):
	lo = 0
	hi = N-1
	dct.update({i:0 for i in arr})
	arr2 = copy(arr)
	merge_sort(arr, lo, hi, dct)
	return ' '.join([str(dct[num]) for num in arr2])