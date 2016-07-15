from BinarySearchTree import BstNode

__author__ = 'Danylo'


def is_bst(tree):
    if tree is None:
        return False

    return subtree_is_bst(tree, float('-inf'), float('inf'))


def subtree_is_bst(subtree, lower, upper):
    if subtree is None:
        return True
    elif subtree.value <= lower or subtree.value >= upper:
        return False

    new_lower = max(lower, subtree.value)
    new_upper = min(upper, subtree.value)

    return subtree_is_bst(subtree.left, lower, new_upper) \
           and subtree_is_bst(subtree.right, new_lower, upper)


root = BstNode(10)

root.left = BstNode(5)
root.right = BstNode(15)

root.left.left = BstNode(2)
root.left.right = BstNode(7)

root.right.left = BstNode(12)
root.right.right = BstNode(17)

root.left.right.left = BstNode(4)

print(is_bst(root))
