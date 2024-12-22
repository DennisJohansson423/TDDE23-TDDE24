from tree import *


def empty_tree_fn():
  return 0


def leaf_fn(key):
  return key**2


def inner_node_fn(key, left_value, right_value):
  return key + left_value


def traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn):
  """
  Calculate the value of the inner node, if a inner node exist.
  """
  if is_empty_tree(tree):
    return empty_tree_fn()
  elif is_leaf(tree):
    return leaf_fn(tree)
  else:
    left_subttree = left_subtree(tree)
    right_subttree = right_subtree(tree)
    center_value = center_tree(tree)
    
    left_value = traverse(left_subttree, inner_node_fn, leaf_fn, empty_tree_fn)
    right_value = traverse(right_subttree, inner_node_fn, leaf_fn,
                           empty_tree_fn)
    return inner_node_fn(center_value, left_value, right_value)


def test_traverse():
  """
  Test the traverse func.
  """
  tree_lists = [[], [1, 1, 1], [0, 0, 0], [-1, -1, -1], [6, 7, 8],
                 [-2, 2, 1]]

  expected_results = [(0), (2), (0), (0), (43), (6)]

  for tree, expected in zip(tree_lists, expected_results):
    assert (traverse(tree, inner_node_fn, leaf_fn,
                     empty_tree_fn) == expected), "Expected {} got {} ".format(
                       expected, str(traverse(tree,inner_node_fn, leaf_fn,
                     empty_tree_fn)))

  print("The code passed all the traverses tests")


test_traverse()


## Contains_key section



def contains_key(key, tree):
  """
  Checks if the given tree contain a given key.
  """
  empty_tree_fn = lambda: False

  def inner_node_fn(center_value, left_value, right_value):
    """
    Goes trough the values given from traverse to
    check if a value matches the given key.
    """
    return key == center_value or left_value or right_value

  def leaf_fn(tree):
    return tree == key

  return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def test_contains_key():
  """
  Tests the contains_key func.
  """
  inputs_list = [
    [2, [6, 7, 8]],
    [6, [6, 7, 8]],
    [0, [0, 0, 0]],
    [1, [1, 1, 1]],
    [-1, [-1, -1, -1]],
    [2, [6, 7, [[2, 3, 4], 0, []]]],
    [2, [6, 7, [[3, 3, 4], 0, []]]],
    [5, [6, 7, [[3, 3, 4], 0, [0, 0, 5]]]],
    [1, [0, 0, 0]],
  ]

  expected_results = [(False), 
                      (True), 
                      (True), 
                      (True), 
                      (True), 
                      (True),
                      (False),
                      (True), 
                      (False)]

  for input, expected in zip(inputs_list, expected_results):
    assert (contains_key(input[0],input[1]) == expected), "Expected {} got {} ".format(
                           expected, str(contains_key(input[0], input[1])))
 
  print("The code passed all the contains_keys tests")


test_contains_key()


def tree_size(tree):
  """
  Calculate the total values of the leafes and the inner node.
  """
  def inner_node_fn(center_value, left_value, right_value):
    return left_value + 1 + right_value

  empty_tree_fn = lambda : False
  leaf_fn = lambda x: 1

  return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)


def test_tree_size():
  """
  Test the tree_size func.
  """
  tree_list = [[2, 7, []], [], [[1, 2, []], 4, [[], 5, 6]],
               [[1, 2, [1, 2, 2]], 4, [[], 5, 6]],
               [[1, 2, [[12, 2, 3], 2, 2]], 4, [[], 5, 6]], [1, 2, 1]]

  expected_results = [(2), (0), (5), (8), (10), (3)]
  for tree, expected in zip(tree_list, expected_results):
    assert (tree_size(tree) == expected), "Expected {} got {} ".format(
      expected, str(contains_key(tree)))
  print("The code passed all the tree_sizes tests")


test_tree_size()





def tree_depth(tree):
  """
  Find and calculates the biggest and longest road
  from the root to the last leaf.
  """
  def inner_node_fn(center_value, left_value, right_value):
    if left_value > right_value:
      return left_value + 1
    return right_value + 1

  empty_tree_fn = lambda : 0
  leaf_fn = lambda x: 1

  return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)




def test_tree_depth():
  """
  Test the tree_depth func.
  """
  tree_list = [
    0, 1, -1, [1, 2, 3], [1, 5, [10, 7, 14]], [1, 2, [[1, 2, 3], 7, 14]],
    [1, 2, []]
  ]

  expected_results = [(1), (1), (1), (2), (3), (4), (2)]

  for tree, expected in zip(tree_list, expected_results):
    assert (tree_size(tree) == expected), "Expected {} got {} ".format(
      expected, str(contains_key(tree)))
  print("The code passed all the tree_depth tests")



