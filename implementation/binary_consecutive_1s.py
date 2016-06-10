#!/bin/python

"""
Task
Given a base- integer, , convert it to binary (base2-). Then find and print the base-10 integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, .

Constraints

Output Format

Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2

"""


num = int(raw_input().strip())

bitStr = bin(num)[2:]
ln = len(bitStr)

def maxOnes(bitStr, ln):
    i = _maxC = count = 0
    for j in xrange(ln):
        if bitStr[j] == '1':
            count += 1
        else:
            _maxC = max(_maxC, count)
            i = j
            count = 0
    _maxC = max(_maxC, count)
    return _maxC

print maxOnes(bitStr,ln)


