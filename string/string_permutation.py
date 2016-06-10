from array import array

# not working
def string_permute_iterative(ar, hi):
    lo = index = 0
    stack = [(lo, index)]
    while lo<=index<=hi:
        if lo == hi:
            while stack:
                lo, index = stack.pop()
                ar[lo], ar[index] = ar[index], ar[lo]
                if lo == index:
                    print ar[:]
                elif index+1 <= hi:
                    ar[index], ar[lo] = ar[lo], ar[index]
                    stack.append((lo, index+1))
            else:
                break
        else:
            for index in xrange(lo, hi+1):
                ar[index], ar[lo] = ar[lo], ar[index]
                stack.append((lo, index))
            lo += 1



def string_permute(ar, lo, hi, result):
    # this is beautiful
    if lo == hi:
        # print ar
        result.append(ar[:])
    else:
        for index in xrange(lo, hi+1):
            ar[index], ar[lo] = ar[lo], ar[index]
            string_permute(ar, lo+1, hi, result)
            ar[index], ar[lo] = ar[lo], ar[index]
    return result


if __name__ == "__main__":
    f = array('c', '123')
    result = []
    # string_permute(f.tolist(), 0, len(f)-1, result)
    # print result
    string_permute_iterative(f.tolist(), len(f)-1)
    # string_permute_iter(f.tolist(), 0, len(f)-1)  # this is useless