#!/bin/python

from collections import defaultdict, deque
from functools import wraps
from functools import partial as ptl


class Cacher(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        # print 'Cacher called with %s entries' %(len(self.cache))
        return self.cache[args]
    
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return ptl(self.__call__, obj)
    

class BadKeyError(Exception):

    def __init__(self, errmsg):
        super(type(self), self).__init__(r"%s" % errmsg)

        
class Node(object):
    """A singleton Trie Node."""
    
    def __init__(self, val, parent, children):
        """Initialize.
        
        Args:
          val: str, a character value.
          parent: object, a Node object referencing to its parent node.
          children: defaultdict, of type Node.
        """
        self.parent = None or parent
        self.val = None or val
        self.children = children or defaultdict(Node.__class__)
    
    def __getitem__(self, key):
        return self.children.get(key, None)
    
    def __setitem__(self, key, val):
        self.children[key] = Node(key, self, None)
    
    def __contains__(self, key):
        return key in self.children
    
    def __iter__(self):
        if not self.children:
            raise StopIteration("No substring exists!")
        return self.children.itervalues()


class Trie(object):

    def __init__(self):
        self.root = Node(None, None, None)
        
    def _check(self, substr):
        cur_node = self.root
        if not cur_node.children:
            return False
        cmp_str = ''
        for char in substr:
            if char not in cur_node:
                return False
            else:
                cur_node = cur_node[char]
                cmp_str += char
            if cmp_str == substr:
                return cur_node
    
    @Cacher
    def _check_append(self, substr):
        cur_node = self.root
        cmp_str = ''
        for char in substr:
            # character of substring shouldn't be '*'
            if char == '*':
                raise BadKeyError(r"Cannot set %s as character. Not allowed" % char)
            if char not in cur_node:
                cur_node[char] = char
            cur_node = cur_node[char]
            assert cur_node != None
            cmp_str += char
            if cmp_str == substr:
                return cur_node
    
    def insert(self, substr):
        if substr:    
            cur_node = self._check_append(substr)
            cur_node['*'] = '*'
    
    @Cacher
    def search(self, substr):
        return self._check(substr)


class Contacts(Trie):
    """Contacts application!
    AddName: str, add name, where name is a string denoting a contact name. This must store  as a new contact in the application.
    FindPartial: str, find partial, where partial is a string denoting a partial name to search the application for. It must count the number of contacts starting with `partial` and print the count on a new line.
    Given sequential add and find operations, perform each operation in order.
    """

    def __init__(self):
        super(type(self), self).__init__()
    
    def AddName(self, name):
        """Add contact Name.
        Args:
          name: str, add name, where name is a string denoting a contact name. This must store  as a new contact in the application.
        """
        self.insert(name)
    
    def FindPartial(self, partial):
        """Finds all contacts starting with a substring.
        
        Args:
          partial: str, find partial, where partial is a string denoting a partial name to search the application for. It must count the number of contacts starting with `partial` and print the count on a new line.
         
         Returns:
           count: int, count of all matches.
        """
        cur_node = self.search(partial)
        # res = []
        count = 0
        if cur_node:
            stack = deque([])
            for k in cur_node:
                if k.val == '*':
                    # res.append(partial)
                    count += 1
                else:
                    stack.appendleft(k)
            while stack:
                key_node = stack.pop()
                for node in key_node:
                    if node.val == '*':
                        # res.append(partial+key_node.val)
                        count += 1
                    else:
                        stack.appendleft(node)
        # return len(res)
        return count


if __name__ == '__main__':
    
    test_book = Contacts()
    test_book.AddName('pandey')
    test_book.AddName('pandeyupadhyay')
    assert test_book.FindPartial('pan') == 2

    book = Contacts()

    with open('./testdata/output02.txt', 'r') as f:    
        # for n_itr in xrange(int(raw_input())):
        n_itr = int(raw_input())
        
        for line_num, line in enumerate(f):
            opContact = raw_input().split()

            op = opContact[0].strip()

            contact = opContact[1].strip()
            w = int(line.strip())
            if op == 'add':
                book.AddName(contact)
            elif op == 'find':
                try:
                    assert book.FindPartial(contact) == w
                except AssertionError as e:
                    print '%s for word %s at line %s\n' % (e.message, contact, line_num), book.FindPartial(contact), w
                    raise(e)
                    pass