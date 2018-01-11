import random
import networkx as nx
from numpy import array
from csu.excess_average_degree import excess
from csu.excess_average_degree import excess_distribution


def rand_loc(loc_range):  # random location in a matrix
    x = random.randint(0, loc_range)
    y = random.randint(0, loc_range)
    while y == x:
        y = random.randint(0, loc_range)
    return tuple([x, y])


def is_loc_equal(loc1, loc2):  # to judge whether the two location refer to the same edge
    if (loc1[0] == loc2[0] and loc1[1] == loc2[1]) or (loc1[0] == loc2[1] and loc1[1] == loc2[0]):
        return True
    else:
        return False


def m_degree(matrix, node):  # calculate the degree of node in matrix
    d = 0
    for i in range(len(array(matrix)[0])):
        if matrix[node, i]:
            d = d + 1
    return d


def add_num(li):
    res = []
    for i in range(len(li)):
        res.append(tuple([i, li[i]]))
    return res


def print_attr(g):
    N = int(len(g.nodes))  # Number of nodes
    M = int(len(g.edges))  # Number of edges
    K = (2 * M) / N  # Average degree
    Pk = add_num(nx.degree_histogram(g))  # Degree distribution
    Kn = excess(g)  # Excess average degree
    Pnk = excess_distribution(g)
    L = nx.average_shortest_path_length(g)  # Average path length
    C = nx.average_clustering(g)  # Clustering coefficient
    # ##################################################
    print("Number of nodes(N): ", N)
    print("Number of edges(M): ", M)
    print("Average degree(<k>): ", K)
    print("Degree distribution(P(k)): ", Pk)
    print("Excess average degree(<Kn>): ", Kn)
    print("Excess average degree distribution(Pn(k)): ", Pnk)
    print("Average path length(L): ", L)
    print("Clustering coefficient(C): ", C)
