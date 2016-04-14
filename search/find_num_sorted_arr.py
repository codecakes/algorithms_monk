def findNum(arr, N, x):
    lefti = mid = 0
    righti = N-1
    while lefti <= righti:
        mid = (lefti+righti)/2
        if arr[mid] == x: return mid
        if x > arr[mid]: lefti = mid + 1
        elif x < arr[mid]: righti = mid - 1
        # print lefti, righti
    return -1

if __name__ == "__main__":
    arr = [2,3,46,1,5,90]
    arr.sort()
    print findNum(arr, len(arr), 2)
    print findNum(arr, len(arr), 90)