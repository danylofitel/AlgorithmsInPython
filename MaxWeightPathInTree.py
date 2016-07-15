from BinarySearchTree import BstNode

__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/
# Find the maximum sum leaf to root path in a Binary Tree
# Given a Binary Tree, find the maximum sum path from a leaf to root.


def max_weight_path_from_root(tree):
    if tree is None:
        return None

    max_left = max_weight_path_from_root(tree.left)
    max_right = max_weight_path_from_root(tree.right)

    if (max_left is None) and (max_right is None):
        return tree.value

    max_weight = 0
    if max_left is None:
        max_weight = max_right
    elif max_right is None:
        max_weight = max_left
    else:
        max_weight = max_left
        if max_right > max_left:
            max_weight = max(max_right, 0)

    return tree.value + max_weight


# http://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/
# Find the maximum path sum between two leaves of a binary tree
# Given a binary tree in which each node element contains a number.
# Find the maximum possible sum from one leaf node to another.
# The maximum sum path may or may not go through root.
# Expected time complexity is O(n).


def max_weight_path_in_tree(tree):
    if tree is None:
        return None

    tree.max_path_down = tree.value
    tree.max_paths_down = tree.value

    max_left = 0
    max_right = 0

    if tree.left is not None:
        max_weight_path_in_tree(tree.left)
        if tree.left.max_path_down > 0:
            tree.max_path_down += tree.left.max_path_down
            tree.max_paths_down += tree.left.max_path_down
            max_left = tree.left.max_paths_down

    if tree.right is not None:
        max_weight_path_in_tree(tree.right)
        if tree.right.max_path_down > 0:
            tree.max_path_down = max(tree.max_path_down, tree.value + tree.right.max_path_down)
            tree.max_paths_down += tree.right.max_path_down
            max_right = tree.right.max_paths_down

    return max(max_left, tree.max_paths_down, max_right)


root = BstNode(1)

root.left = BstNode(0)

root.right = BstNode(10)

root.left.left = BstNode(100)

root.left.right = BstNode(30)

root.right.right = BstNode(90)

root.right.right.left = BstNode(10)

print(max_weight_path_from_root(root))

print(max_weight_path_in_tree(root))
