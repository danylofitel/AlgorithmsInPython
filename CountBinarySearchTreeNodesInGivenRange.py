from BinarySearchTree import BstNode

__author__ = 'Danylo'


# http://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/
# Count BST nodes that lie in a given range
# Given a Binary Search Tree (BST) and a range, count number of nodes that lie in the given range.


def count_nodes_in_range(tree, left, right):
    if tree is None:
        return 0

    count = 0

    if left <= tree.value <= right:
        count += 1

    if tree.left is not None and tree.value > left:
        count += count_nodes_in_range(tree.left, left, right)

    if tree.right is not None and tree.value < right:
        count += count_nodes_in_range(tree.right, left, right)

    return count

root = BstNode(9)

root.left = BstNode(5)
root.right = BstNode(15)

root.left.left = BstNode(3)
root.left.right = BstNode(7)

root.right.left = BstNode(12)
root.right.right = BstNode(20)

print count_nodes_in_range(root, 7, 20)
