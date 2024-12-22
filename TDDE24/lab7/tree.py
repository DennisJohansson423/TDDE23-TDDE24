def is_empty_tree(tree):
    return isinstance(tree, list) and not tree


def is_leaf(tree):
    return isinstance(tree, int)


def center_tree(tree):
    return tree[1]

	
def left_subtree(tree):
    return tree[0]


def right_subtree(tree):
    return tree[2]

