# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

from collections import defaultdict, namedtuple

def find_bridges(adj_matrix):
    timer = 0
    covered = {}
    fup = {}
    tin = {}
    bridges = defaultdict(list)
    [bridge_dfs(
        node, None, timer, tin, fup, adj_matrix, covered, bridges
        ) for node in adj_matrix if node not in covered
    ]
    return bridges
    

def bridge_dfs(node, from_node, timer, tin, fup, adj_matrix, covered, bridges):
    covered[node] = True
    timer += 1
    # Note total time through all paths and time to reach IN node.
    fup[node] = tin[node] = timer
    for v2 in adj_matrix[node]:
        # For all nodes not parent node from_node.
        if v2 != from_node:
            if v2 in covered:
                fup[node] = min(tin[node], fup[v2])
            else:
                bridge_dfs(v2, node, timer, tin, fup, adj_matrix, covered, bridges)
                fup[node] = min(fup[node], fup[v2])
            # If the connection from node -> v2 < time via all 
            # other routes to reach v2 then its a bridge node.
            if tin[node] < fup[v2]:
                bridges[node].append(v2)
                bridges[v2].append(node)

def get_edges_cached_decorate(func):
    if not hasattr(func, 'cache'):
        setattr(func, 'cache', {})
    def get_non_bridges(*args, **kw):
        hashed = hash((args, kw))
        if hashed not in func.cache:
            res = func.cache[hashed] = func(*args, **kw)
        else:
            res = func.cache[hashed]
        return res
    return get_non_bridges

# @get_edges_cached_decorate
def filter_non_bridges(node_list, bridges):
    return [node for node in node_list if node not in bridges]

def pick_node(from_node, to_nodes, edges_covered):
    for to_node in to_nodes:
        # print 'inside pick_node. from_node=%s to_node=%s' %(from_node, to_node)
        # print 'edges_covered', edges_covered
        if (from_node, to_node) not in edges_covered[from_node] and (
            to_node, from_node) not in edges_covered[to_node]:
            return to_node
    return None

def find_eulerian_tour(graph):
    adj_matrix = defaultdict(list)
    num_odd_edged_nodes = 0
    odd_nodes = []
    edges_covered = defaultdict(list)
    edges = []
    bridge_nodes = defaultdict(set)
    # Create adjency matrix.
    for edge in graph:
        adj_matrix[edge[0]].append(edge[1])
        adj_matrix[edge[1]].append(edge[0])
    # print 'adj_matrix', adj_matrix
    # Get a list of all nodes.
    all_nodes = adj_matrix.keys()
    # print 'all nodes are', all_nodes
    # Find all nodes with bridge edges.
    bridges = find_bridges(adj_matrix)
    # print 'bridge nodes >>>', bridges
    for node in adj_matrix:
        num_odd_edged_nodes = len(adj_matrix[node])
        if num_odd_edged_nodes%2 == 1:
            odd_nodes.append(node)
    num_odd_nodes = len(odd_nodes)
    node = None
    # print 'odd_nodes', odd_nodes
    # Choose nodes with odd edges if available.
    node_list = odd_nodes if num_odd_nodes%2 == 1 else all_nodes
    # Filter Nodes that have non-bridge edges.
    # print 'node_list before', node_list
    node_list = filter_non_bridges(node_list, bridges) or node_list
    # print 'node_list after', node_list
    # Pick any random node.
    from_node = node_list[0]
    # print '1st node picked', from_node
    while True:
        to_nodes = adj_matrix[from_node]
        # print 'to_nodes', to_nodes
        # Cached function. pick a non bridge edge if available.
        to_nodes = filter_non_bridges(to_nodes, bridges) or to_nodes
        # Add the bridge nodes.
        bridge_nodes[from_node].update(set(adj_matrix[from_node]) - set(to_nodes))
        # Try to pick a new node each time. Prefer a non bridge node over a bridged one.
        to_node = pick_node(from_node, to_nodes, edges_covered) or pick_node(
            from_node, bridge_nodes[from_node], edges_covered)
        # print 'from node %s to_node picked %s' %(from_node, to_node)
        if to_node is not None:
            edges_covered[from_node].append((from_node, to_node))
            edges.append((from_node, to_node))
            # Traverse the other node on the edge.
            from_node = to_node
        else:
            break
        # print 'edges_covered', edges_covered
    # print 'edges_covered', edges_covered
    # print edges
    result = []
    for edge in edges:
        if result and edge[0] != result[-1]:
            result.append(edge[0])
        if result and edge[1] != result[-1]:
            result.append(edge[1])
        else:
            result.extend(edge)
    del bridge_nodes, edges_covered, adj_matrix, node_list
    return result


assert find_eulerian_tour([(1, 2), (2, 3), (3, 1)]) == [1,2,3,1]
assert find_eulerian_tour([(1, 2), (2, 4), (3, 1), (3, 4)]) == [1, 2, 4, 3, 1]
assert find_eulerian_tour(
    [
        (0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
        (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)
    ]) == [2, 4, 8, 9, 5, 4, 0, 1, 7, 3, 6, 1, 5, 2]

assert find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19),
(3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
(1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
(6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)]
)
