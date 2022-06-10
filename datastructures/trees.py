from graphs import *
#perfect_tree , balanced_tree , complete_tree , full_tree

def perfect_tree(num_nodes):
    edges = []
    cnt = 1
    for i in range(1,num_nodes):

        edges.append((cnt, cnt*2))
        edges.append((cnt, cnt*2 + 1))
        cnt +=1

    return edges


def balanced_tree(num_nodes):
    edges = []
    cnt = 1
    od =  1
    for i in range(num_nodes-1):
        if cnt == 1 or cnt == 2:
            edges.append((cnt, cnt * 2))
            edges.append((cnt, cnt * 2 + 1))
        else:
            if cnt % 2 == 1:
                edges.append((cnt, cnt * 2))
            elif cnt % 2 == 0:
                edges.append((cnt, cnt * 2 + 1))
                if od % 2 == 1:
                    cnt += 1
                else:
                    cnt -=2
                od +=1
        cnt += 1

    return edges


def complete_tree(num_nodes):
    edges = []
    cnt = 1
    nodes_num = (num_nodes-1)*2 + 1
    lev = 1
    if nodes_num > 1:
        lev =2
    elif nodes_num > 3:
        lev = 3
    elif nodes_num > 7:
        lev = 4
    print(nodes_num)

    for i in range(num_nodes-1):
        if cnt *2 == nodes_num-1:

            edges.append((cnt, cnt * 2))
        else:
            edges.append((cnt, cnt * 2))
            edges.append((cnt, cnt * 2 + 1))
        cnt += 1

    return edges


def full_tree(num_nodes):
    edges = []
    cnt = 1
    for i in range(num_nodes-1):

        edges.append((cnt, cnt * 2))
        edges.append((cnt, cnt * 2 + 1))
        cnt += 1

    return edges

#edges = complete_tree(7)
#print(edges)
#draw_tree_matplotlib(edges)
#draw_tree_matplotlib([(1,2),(2,1)])

