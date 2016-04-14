# Prateek wants to give a party to his N friends on his birthday, where each friend is numbered from 1 to N. His friends are asking for a gift to come to the party, instead of giving him one. The cost of the gifts are given in the array Value where ith friend asks for a gift which has a cost Costi.

# But, Prateek has only X amount of money to spend on gifts and he wants to invite his friends which are in continuous range such that sum of the cost of the gifts of those friends will be exactly equal to X.

# If he can invite his friends, who can satisfy the above condition then, print YES otherwise print NO.

# Input:
# The first line contains a single integer T, denoting the number of test cases. In each test case, the following input will be present: - The next line contains two space-separated integers N and X, where N represents the number of friends and X represents amount of money which Prateek can spend on gifts.
# - Next N line contains N integers, where ith line contains ith integer, which represents the Costi .

# Ouput
# Output exactly T lines, each containing the answer to the corresponding test case .

# Constraints:
# 1 <= T <= 10
# 1 <= N , Costi <= 106
# 1 <= X <= 1012

# Sample Input(Plaintext Link)
#  1
# 5 12
# 1
# 3
# 4
# 5
# 2
# Sample Output(Plaintext Link)
#  YES
# Explanation
# In the sample input, T is equal to 1. So, accordingly, in next line, values of N and X are given which are 5 and 12 respectively. In the next 5 lines, you have costi asked by ith friend. As friends numbered from 2 to 4 (inclusively) have gifts value which are {3, 4, 5}, and their sum equals to 12 - that is, the given value of X. So, the answer is YES.In


def is_conssecutive_sum(arr, x, N):
    '''Finds a subarray sequence of Positive numebers that adds upto x
    Using Sliding Window Array subsequence.
    ~O(maxSubArr * N)'''
    s = d = i = j =  0
    start = end = 0
    while j < N:
        #print "s=%s"%s
        while s-d < x and i < N:
            s += arr[i]
            end = i + 1
            i += 1
        else:
            #print "s=%s@ d=%s i=%s"%(s,d,i)
            #while sum s still > x inc j
            if s-d != x:
                d += arr[j]
                start = j+1
            elif s-d == x:
                #print arr[start:end], s, d, x,N
                return "YES"
            j += 1
            #if s-d < x:
            #    s -= d
            #print "s=%s d=%s @j=%s"%(s,d,j)
    #print "s:%s"%s
    del i,j
    #print arr[start:end], s, x,N, "NO"
    return 'NO'
    # return 'YES' if sum(arr[start:end+1]) == x else 'NO'

if __name__ == "__main__":
    assert is_conssecutive_sum([1, 3, 4, 5, 2], 12, 5) == 'YES'
    assert is_conssecutive_sum([1, 2, 3, 4, 5], 12, 5) == "YES"
    assert is_conssecutive_sum([2,3,7,8,9,10], 15, 6) == "YES"
    assert is_conssecutive_sum([1,2,3,4,5,6,7], 45, 7) == "NO"
    assert is_conssecutive_sum([4,5,7,8,1,2,3,5], 35, 8) == "YES"
    assert is_conssecutive_sum([2, 4, 6, 8, 9], 1, 5) == "NO"
    assert is_conssecutive_sum([2, 3, 4, 5, 8, 9, 50], 50, 7) == "YES"