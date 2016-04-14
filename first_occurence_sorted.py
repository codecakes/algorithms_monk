def firstOccur(arr, N, x):
    lastmid = lefti = mid = 0
    righti = N-1
    while lefti<righti:
        mid = (lefti+righti)/2
        if lastmid == mid:
            mid += 1
        if mid == righti:
            return righti
        if arr[mid] >= x:
            righti = mid
        else:
            lefti = mid
        lastmid = mid
        # print lefti, righti
    return righti if arr[righti] == x else -1

if __name__ == "__main__":
    arr = [2,2, 2, 3,46,1,5,90]
    arr.sort()
    print firstOccur(arr, len(arr), 2)
    print firstOccur(arr, len(arr), 90)
