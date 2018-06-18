def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def get_left(idx): return 2*idx + 1
def get_right(idx): return 2*idx + 2
def get_parent(idx): return idx/2 if idx%2 else idx/2 - 1


# def min_heapify(arr, idx, N):
#     if idx<=N:
#         smallest = None
#         left_idx = get_left(idx)
#         right_idx = get_right(idx)
        
#         if left_idx <= N:
#             smallest = min(left_idx, idx, key=lambda x: arr[x])
#         if right_idx <= N:
#             smallest = min(smallest, right_idx, key=lambda x: arr[x])
#         if smallest and smallest != idx:
#             swap(arr, smallest, idx)
#             min_heapify(arr, smallest, N)
#         elif smallest > 0 and arr[get_parent(smallest)] > arr[smallest]:
#             parent_idx = get_parent(smallest)
#             swap(arr, smallest, parent_idx)
#             min_heapify(arr, smallest, N)

def max_heapify(arr, idx, N):
    if idx<=N:
        largest = None
        left_idx = get_left(idx)
        right_idx = get_right(idx)
        
        if left_idx <= N:
            largest = max(left_idx, idx, key=lambda x: arr[x])
        if right_idx <= N:
            largest = max(largest, right_idx, key=lambda x: arr[x])
        if largest and largest != idx:
            swap(arr, largest, idx)
            max_heapify(arr, largest, N)
        elif largest > 0 and arr[get_parent(largest)] < arr[largest]:
            parent_idx = get_parent(largest)
            swap(arr, largest, parent_idx)
            max_heapify(arr, largest, N)

def build_maxheap(arr, N):
    idx = N+1/2
    while idx >= 0:
        max_heapify(arr, idx, N)
        idx -= 1
    return arr

def heapsort(arr, N):
    copyarr = []
    arr = build_maxheap(arr, N)
    while N >= 0:
        swap(arr, 0, N)
        N -= 1
        copyarr.insert(0, arr.pop())
        max_heapify(arr, 0, N)
    return copyarr


if __name__ == "__main__":
    arr = [3, -100, 4, 1, 2, 6]
    arr2 = [3, -100, 4, 2]
    N = len(arr)-1
    N2 = len(arr2)-1
    sorted_arr = heapsort(arr, N)
    sorted_arr2 = heapsort(arr2, N2)
    assert sorted_arr == sorted([3, -100, 4, 1, 2, 6])
    assert sorted_arr2 == sorted([3, -100, 4, 2])