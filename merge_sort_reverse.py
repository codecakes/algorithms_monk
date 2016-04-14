def merge(arr, left_lo, left_hi, right_lo, right_hi):
	startL = left_lo
	startR = right_lo
	N = left_hi-left_lo + 1 + right_hi - right_lo + 1
	aux = [0] * N
	for i in xrange(N):
		if startL > left_hi:
			aux[i] = arr[startR]
			startR += 1
		elif startR > right_hi:
			aux[i] = arr[startL]
			startL += 1
		elif arr[startL] > arr[startR]:
			aux[i] = arr[startL]
			startL += 1
		else:
			aux[i] = arr[startR]
			startR += 1

	for i in xrange(left_lo, right_hi+1):
		arr[i] = aux[i - left_lo]
	return

def merge_sort(arr, lo, hi):
	mid = (lo+hi)/2
	if lo<=mid<hi:
		merge_sort(arr, lo, mid)
		merge_sort(arr, mid+1, hi)
		merge(arr, lo, mid, mid+1, hi)
	return