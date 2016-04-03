from BinarySearchTree import*

__author__ = 'Danylo'


def construct_bst(inorder):
    if inorder is None or len(inorder) == 0:
        return None

    n = len(inorder)

    if n == 1:
        return BstNode(inorder[0])

    mid = n / 2
    root = BstNode(inorder[mid])

    root.left = construct_bst(inorder[0:mid])
    root.right = construct_bst(inorder[mid+1:n])

    return root

inorder_traversal = [1, 2, 4, 5, 8, 9, 11, 12, 13, 14, 18, 21, 25]
bst = construct_bst(inorder_traversal)

print_inorder(bst)

