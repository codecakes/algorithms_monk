#!/bin/python

"""
Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters.

There are nn chapters in Lisa's workbook, numbered from 11 to nn.
The ii-th chapter has titi problems, numbered from 11 to titi.
Each page can hold up to kk problems. There are no empty pages or unnecessary spaces, so only the last page of a chapter may contain fewer than kk problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at 11.
Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. Given the details for Lisa's workbook, can you count its number of special problems?

Note: See the diagram in the Explanation section for more details.

Input Format

The first line contains two integers nn and kk — the number of chapters and the maximum number of problems per page respectively.
The second line contains nn integers t1,t2,…,tnt1,t2,…,tn, where titi denotes the number of problems in the ii-th chapter.

Constraints

1=<n,k,ti=<1001=<n,k,ti=<100
Output Format

Print the number of special problems in Lisa's workbook.

Sample Input

5 3
4 2 6 1 10
Sample Output

4
"""


def spl_question(arr, n, k):
    prev_accum = cumm = tot_pg_num = ques = count = 0

    for each_chptr in arr:
        # O(N)
        pgs, rem = divmod(each_chptr, k)
        ques = prev_accum = cumm = 0
        for pg in xrange(pgs):
            tot_pg_num += 1
            ques += k
            cumm = ques
            if prev_accum < tot_pg_num <= cumm:
                count += 1
            prev_accum = cumm
        if rem:
            tot_pg_num += 1
            ques += rem
            cumm = ques
        if prev_accum < tot_pg_num <= cumm:
            count += 1
    return count

if __name__ == "__main__":
    n, k = raw_input().strip("\n").split()
    n, k = int(n), int(k)

    arr = map(int, raw_input().strip("\n").split())

    print spl_question(arr, n, k)