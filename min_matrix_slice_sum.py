# https://www.hackerearth.com/problem/algorithm/monk-in-the-grass-fields/description/

from math import log, ceil

from collections import deque

def left_index(index): return 2*index + 1

def right_index(index): return 2*index + 2

def left_child (h, index): return h[left_index(index)]

def right_child (h, index): return h[right_index(index)]

def parent_index(index): return index/2 -1 if index%2==0 else index/2

def parent(h, index): return h[parent_index(index)]

def swap(h, v1, v2): h[v1], h[v2] = h[v2], h[v1]

def min_key(h, key):
    '''minimum of two child key index of a parent key'''
    left_node = left_child(h, key)
    right_node = right_child(h, key)
    if left_node and right_node: return left_index(key) if left_node[0] < right_node[0] else right_index(key)
    elif not left_node: return -1
    else: return left_index(key)

def bubble_down(h, key):
    '''bubbles down max key at pos 'key' down to the leaf nodes'''
    # print "In bubble down"
    # print "min_child_key = min_key(h, key) key =%s" %(key)
    min_child_key = min_key(h, key)
    # print min_child_key , h[min_child_key], h[key], h.maxKey()
    if min_child_key < 0: return
    while h[min_child_key] and h[key][0] > h[min_child_key][0] and key < h.maxKey():
        # print "min_child_key %s, h[min_child_key] %s, key %s, h[key] %s, h.maxKey() %s" %(min_child_key, h[min_child_key], key, h[key], h.maxKey())
        swap(h, key, min_child_key)
        key = min_child_key
        min_child_key = min_key(h, key)
        if min_child_key < 0: return
    # print "bubble down ends"

def _bubbleUp(self, index):
    '''check heap min property by Bubble Up'''
    # print "in bubbleUp"
    parent_node = parent(self, index)
    if not parent_node: return
    while self[index][0] < parent_node[0] and index > 0:
        swap(self, index, parent_index(index))
        index = parent_index(index)
        parent_node = parent(self, index)
        if not parent_node: return
    # print "bubbleUp ends"

def rebalance(hmin, index, val):
	'''rebalances tree from index and below using bubble_down'''
	assert index == 0
	hmin_val = hmin[index]
	hmin[index] = (hmin_val[0]+val, hmin_val[1])
	# print "hmin", hmin
	bubble_down(hmin, index)


class MinHeap(object):

    def __init__(self):
        self._arr = []
        self._index = 0

    def __getitem__(self, index):
        #print "getitem index", index
        return self._arr[index] if (0 <= index < self._index and self._index != 0) else None

    def __setitem__(self, key, val):
        if (0 <= key < self.maxKey()): self._arr[key] = val

    def maxKey(self): return self._index

    def insert(self, val):
        self._arr.append(val)
        self._index += 1
        # print "added %s %s" %(val[0], val[1])
        _bubbleUp(self, self._index-1)

    def extract_min(self):
        del self[0]

    def __delitem__(self, index):
        if self._index == 0: return
        if index == 0:
            swap(self, 0, self._index-1)
            pop_node = self._arr.pop()
            bubble_down(self, 0)
            self._index -= 1
            return pop_node
        elif index == self._index-1:
            self._index -= 1
            return self._arr.pop()

    def __str__(self): return "{}".format(self._arr)

def fill_heap(arr, sum_index, h): h.insert((sum(arr), sum_index))

def row_slice_mat(mat, N):
	h = MinHeap()
	stack = [[0, N-1]]
	lo = hi = 0
	while stack:
		lo, hi = stack.pop()
		mid = (lo+hi)/2
		if lo<hi:
			stack.insert(0, [lo, mid])
			stack.insert(0, [mid+1, hi])
		else:
			fill_heap(mat[lo], lo, h)
	return h

