def no_dups(s, ln):
    '''Removes duplicate chars'''
    t = s[0]
    for i in xrange(1, ln):
        if s[i] != s[i-1]:
            t += s[i]
    print t

if __name__ == "__main__":
    no_dups('abb', 3)
