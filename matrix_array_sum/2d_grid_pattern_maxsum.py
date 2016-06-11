#!/bin/python

"""
Context
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .

Constraints

Output Format

Print the largest (maximum) hourglass sum found in .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
"""

def max_pattern_sum(arr, lo, hi, N, bound=3):
    mid = lo + (hi-lo)/2
    if lo < hi:
        return max(max_pattern_sum(arr, lo, mid, N), max_pattern_sum(arr, mid+1, hi, N))
    elif mid <= N-bound:
        return max([sum((sum(arr[mid][c:c+bound]), arr[mid+1][c+1], sum(arr[mid+2][c:c+bound]))) for c in xrange(N-bound+1)])
    return float('-inf')



arr = []
for arr_i in xrange(6):
   arr.append( map(int,raw_input().strip().split(' ')) )

N = len(arr)

print max_pattern_sum(arr, 0, N-1, N)