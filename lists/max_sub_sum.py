def find_subsequence(arr, i, n):
    print "i is %s" %i,
    if i < n:
        print "arr[i]=%s" %(arr[i])
        return max(arr[i] + find_subsequence(arr, i+2, n), arr[i+1] if i+1 < n else 0 + find_subsequence(arr, i+3, n))
    return 0

# assert find_subsequence([5, 8, 9, 15, 19], 0, 5) == 33
# assert find_subsequence([-155, 500, 600, 15, 190], 0, 5) == 635
print find_subsequence([155, 500, 0, 15, 190], 0, 5)
