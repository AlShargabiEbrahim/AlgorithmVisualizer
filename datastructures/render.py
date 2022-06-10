from collections import namedtuple
from pyvis.network import Network

import networkx as nx
import matplotlib.pyplot as plt
import pydot

from networkx.drawing.nx_pydot import graphviz_layout
import random



Graph = namedtuple("Graph", ["nodes", "edges", "directed", "type"])


def adjacency_list(graph):
    """Returns the adjacency list """
    adjacency_list = {node: [] for node in graph.nodes}

    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adjacency_list[node1].append(node2)

        if not graph.directed:
            adjacency_list[node2].append(node1)

    return adjacency_list


def adjacency_matrix(graph):
    """Returns the adjacency matrix """

    adjacency_matrix = [[0 for node in graph.nodes] for node in graph.nodes]

    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adjacency_matrix[node1][node2] += 1

        if not graph.directed:
            adjacency_matrix[node2][node1] += 1

    return adjacency_matrix


def render_graph(graph):
    g = Network(directed=graph.directed)
    for i in range(len(graph.nodes)):
        g.add_node(graph.nodes[i], label=str(i))
    g.add_edges(graph.edges)
    g.show(str(graph.type)+".html")
    return g

def render_graph_matplotlib(edges_type):

    if edges_type[1]:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    #minimum_spanning_edges(G)
    G.add_edges_from(edges_type[0])
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    nx.draw_networkx_labels(G, pos)
    plt.show()


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    if root is None:
        if isinstance(G, nx.DiGraph):
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):

        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc - vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)


def draw_tree_matplotlib(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = hierarchy_pos(G, 1)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
    plt.show()


