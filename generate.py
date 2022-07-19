'''
generate a relational operator series

'''

from relop import *



seed = ['<', '>']
num = 10


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
        

rows = generate(seed, num)

with open('generate.log', 'w') as f:
    f.write(f'seed: {seed}\n')
    f.write(f'num: {num}\n')
    f.write('---\n')
    for i, row in enumerate(rows):
        f.write(f'{i}\n')
        
        for j, node in enumerate(row):
            f.write(f'    {j: >5}: {node}\n')
