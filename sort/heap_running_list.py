#!/bin/python
"""
https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
"""

# heapq given for historical reasons
# it works. but not as fast in python 
# as insort implementation version

import heapq
from bisect import insort

            
def _insert(a_item, min_heap, max_heap, n):
    if n%2:
        to_min = heapq._heappushpop_max(max_heap, a_item)
        heapq.heappush(min_heap, to_min)
    else:
        max_heap.append(a_item)
        heapq._heapify_max(max_heap)
        if not min_heap:
            return n + 1
        if max_heap[0] > min_heap[0]:
            to_max = heapq.heappop(min_heap)
            to_min = heapq._heappushpop_max(max_heap, to_max)
            assert to_max != to_min
            heapq.heappush(min_heap, to_min)
    return n+1


def get_median(min_heap, max_heap, n):
    if n%2:
        return max_heap[0] * 1.0
    else:
        return (min_heap[0] + max_heap[0])/2.0

    
def find_median(a_item, min_heap, max_heap, n):
    n = _insert(a_item, min_heap, max_heap, n)
    # print max_heap, min_heap
    return get_median(min_heap, max_heap, n), n
    
F = float

if __name__ == '__main__':
    min_heap = []
    max_heap = []
    res = []
    ln = 0

    for _ in xrange(int(raw_input())):
        a_item = int(raw_input())
        # median, ln = find_median(a_item, min_heap, max_heap, ln)
        # print median
        insort(res, a_item)
        ln = len(res)
        median = res[ln/2] if ln%2 else (res[ln/2] + res[ln/2 - 1])/2.0
        print F(median)
