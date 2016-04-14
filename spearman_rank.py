from collections import OrderedDict, deque
from numpy import mean

def rank_order(arr):
    '''
    rank first to last the sorted array in desc order.
    Used for calculating Spearman's rank coefficient'''
    #sort in desc order
    d = OrderedDict()
    s = deque([], len(arr))
    rank = OrderedDict()

    #O(NlgN)
    arr = sorted(arr, reverse=True)
    #store the frequency
    for each in arr: d[each] = d.get(each,0) +1  #O(N)
    #store its index as well
    arr = [(k[0],k[1],index) for index, k in enumerate(d.iteritems())]  #O(k<=N)
    #print arr

    #rank counting max to min w.r.t freq
    index = 1
    #O(k<=N)
    for e in arr:
        #O(m<=N) | if m==N then there is only 1 iteration
        rank[e[0]] = mean(map(lambda x: x+index, xrange(e[1])))
        index += e[1]
    #O(k*m) <= O(N)
    del s
    return rank

def squared_d(xarr, yarr, n):
    xrank = rank_order(xarr)
    yrank = rank_order(yarr)
    return sum([(xrank[xarr[i]] - yrank[yarr[i]])**2 for i in xrange(n)])

def spearman_r(xarr, yarr):
    n = len(xarr)
    d2 = squared_d(xarr, yarr, n)
    return round(1 - 6*d2/float(n**3 - n), 4)

if __name__ == "__main__":
    xarr = [ 50, 175, 270,  375, 425, 580, 710, 790, 890, 980]
    yarr = [1.8, 1.2, 2, 1, 1, 1.2, .8, .6, 1, .85]
    print rank_order(xarr)
    print rank_order(yarr)
    print spearman_r(xarr, yarr)