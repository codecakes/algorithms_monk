from math import log

def counting_sort(arr, n):
    k = max(arr) + 1
    aux = [0] * k
    out = [0] * n

    # frequency counter
    for i in xrange(n):
        aux[arr[i]] += 1

    # running sum
    # how many elements a1 are there before element a2
    for i in xrange(1,k):
        aux[i] += aux[i-1]


    # - for each number stored as index in aux,
    # add the index in aux to the out index the arr[i] value
    # - decrement by 1 so that the next same element
    # while descending comes before to maintain order stability
    for i in xrange(n-1, -1, -1):
        aux[arr[i]] -= 1
        # print "aux[arr[%s]] num %s: %s at index of aux" %(i,arr[i], aux[arr[i]])
        out[aux[arr[i]]] = arr[i]

    return out

def counting_sort_radix(arr, n, k, p):
    # k = max(arr) + 1
    aux = [0] * k
    out = [0] * n
    e = 10**p

    # frequency counter
    for i in xrange(n):
        aux[(arr[i]/e)%10] += 1

    # running sum
    # how many elements a1 are there before element a2
    for i in xrange(1,k):
        aux[i] += aux[i-1]


    # - for each number stored as index in aux,
    # add the index in aux to the out index the arr[i] value
    # - decrement by 1 so that the next same element
    # while descending comes before to maintain order stability
    for i in xrange(n-1, -1, -1):
        aux[(arr[i]/e)%10] -= 1
        # print "aux[arr[%s]] num %s: %s at index of aux" %(i,arr[i], aux[arr[i]])
        out[aux[(arr[i]/e)%10]] = arr[i]

    for i in xrange(n):
        arr[i] = out[i]

    return

# helpful: https://www.hackerearth.com/notes/radix-sort/
def radix_sort(arr, n):
    # b = n
    # c = log(k, b)
    k = max(arr)
    w = len(str(k))
    for p in xrange(w):
        counting_sort_radix(arr, n, 10, p)
    return arr


if __name__ == "__main__":
    arr = [5,4,2,3,1]
    k = max(arr)
    assert counting_sort(arr, len(arr)) == [1,2,3,4,5]

    arr = [66, 170, 75, 802, 45, 24, 2, 90]
    res = radix_sort(arr, len(arr))
    print res
    assert res == sorted(arr)
