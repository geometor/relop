'''
relop module
'''

from geometor.utils import *
from geometor.model import *
from geometor.render import *

from .seeds import *

#  from itertools import permutations

sp.init_printing()


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
        
