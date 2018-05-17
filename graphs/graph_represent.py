class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        return [(edge.value, edge.node_from.value, edge.node_to.value) for edge in self.edges]

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        
        max_val = float('-inf')
        min_val = float('inf')
        #O(N)
        count = 0
        for node in self.nodes:
            count += 1
            if node.value > max_val:
                max_val = node.value
            if node.value < min_val:
                min_val = node.value
        #O(N+k)
        arr = [None for _ in xrange(min_val + count)]
        #O(E*lg(N)), where E <= N
        self.divide_conquer(self.nodes, 0, count-1, lambda node: self.adjacency_list_helper(arr, node))
        return arr

    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        
        max_val = float('-inf')
        min_val = float('inf')
        count = 0
        for node in self.nodes:
            count += 1
            if node.value > max_val:
                max_val = node.value
            if node.value < min_val:
                min_val = node.value
        arr = [[0]*(min_val + count) for _ in xrange(min_val + count)]
        self.divide_conquer(self.nodes, 0, count-1, lambda node: self.adjacency_matrix_helper(arr, node))
        return arr
        
    
    @staticmethod
    def adjacency_matrix_helper(arr, node):
        for e2 in node.edges:
            if e2.node_to != node:
                arr[node.value][e2.node_to.value] = e2.value
    
    
    @staticmethod
    def adjacency_list_helper(arr, node):
        for e2 in node.edges:
            if e2.node_to != node:
                if not arr[node.value]:
                    arr[node.value] = []
                arr[node.value].append((e2.node_to.value, e2.value))
    
    @classmethod
    def divide_conquer(cls, arr, lo, hi, func):
        mid = lo + (hi-lo)/2
        if lo < hi:
            cls.divide_conquer(arr, lo, mid, func)
            cls.divide_conquer(arr, mid+1, hi, func)
        else:
            func(arr[lo])

if __name__ == "__main__":     
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)
    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print graph.get_edge_list()
    assert graph.get_edge_list() == [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print graph.get_adjacency_list()
    assert graph.get_adjacency_list() == [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print graph.get_adjacency_matrix()
    assert graph.get_adjacency_matrix() == [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]