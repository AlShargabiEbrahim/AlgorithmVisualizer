from render import *

#undirected_path , directed_path , directed_cycle , undirected_cycle , undirected_complete_graph , undirected_tree_graph , directed_tree_graph
def undirected_path(num_nodes):
    """Return an undirected path containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))
    undirected_path_graph = Graph(nodes, edges, directed=False, type="undirected_path")
    return undirected_path_graph


def directed_path(num_nodes):
    """Return an directed path containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))

    directed_path_graph = Graph(nodes, edges, directed=True, type="directed_path")
    return directed_path_graph


def directed_cycle(num_nodes):
    """Return an directed cycle containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))

    directed_cycle_graph = Graph(nodes, edges, directed=True, type="directed_cycle")

    directed_cycle_graph.edges.append((num_nodes - 1, 0))
    return directed_cycle_graph


def undirected_cycle(num_nodes):
    """Return an undirected cycle containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))
    undirected_cycle_graph = Graph(nodes, edges, directed=False, type="undirected_cycle")
    undirected_cycle_graph.edges.append((num_nodes - 1, 0))
    return undirected_cycle_graph


def undirected_complete_graph(num_nodes):
    """Return the complete graph containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)

    edges = list()
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            edges.append((i, j))

    complete_graph = Graph(nodes, edges, directed=False, type="undirected_complete_graph")
    return complete_graph


def undirected_tree_graph(num_nodes):
    """Return the undirected tree graph containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(1, num_nodes):
        edges.append((0, j))
    undirected_tree = Graph(nodes, edges, directed=False, type="undirected_tree")
    return undirected_tree


def directed_tree_graph(num_nodes):
    """Return the directed tree graph containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(1, num_nodes):
        edges.append((0, j))
    undirected_tree = Graph(nodes, edges, directed=True, type="directed_tree")
    return undirected_tree
#########################################################


def undirected_path_matplotlib(num_nodes):
    """Return an undirected path containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))
    return edges , 0


def directed_path_matplotlib(num_nodes):
    """Return an directed path containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))

    return edges ,1


def directed_cycle_matplotlib(num_nodes):
    """Return an directed cycle containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))

    edges.append((num_nodes - 1, 0))
    return edges ,1


def undirected_cycle_matplotlib(num_nodes):
    """Return an undirected cycle containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(num_nodes - 1):
        edges.append((j, j + 1))

    edges.append((num_nodes - 1, 0))
    return edges,0


def undirected_complete_graph_matplotlib(num_nodes):
    """Return the complete graph containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)

    edges = list()
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            edges.append((i, j))

    return edges,0


def undirected_tree_graph_matplotlib(num_nodes):
    """Return the undirected tree graph containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(1, num_nodes):
        edges.append((0, j))
    return edges,0


def directed_tree_graph_matplotlib(num_nodes):
    """Return the directed tree graph containing the number of nodes"""
    nodes = []
    for i in range(num_nodes):
        nodes.append(i)
    edges = []
    for j in range(1, num_nodes):
        edges.append((0, j))
    return edges,1

#g = undirected_cycle(4)
#draw_graph(g)
#draw_graph_matplotlib(undirected_cycle_matplotlib(4))
#T = nx.balanced_tree(2, 5)

#pos = graphviz_layout(T)
#nx.draw(T, pos)

######################################
