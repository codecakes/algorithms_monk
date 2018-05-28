#!/bin/python

import math
import os
import random
import re
import sys

DCT = {
    ')': '(',
    ']': '[',
    '}': '{'
}

BRACKETS = DCT.values() + DCT.keys()


def ast_bracket(expr):
    stack = []
    for br in expr:
        if br in BRACKETS:            
            if stack:
                sym = DCT.get(br, None)
                if sym and stack[-1] == sym:
                    stack.pop()
                elif sym == None:
                    stack.append(br)
                else:
                    return 'NO'
            else:
                stack.append(br)
    return 'YES' if not stack else 'NO'


if __name__ == '__main__':
    # t = int(raw_input())

    expr = output = res = ''
    try:    
        with open('test_ast_brackets.txt', 'r') as F:
            with open('test_output_ast_brackets.txt') as RES:    
                t = int(F.readline().strip())
                print t
                for t_itr in xrange(t):
                    expr = expression = F.readline().strip()
                    res = ast_bracket(expression)
                    output = RES.readline().strip()
                    # print "expr is %s and output is: %s and result is: %s" %(expr, output, res)
                    assert res == output
    except Exception as e:
        print e
        print "Error at", expr, res, output
    finally:
        print "DONE!"
        sys.exit()