def col_slice_mat(mat, N):
	h = MinHeap()
	stack = [[0, N-1]]
	lo = hi = 0
	# O(N lgN)
	while stack:
		lo, hi = stack.pop()
		mid = (lo+hi)/2
		if lo<hi:
			stack.insert(0, [lo, mid])
			stack.insert(0, [mid+1, hi])
		else:
			# O(N)
			fill_heap([mat[i][lo] for i in xrange(N)], lo, h)
	return h


def min_level_traversal(mat, N, K):
    level = 0
    row_sum_heap = row_slice_mat(mat, N)
    col_sum_heap = col_slice_mat(mat, N)

    tree_level = int(ceil(log(N, 2)))
    minVal = None
    countr = countc = 0

    sr = deque([], N)
    sc = deque([], N)
    # should be close to ~O(K lgN)
    for _ in xrange(K):
        minRow, indexRow = row_sum_heap[0]
        minCol, indexCol = col_sum_heap[0]


        if minRow != minCol:
            minVal, hmin, h_other = (minRow, row_sum_heap, col_sum_heap) if minRow<=minCol else (minCol, col_sum_heap, row_sum_heap)
        else:
            # FIX THIS!!
            # https://www.hackerearth.com/problem/algorithm/monk-in-the-grass-fields/description/

            # does level order traversal to find out all nodes with same rank as minRow and minCol
            countr = 1
            countc = 1
            minRow2, minCol2 = minRow, minCol
            sr.append(0)
            while sr:
                r = sr.pop()
                row_left = left_child(row_sum_heap, r)
                row_right = right_child(row_sum_heap, r)
                if row_left:
                    if row_left[0] == minRow2:
                        countr += 1
                        sr.appendleft(row_left[1])
                if row_right:
                    if row_right[0] == minRow2:
                        countr += 1
                        sr.appendleft(row_right[1])

            sc.append(0)
            while sc:
                c = sc.pop()
                col_left = left_child(col_sum_heap, c)
                col_right = right_child(col_sum_heap, c)
                if col_left:
                    if col_left[0] == minCol2:
                        countc += 1
                        sc.appendleft(col_left[1])
                if col_right:
                    if col_right[0] == minCol2:
                        countc += 1
                        sc.appendleft(col_right[1])

            minVal, hmin, h_other =(minRow, row_sum_heap, col_sum_heap) if countr >= countc else (minCol, col_sum_heap, row_sum_heap)
        # print minVal

        level += minVal

        # rebalances the heap tree ~O(lg N)
        rebalance(hmin, 0, N)

        for i in xrange(N):
            val, index = h_other[i]
            h_other[i] = (val+1, index)

    return level

if __name__ == "__main__":
    print "level:", min_level_traversal([[1,3], [2,4]], 2, 1)
    print "level:", min_level_traversal([[1,3], [2,4]], 2, 2)
    print "level:", min_level_traversal([[1,3], [2,4]], 2, 3)
    print "level:", min_level_traversal([[1,3], [2,4]], 2, 4)

    # print min_level_traversal([[6, 7], [7, 6]], 2, 4)
    print min_level_traversal([[4, 2, 1], [2, 1, 4], [1, 5, 6]], 3, 2)
    print min_level_traversal([[4, 2, 1], [2, 1, 5], [1, 4, 6]], 3, 2)

    # import os
    # from cStringIO import StringIO

    # with open(os.path.join(os.getcwd(), 'min_slice_tests', "test4.txt"), 'r') as f:
    #     s = StringIO(f.read())

    # with open( os.path.join(os.getcwd(), 'min_slice_tests', r"test4_res.txt") ) as f:
    #     ans = StringIO(f.read())


    # T = int(s.readline().strip("\n"))
    # t= 0

    # for case in xrange(T):
   	# N, K = map(int, s.readline().strip("\n").split(" "))
   	# mat = [map(int, s.readline().strip("\n").split(" ")) for _ in xrange(N)]
   	# res = min_level_traversal(mat, N, K)
   	# res2 = int(ans.readline().strip("\n"))
   	# t = case+1
   	# if res != res2:
   	#     print "Wrong Case#: %s" %(t)
   	#     print res, res2, K