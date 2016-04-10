from BinarySearchTree import BstNode


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


root = BstNode(9)

root.left = BstNode(5)
root.right = BstNode(15)

root.left.left = BstNode(3)
root.left.right = BstNode(7)

root.right.left = BstNode(12)
root.right.right = BstNode(20)

print_right_view(root)
