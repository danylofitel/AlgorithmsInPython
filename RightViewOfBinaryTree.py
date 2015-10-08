from BST import Node

__author__ = 'Danylo'


# http://www.geeksforgeeks.org/print-right-view-binary-tree-2/
# Print Right View of a Binary Tree
# Given a Binary Tree, print Right view of it.
# Right view of a Binary Tree is set of nodes visible when tree is visited from Right side.


def print_right_view_help(tree, level, max_level):
    if tree is None:
        return max_level

    if level > max_level:
        print tree.value
        max_level = level

    max_level = max(max_level, print_right_view_help(tree.right, level + 1, max_level))
    max_level = max(max_level, print_right_view_help(tree.left, level + 1, max_level))

    return max_level


def print_right_view(tree):
    print_right_view_help(tree, 1, 0)


root = Node(9)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(3)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)

print_right_view(root)
