'''
generate a relational operator series

'''

from relop import *


seed_key = "2c"
seed = SEEDS[seed_key]
num = 5

rows = generate(seed, num)

log_name = f'{seed_key}-{num}.log'
with open(log_name, 'w') as f:
    f.write(f'seed_key: {seed_key}\n')
    f.write(f'seed: {seed}\n')
    f.write(f'num: {num}\n')
    f.write('---\n')
    for i, row in enumerate(rows):
        f.write(f'{i}\n')
        
        for j, node in enumerate(row):
            f.write(f'    {j: >5}: {node}\n')

with open(log_name, 'r') as f:
    print(f.read())
