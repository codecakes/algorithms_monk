def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


def max_heapify(arr, idx, N):
    if idx<=N:
        largest = None
        left_idx = 2*idx + 1
        right_idx = 2*idx + 2
        
        if left_idx <= N:
            largest = max(left_idx, idx, key=lambda x: arr[x])
        if right_idx <= N:
            largest = max(largest, right_idx, key=lambda x: arr[x])
        if largest and largest != idx:
            swap(arr, largest, idx)
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
        copyarr += [arr.pop()]
        N -= 1
        arr = build_maxheap(arr, N)
    return copyarr


if __name__ == "__main__":
    arr = [3, -100, 4, 1, 2, 6]
    arr2 = [3, -100, 4, 2]
    N = len(arr)-1
    N2 = len(arr2)-1
    sorted_arr = heapsort(arr, N)
    sorted_arr2 = heapsort(arr2, N2)
    assert list(reversed(sorted_arr)) == sorted([3, -100, 4, 1, 2, 6])
    assert list(reversed(sorted_arr2)) == sorted([3, -100, 4, 2])