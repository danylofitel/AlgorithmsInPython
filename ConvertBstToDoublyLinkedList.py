from BinarySearchTree import BstNode
from LinkedList import DllNode

__author__ = 'Danylo'


# Think of the similarity between a sorted doubly linked list and a perfect
# or full binary search tree. Imagine each node in the binary tree has a parent pointer.
# Implement the algorithm to convert the binary search tree to a sorted doubly linked list.


def convert_bst_to_list(tree):
    if tree is None:
        return None
    return convert_impl(tree)[0]


def convert_impl(tree):
    if tree is None:
        return None

    current = DllNode(tree.value)

    left_list = convert_impl(tree.left)
    right_list = convert_impl(tree.right)

    new_start = current
    new_finish = current

    if left_list:
        left_list[1].nxt = current
        current.prv = left_list[1].nxt
        new_start = left_list[0]

    if right_list:
        right_list[0].prv = current
        current.nxt = right_list[0]
        new_finish = right_list[1]

    return new_start, new_finish


root = BstNode(10)

root.left = BstNode(5)
root.right = BstNode(15)

root.left.left = BstNode(2)
root.left.right = BstNode(7)

root.right.left = BstNode(12)
root.right.right = BstNode(17)

sorted_list = convert_bst_to_list(root)
pointer = sorted_list

while pointer:
    print pointer.value
    pointer = pointer.nxt
