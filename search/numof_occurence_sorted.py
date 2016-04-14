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

def numOccur(arr, N, x):
    left_index = firstOccur(arr, N, x)
    right_index = lastOccur(arr, N, x)
    # print left_index, right_index
    return right_index - left_index + 1 if arr[left_index] == x and arr[right_index] == x else -1



if __name__ == "__main__":
    arr = [2,2, 2, 3,46,1,5,90, 90, 90]
    arr.sort()
    print firstOccur(arr, len(arr), 2)
    print lastOccur(arr, len(arr), 2)
    print numOccur(arr, len(arr), 2)

    print firstOccur(arr, len(arr), 90)
    print lastOccur(arr, len(arr), 90)
    print numOccur(arr, len(arr), 90)
