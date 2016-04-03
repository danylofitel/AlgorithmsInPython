from BinarySearchTree import BstNode

__author__ = 'Danylo'


# http://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/


class Info:
    def __init__(self, size, max, min, res):
        self.size = size
        self.max = max
        self.min = min
        self.res = res


def largest_bst_subtree(tree):
    result = Info(1, tree.value, tree.value, 1)

    if tree.left:
        left_result = largest_bst_subtree(tree.left)
        if left_result.max <= result.min:
            result.size += left_result.size
            result.min = left_result.min
        result.res = max(result.res, max(result.size, left_result.res))

    if tree.right:
        right_result = largest_bst_subtree(tree.right)
        if right_result.min >= result.max:
            result.size += right_result.size
            result.max = right_result.max
        result.res = max(result.res, max(result.size, right_result.res))

    return result


root = BstNode(50)

root.left = BstNode(30)
root.right = BstNode(60)

root.left.left = BstNode(5)
root.left.right = BstNode(20)

root.right.left = BstNode(45)
root.right.right = BstNode(70)

root.right.right.left = BstNode(65)
root.right.right.right = BstNode(80)

print largest_bst_subtree(root).res
