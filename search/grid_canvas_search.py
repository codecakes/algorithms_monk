#!/bin/python

"""
You are given a square map of size . Each cell of the map has a value denoting its depth. We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).

You need to find all the cavities on the map and depict them with the uppercase character X.

Input Format

The first line contains an integer, , denoting the size of the map. Each of the following  lines contains  positive digits without spaces. Each digit (1-9) denotes the depth of the appropriate area.

Constraints

Output Format

Output  lines, denoting the resulting map. Each cavity should be replaced with character X.

Sample Input

4
1112
1912
1892
1234
Sample Output

1112
1X12
18X2
1234
Explanation

The two cells with the depth of 9 fulfill all the conditions of the Cavity definition and have been replaced by X.
"""

I = int

def foo(arr, lo, hi, n):
    mid = (lo+hi)/2
    if lo<hi:
        foo(arr, lo, mid, n)
        foo(arr, mid+1, hi, n)
    elif lo == n-1 or lo == 0:
        print arr[lo]
    else:
        ar = arr[lo]
        for index in xrange(n):
            if n-1 > index > 0:
                if ar[index-1] != 'X' and I(arr[lo-1][index]) != 'X' and I(arr[lo+1][index]) != 'X':
                    try:
                        if I(ar[index-1]) < I(ar[index]) and I(ar[index]) > I(ar[index+1]) and \
                        I(arr[lo-1][index]) < I(ar[index]) and I(ar[index]) > I(arr[lo+1][index]):
                            ar = ar[:index]+'X'+ar[index+1:]
                    except IndexError as e:
                        print e
                        print n, index-1, index, index+1
                        print ar, len(ar)
                        raise IndexError
        print ar

def scan_cavity(arr, n):
    return foo(arr, 0, n-1, n)


n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid.append(raw_input().strip())

scan_cavity(grid, n)