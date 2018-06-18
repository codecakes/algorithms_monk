"""
Max Priority Queue is based on the structure of max heap and can perform following operations:

maximum(Arr) : It returns maximum element from the Arr.
extract_maximum (Arr) - It removes and return the maximum element from the Arr.
increase_val (Arr, i , val) - It increases the key of element stored at index i in Arr to new value val. 
insert_val (Arr, val ) - It inserts the element with value val in Arr.
"""

from heapsort import get_parent, swap, max_heapify, build_maxheap, heapsort

class PQ(object):
    def __init__(self, arr):
        self.arr = arr if isinstance(arr, list) else []
        self.N = len(arr) if isinstance(arr, list) else 0
    
    def setup_build(self):
        build_maxheap(self.arr, self.N-1)
    
    def maximum(self):
        return self.arr[0] if self.arr else None
    
    def extract_maximum(self):
        ln = self.N - 1
        if not self.arr:
            return None
        swap(self.arr, 0, ln)
        val = self.arr.pop()
        ln -= 1
        max_heapify(self.arr, 0, ln)
        self.N -= 1
        return val

    
    def increase_val(self, idx, val):
        ln = self.N - 1
        if idx < self.N:
            self.arr[idx] = val
            max_heapify(self.arr, idx, ln)
    
    def insert_val(self, val):
        self.arr.append(val)
        self.N += 1
        last_idx = self.N - 1
        max_heapify(self.arr, get_parent(last_idx), last_idx)


