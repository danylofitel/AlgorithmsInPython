__author__ = 'Danylo'


# Binary search tree structure and common routines


class BstNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BstWithParentNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def print_preorder(tree):
    if tree is None:
        return

    print tree.value
    print_preorder(tree.left)
    print_preorder(tree.right)


def print_inorder(tree):
    if tree is None:
        return

    print_inorder(tree.left)
    print tree.value
    print_inorder(tree.right)


def print_postorder(tree):
    if tree is None:
        return

    print_postorder(tree.left)
    print_postorder(tree.right)
    print tree.value


def print_level_order(tree):
    if tree is None:
        return

    queue = tree

    while len(queue) != 0:
        node = queue.pop(0)
        print node.value

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return
