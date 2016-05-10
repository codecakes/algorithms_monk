def check(dct, ar2, lo, hi, count):
    c = 0
    if (dct.get(lo, -1) > -1):
        if ar2[dct[lo]] == 0:
            ar2[dct[lo]] += 1
            c += 1
    if (dct.get(hi, -1) > - 1):
        if ar2[dct[hi]] == 0:
            ar2[dct[hi]] += 1
            c += 1
    return c

def bisection(arr, K, lo, hi, count, dct, ar2):
    if lo-hi<=K:
        c = check(dct, ar2, lo, hi, count)
        K -= c
        count += c
    if lo<hi:
        mid = (lo+hi)/2
        K, count = bisection(arr, K, lo, mid, count, dct, ar2)
        K, count = bisection(arr, K, mid+1, hi, count, dct, ar2)
    return K, count

def main(arr, N, K):
    arr.sort()
    ar2 = [0] * N
    dct = {arr[i]: i for i in xrange(N)}
    lo = arr[0]
    hi = arr[N-1]
    K, count = bisection(arr, K, lo, hi, 0, dct, ar2)
    return count

if __name__ == "__main__":
    N = 3
    K = 2
    arr = [1, 5, 20]
    print main(arr, N, K)

    import os
    from cStringIO import StringIO

    with open(os.path.join(os.getcwd(), 'powerRanger_tests', "test1.txt"), 'r') as f:
        s = StringIO(f.read())

    with open( os.path.join(os.getcwd(), 'powerRanger_tests', r"test1ans.txt"), 'r' ) as f:
        ans = StringIO(f.read())

    N,K = map(int, s.readline().strip("\n").split())
    arr = map(int, s.readline().strip("\n").split())

    print main(arr, N, K), int(ans.readline().strip("\n"))