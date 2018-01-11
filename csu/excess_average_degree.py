def excess_each_node(g):  # excess average degree of each node in the network
    excess_average_degree_dict = {}
    # print(g.degree())
    for i in g.nodes:
        # excess_average_degreeList.append()
        # print(g.degree(i))
        neighbors = list(g.neighbors(i))
        # print(neighbors)
        neighbors_len = len(neighbors)
        neighbors_degree_sum = 0
        for j in neighbors:
            neighbors_degree_sum = neighbors_degree_sum + g.degree(j)
        excess_average_degree = neighbors_degree_sum / neighbors_len
        excess_average_degree_dict[i] = excess_average_degree
    return excess_average_degree_dict


def excess_each_degree(g):  # excess average degree of each degree in the network
    excess_average_degree_dict = {}

    excess_each_degree_sum = {}
    excess_each_degree_res = {}

    # print(g.degree())
    for i in g.nodes:
        # excess_average_degreeList.append()
        # print(g.degree(i))
        neighbors = list(g.neighbors(i))
        # print(neighbors)
        neighbors_len = len(neighbors)
        neighbors_degree_sum = 0
        for j in neighbors:
            neighbors_degree_sum = neighbors_degree_sum + g.degree(j)
        excess_average_degree = neighbors_degree_sum / neighbors_len
        excess_average_degree_dict[i] = excess_average_degree
    for k in g.nodes:
        if g.degree(k) in excess_each_degree_sum.keys():
            excess_each_degree_sum[g.degree(k)] = excess_each_degree_sum[g.degree(k)] + excess_average_degree_dict[k]
        else:
            excess_each_degree_sum[g.degree(k)] = 0
    for key in excess_each_degree_sum:
        excess_each_degree_res[key] = excess_each_degree_sum[key] / key
    return excess_each_degree_res


def excess(g):  # excess average degree of the whole network
    excess_average_degree_dict = {}
    res = 0
    # print(g.degree())
    for i in g.nodes:
        # excess_average_degreeList.append()
        # print(g.degree(i))
        neighbors = list(g.neighbors(i))
        # print(neighbors)
        neighbors_len = len(neighbors)
        neighbors_degree_sum = 0
        for j in neighbors:
            neighbors_degree_sum = neighbors_degree_sum + g.degree(j)
        if neighbors_len != 0:
            excess_average_degree = neighbors_degree_sum / neighbors_len
        else:
            excess_average_degree = 0
        excess_average_degree_dict[i] = excess_average_degree
    for key in excess_average_degree_dict:
        res = res + excess_average_degree_dict[key]
    res = res / len(g.nodes)
    return res


def excess_distribution(g):  # excess average degree distribution of the whole network
    excess_average_degree_distribution_dict = {}
    # print(g.degree())
    for i in g.nodes:
        neighbors = list(g.neighbors(i))
        for j in neighbors:
            if g.degree(j) in excess_average_degree_distribution_dict.keys():
                excess_average_degree_distribution_dict[g.degree(j)] = excess_average_degree_distribution_dict[g.degree(j)] + 1
            else:
                excess_average_degree_distribution_dict[g.degree(j)] = 1
    # sort
    res = []
    for key in sorted(excess_average_degree_distribution_dict.keys()):
        res.append(tuple([key, excess_average_degree_distribution_dict[key]]))
    return res
