#!/bin/python

import os
from cStringIO import StringIO as IO

def scan_block(G, P, G_index, start_col, R, r, c):
    gr = G_index
    gc = start_col
    pr = 0
    pc = 0
    # O(r*c)
    # matrix traversal
    while gr < R and gc < C:
        while pc < c and pr < r:
            if G[gr][gc] != P[pr][pc]:
                return False
            # print "G[%s][%s]:%s == P[%s][%s]:%s ?"%(gr, gc, G[gr][gc], pr, pc, P[pr][pc])
            gr += 1
            pr += 1
        gr = G_index
        pr = 0
        gc += 1
        pc += 1
    return True

def scan(G, P, G_index, R, C, r, c):
    if not (G_index + r -1 < R):
        return False
    stat = False
    # O(R * r*c)
    # print "scanning row %s"%(G_index)
    for start_col in xrange(C):
        # print "scanning col %s"%(start_col)
        stat = scan_block(G, P, G_index, start_col, R, r, c)
        # print stat
        if stat:
            return stat
    return False

def sliceG(G, P, lo, hi, R, C, r, c):
    # O(R*rc*lgR)
    mid = (lo+hi)/2
    if lo<hi:
        # log(R)
        return sliceG(G, P, lo, mid, R, C, r, c) or sliceG(G, P, mid+1, hi, R, C, r, c)
    else:
        # O(R * r*c)
        return scan(G, P, lo, R, C, r, c)


def detect_pattern(G, P, R, C, r, c):
    return 'YES' if sliceG(G, P, 0, R-1, R, C, r, c) else 'NO'

if __name__ == "__main__":

    with open(os.path.join(os.getcwd(), 'grid_pattern_tests','nuance.txt')) as test:
        fin = IO(test.read())

    with open(os.path.join(os.getcwd(), 'grid_pattern_tests','nuanceout.txt')) as ans:
        fout = IO(ans.read())

    t = int(fin.readline().strip("\n").strip())
    for a0 in xrange(t):
        R,C = fin.readline().strip("\n").strip().split(' ')
        R,C = [int(R),int(C)]
        G = []
        G_i = 0
        for G_i in xrange(R):
           G.append(map(int, fin.readline().strip("\n").strip().strip('\n')))
        r,c = fin.readline().strip("\n").strip().split(' ')
        r,c = [int(r),int(c)]
        P = []
        P_i = 0
        for P_i in xrange(r):
           P.append(map(int, fin.readline().strip("\n").strip().strip('\n')))
        ans = fout.readline().strip("\n").strip()
        res = detect_pattern(G, P, R, C, r, c)
        try:
            assert res == ans
        except AssertionError as e:
            print "error in test case# %s"%(a0+1)
            print res, ans, R, C, r, c
        # print "="*20
    # print detect_pattern(G, P, R, C, r, c)
