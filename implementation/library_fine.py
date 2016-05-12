#!/bin/python

"""
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
Input Format

The first line contains  space-separated integers denoting the respective , , and  on which the book was actually returned.
The second line contains  space-separated integers denoting the respective , , and  on which the book was expected to be returned (due date).

Constraints

Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
"""

def isLeap(yy):
    if yy%4 != 0: return 365
    if yy%100 != 0: return 366
    if yy%400 != 0: return 365
    return 366

def month_days(m, y):
    return 28 if (m==2 and not isLeap(y)) \
        else (29 if (m ==2 and isLeap(y)) \
              else (31 if (m%2 == 1 and m<8) \
                  else (31 if m%2 == 0 and 12>=m>7 \
                        else (30 if m%2 == 1 and 12>=m>7 \
                              else 30))))

def fine_due(d1,m1,y1,d2,m2,y2):
    # d1,m1,y1 - actual
    # d2,m2,y2 - due
    # tot_days = m_count = 0
    if y1<y2:
        return 0
    if y1>y2:
        # m1_days = month_days(m1, y1)
        # m2_days = month_days(m2, y2) - d2 - 1
        # yr_days = 365 if not isLeap(y2) else 366

        # m_count += 1 if m2_days%month_days(m2, y2) == 0 else 0
        #for m in xrange(m2+1, 13):
        #    tot_days += month_days(m, y2)
        #    m_count += 1
        #    tot_days += m2_days
        #
        #    for m in xrange(1, m1):
        #        tot_days += month_days(m, y1)
        #        m_count += 1
        #    tot_days += d1

        # print tot_days
        #return 10000 if tot_days > yr_days else 500 * m_count
        return 10000
    if m1<m2:
        return 0
    if m1>m2:
        return 500 * (m1-m2)
    if d1<d2:
        return 0
    if d1>d2:
        return 15 * (d1-d2)
    return 0

d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

print fine_due(d1,m1,y1,d2,m2,y2)