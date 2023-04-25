'''
relop module
'''

from geometor.utils import *
from geometor.model import *
from geometor.render import *

from .seeds import *

import graphviz

#  from itertools import permutations

sp.init_printing()

def get_digraph(name: str) -> graphviz.Digraph:
    """return a configured digraph

    :name: TODO
    :returns: TODO

    """
    dot = graphviz.Digraph(name, format='png')
    #  dot.engine = 'circo'
    dot.attr('graph', bgcolor='black')
    dot.attr('node', fontcolor='white')
    dot.attr('node', color='white')
    #  dot.attr('node', shape='point')
    dot.attr('node', shape='rect')
    dot.attr('edge', color='#666666')
    dot.attr('edge', arrowsize='1')
    return dot


def generate(seed, num):
    rows = [seed]
    for i in range(num):
        last_row = rows[-1]
        new_row = []
        for j, node in enumerate(last_row):
            new_row.append(node)
            if j + 1 in range(len(last_row)) :
                new_node = node + last_row[j+1]
                new_row.append(new_node)

        rows.append(new_row)
    return rows

def generate_2(seed, num):
    rows = [seed]
    for i in range(num):
        last_row = rows[-1]
        new_row = []
        for j, node in enumerate(last_row):
            new_row.append(node)
            if j + 1 in range(len(last_row)) :
                new_node = [node, last_row[j+1]]
                new_row.append(new_node)

        rows.append(new_row)
    return rows

def generate_graph(seed_key, seed, num):
    graph = get_digraph(f'{seed_key}-{num}')
    rows = [seed]

    for i, node in enumerate(seed):
        graph.node(f'0.{i}', label=node)

    for i in range(num):
        level = len(rows) - 1
        last_row = rows[-1]
        new_row = []
        for j, node in enumerate(last_row):
            parent_name = f'{level}.{j}'
            child_name = f'{level + 1}.{len(new_row)}'
            label = graphviz.nohtml(node)
            graph.node(child_name, label=label)
            graph.edge(parent_name, child_name)
            new_row.append(node)
            if j + 1 in range(len(last_row)) :
                new_node = node + last_row[j+1]
                child_name = f'{level + 1}.{len(new_row)}'
                label = graphviz.nohtml(new_node)
                graph.node(child_name, label=label)
                graph.edge(parent_name, child_name)
                parent_name_2 = f'{level}.{j+1}'
                graph.edge(parent_name_2, child_name)

                new_row.append(new_node)

        rows.append(new_row)
    return graph

