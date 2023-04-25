'''
generate Stern Brocot tree

from https://stackoverflow.com/a/69211833/8968340
'''


def sb_tree(rn, n):
    if not n:
        return rn
    def new_rn():
        for i in range(len(rn) - 1):
            yield from (rn[i], tuple(map(sum, zip(rn[i], rn[i+1]))))
        yield rn[i+1]
    return sb_tree(list(new_rn()), n-1)

for i in range(5):
    print(list(sb_tree([(0,1), (1,0)], i)))
