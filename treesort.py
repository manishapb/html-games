import pprint

ul = [7, 3, -1, 2, 6, 9]


def add_node(tree, item):
    if item < tree['val']:
        if tree['lchild']:
            add_node(tree['lchild'], item)
        else:
            tree['lchild'] = {'val': item, 'lchild': None, 'rchild': None}
    else:
        if tree['rchild']:
            add_node(tree['rchild'], item)
        else:
            tree['rchild'] = {'val': item, 'lchild': None, 'rchild': None}

def create_tree(ul):
    root = {'val': ul[0],
            'lchild': None,
            'rchild': None}

    for item in ul[1:]:
        add_node(root, item)

    return root

def traverse_tree(tree):
    if not tree:
        return [] 
    else:
        return traverse_tree(tree['lchild']) + [tree['val']] + traverse_tree(tree['rchild'])

def tree_sort(ul):
    tree = create_tree(ul)
    sl = traverse_tree(tree)

    return sl

print(tree_sort(ul))
