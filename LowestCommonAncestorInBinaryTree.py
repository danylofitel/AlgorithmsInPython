from BinarySearchTree import BstNode

__author__ = 'Danylo'


# http://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/
# Given a binary tree (not a binary search tree) and two values say n1 and n2,
# write a program to find the least common ancestor.


def common_ancestor_linear_space(tree_root, first, second):
    first_path = common_ancestor_ls(tree_root, first, [])
    second_path = common_ancestor_ls(tree_root, second, [])

    if first_path is None or second_path is None:
        return None

    return common_path(first_path, second_path)[-1]


def common_ancestor_ls(tree_root, elem, path):
    if tree_root is None:
        return None

    path.append(tree_root)
    if tree_root.value == elem:
        return path

    left_result = common_ancestor_ls(tree_root.left, elem, path)
    if left_result is not None:
        return left_result

    right_result = common_ancestor_ls(tree_root.right, elem, path)
    if right_result is not None:
        return right_result

    del path[-1]
    return None


def common_path(first, second):
    common = []
    for i in range(0, len(first)):
        if first[i] != second[i]:
            return common
        common.append(first[i])


def common_ancestor_constant_space(root, first, second):
    if root is None:
        return None

    if root.value == first or root.value == second:
        return root

    left = common_ancestor_constant_space(root.left, first, second)
    right = common_ancestor_constant_space(root.right, first, second)

    if left and right:
        return root

    return left if left is not None else right


root = BstNode(9)

root.left = BstNode(5)
root.right = BstNode(15)

root.left.left = BstNode(3)
root.left.right = BstNode(7)

root.right.left = BstNode(12)
root.right.right = BstNode(20)

print(common_ancestor_linear_space(root, 3, 7).value)
print(common_ancestor_constant_space(root, 3, 7).value)
