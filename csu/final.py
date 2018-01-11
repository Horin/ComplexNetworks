import csv
import networkx as nx

from csu.utils import print_attr
from csu.utils import is_loc_equal
from csu.utils import rand_loc
from csu.utils import m_degree

# file path of original network
filePath = "../test_data/data9.csv"

# initial graph and each indicators
G = nx.Graph()  # network
# read data and build the network
with open(filePath, newline='') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        G.add_edge(*row)

# ####################### The original network ##################################
print()
print("================== Indicators of the original network ==================")
print_attr(G)
print("================== Indicators of the original network ==================")
print()
# ###############################################################################


# ####################### The 0 order null model ################################
A0 = nx.to_numpy_matrix(G)

t = 0
while t < 100:
    ij = rand_loc(len(G.nodes) - 1)
    while A0[ij[0], ij[1]] != 1:
        ij = rand_loc(len(G.nodes) - 1)
    kl = rand_loc(len(G.nodes) - 1)
    while is_loc_equal(ij, kl) or (A0[kl[0], kl[1]] == 1):
        kl = rand_loc(len(G.nodes) - 1)
    A0[ij[0], ij[1]] = 0
    A0[ij[1], ij[0]] = 0
    A0[kl[0], kl[1]] = 1
    A0[kl[1], kl[0]] = 1
    t = t + 1

G0 = nx.from_numpy_matrix(A0)

print()
print("================== Indicators of the 0 order null model ==================")
print_attr(G0)
print("================== Indicators of the 0 order null model ==================")
print()
# ###############################################################################


# ####################### The 1 order null model ################################
A1 = nx.to_numpy_matrix(G)

t = 0
while t < 100:
    ij = rand_loc(len(G.nodes) - 1)
    while A1[ij[0], ij[1]] != 1:
        ij = rand_loc(len(G.nodes) - 1)
    kl = rand_loc(len(G.nodes) - 1)
    while is_loc_equal(ij, kl) or (A1[kl[0], kl[1]] != 1):
        kl = rand_loc(len(G.nodes) - 1)
    i = ij[0]
    j = ij[1]
    k = kl[0]
    l = kl[1]
    if (A1[i, k] != 1) \
            and (A1[i, l] != 1) \
            and (A1[j, k] != 1) \
            and (A1[j, l] != 1):
        # ###########
        A1[i, j] = 0
        A1[j, i] = 0
        A1[k, l] = 0
        A1[l, k] = 0
        # ###########
        A1[i, l] = 1
        A1[l, i] = 1
        A1[k, j] = 1
        A1[j, k] = 1
    t = t + 1

G1 = nx.from_numpy_matrix(A1)

print()
print("================== Indicators of the 1 order null model ==================")
print_attr(G1)
print("================== Indicators of the 1 order null model ==================")
print()
# ###############################################################################


# ####################### The 2 order null model ################################
A2 = nx.to_numpy_matrix(G)

t = 0
while t < 100:
    ij = rand_loc(len(G.nodes) - 1)
    while A2[ij[0], ij[1]] != 1:
        ij = rand_loc(len(G.nodes) - 1)
    kl = rand_loc(len(G.nodes) - 1)
    while is_loc_equal(ij, kl) or (A2[kl[0], kl[1]] != 1):
        kl = rand_loc(len(G.nodes) - 1)
    i = ij[0]
    j = ij[1]
    k = kl[0]
    l = kl[1]
    if (A2[i, k] != 1) \
            and (A2[i, l] != 1) \
            and (A2[j, k] != 1) \
            and (A2[j, l] != 1) \
            and (m_degree(A2, j) == m_degree(A2, l)):
        # ###########
        A2[i, j] = 0
        A2[j, i] = 0
        A2[k, l] = 0
        A2[l, k] = 0
        # ###########
        A2[i, l] = 1
        A2[l, i] = 1
        A2[k, j] = 1
        A2[j, k] = 1
    t = t + 1

G2 = nx.from_numpy_matrix(A2)

print()
print("================== Indicators of the 2 order null model ==================")
print_attr(G2)
print("================== Indicators of the 2 order null model ==================")
print()
# ###############################################################################
