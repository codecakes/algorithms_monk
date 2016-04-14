def lastOccur(arr, N, x):
    lastmid = lefti = mid = 0
    righti = N-1
    while lefti<righti:
        mid = (lefti+righti)/2
        if lastmid == mid:
            mid += 1
        if mid == lefti:
            return lefti
        if arr[mid] <= x:
            lefti = mid
        else:
            righti = mid
        lastmid = mid
        # print lefti, righti
    return lefti if arr[lefti] == x else -1

if __name__ == "__main__":
    arr = [2,2, 2, 3,46,1,5,90, 90, 90]
    arr.sort()
    print lastOccur(arr, len(arr), 2)
    print lastOccur(arr, len(arr), 90)
    arr = [2,2, 2, 3,46,1,5,90]
    arr.sort()
    print lastOccur(arr, len(arr), 90)