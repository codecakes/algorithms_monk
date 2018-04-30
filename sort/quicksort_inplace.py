"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def cmp(a, b):
    return a > b

def swap(idx_1, idx_2, arr):
    a, b = arr[idx_1], arr[idx_2]
    arr[idx_1], arr[idx_2] = b, a
    return

def sort_arr(arr, cur_idx, pivot_idx):
    if 0 <= cur_idx < pivot_idx:
        hi = pivot_idx
        while cur_idx < pivot_idx:
            pivot = arr[pivot_idx]
            if cmp(arr[cur_idx], pivot) and pivot_idx -1 == cur_idx:
                swap(cur_idx, pivot_idx, arr)
                pivot_idx -= 1
            elif cmp(arr[cur_idx], pivot):
                swap(pivot_idx-1, pivot_idx, arr)
                swap(cur_idx, pivot_idx, arr)
                pivot_idx -= 1
            else:
                cur_idx += 1
        sort_arr(arr, 0, pivot_idx-1)
        sort_arr(arr, pivot_idx+1, hi)
    return


def quicksort(array):
    """
        - cmp cur idx with pivot
        - if cur idx == previous index
            - cmp and swap and update pivot
        - else
            - swap pivot with previous index
            - swap previous index number with cur idx
        - increment to cur idx to next if arr[cur idx] <= arr[pivot idx] 
    """
    # pivot_idx = -1
    hi = len(array) - 1
    sort_arr(array, 0, hi)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
assert quicksort(test) == sorted(test)
# print quicksort(test)