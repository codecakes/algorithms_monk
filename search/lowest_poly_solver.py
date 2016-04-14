# Our monk, while taking a stroll in the park, stumped upon a polynomial ( A X2 + B X +C ) lying on the ground. The polynomial was dying! Being considerate, our monk tried to talk and revive the polynomial. The polynomial said:
# I have served my purpose, and shall not live anymore. Please fulfill my dying wish. Find me the least non-negative integer Xo, that shall make my value atleast K i.e., A Xo2 + B Xo + C >= K .

# Help our Monk fulfill the polynomial's dying wish!


# Input:
# The first line contains an integer T. T test cases follow.
# Each test case consists of four space-separated integers A, B, C and K.

# Output:
# For each test case, output the answer in a new line.

# Constraints:
# 1 ≤ T ≤ 105
# 1 ≤ A,B,C ≤ 105
# 1 ≤ K ≤ 1010

# Sample Input(Plaintext Link)
#  3
# 3 4 5 6
# 3 4 5 5
# 3 4 5 150
# Sample Output(Plaintext Link)
#  1
# 0
# 7

from math import log, ceil, sqrt

E = lambda a,b,c,x: a*x**2 + b*x + c

y = lambda a,b,c: b**2 - 4*a*c
X = lambda a,b,c, det: ((-b - det)/float(2*a), (-b + det)/float(2*a))

def poly_solver(a,b,c,K):
    # print "inside poly_solver"
    if K < min(a,b,c):
        # print "%s < min(%s,%s,%s)"%(K, a,b,c)
        return 0
    N = 0
    det = y(a,b,c)
    # print "det %s"%(det)
    if det > 0:
        roota, rootb = X(a,b,c,sqrt(det))
        root = N = int(min(roota, rootb))
        # while E(a,b,c,root) < K:
        #     root += 1
        # root = root if root > 0 else 0
        if E(a,b,c,root) >= K:
            # print "YES! root=%s Eqn=%s"%(root, E(a,b,c,root))
            # return root
            N = root + 2
    if N<=0:
        t = int(ceil(log(K, 2) + 1))
        N = t * 10**(int(log(t,2)))
    root = N
    # print "root=%s"%(root)
    # arr = range(N)
    lastmid = lefti = mid = 0
    righti = N-1
    # print "N=%s"%N
    # print "lefti=%s righti=%s"%(lefti, righti)
    while lefti<righti:
        mid = (lefti+righti)/2
        if lastmid == mid:
            mid += 1
        if mid == righti:
            break
        if E(a,b,c,mid) >= K:
            righti = mid
        else:
            lefti = mid
        lastmid = mid
        # print "righti", righti
        # print "lefti=%s righti=%s"%(lefti, righti)
    # print "lefti=%s righti=%s"%(lefti, righti)
    # print "root=%s Eqn=%s"%(arr[righti], E(a,b,c,arr[righti]))
    assert E(a,b,c,righti) >= K
    return righti if E(a,b,c,righti) >= K else 0


if __name__ == "__main__":

    # assert poly_solver(3,4,5,6) == 1
    # assert poly_solver(3,4,5,5) == 0
    # assert poly_solver(3,4,5,150) == 7

    import os
    from cStringIO import StringIO

    with open(os.path.join(os.getcwd(), 'poly_solver_tests', 'test14.txt')) as f:
        test = StringIO(f.read())

    with open(os.path.join(os.getcwd(), 'poly_solver_tests', 'test14ans.txt')) as f:
        res = StringIO(f.read())

    T = int(test.readline().strip("\n"))
    for _ in xrange(T):
        a,b,c,K = map(int, test.readline().strip("\n").split())
        ans = int(res.readline().strip("\n"))
        try:
            out = poly_solver(a,b,c,K)
            if out != ans:
                print a,b,c,K, out, E(a,b,c, out), ans, E(a,b,c,ans), E(a,b,c, out) >= K
        except AssertionError as e:
            print "Error Error"
            print a,b,c,K, e.args, e.message, ans

