__author__ = 'Danylo'

# http://www.geeksforgeeks.org/check-if-a-given-array-can-represent-preorder-traversal-of-binary-search-tree/
# Check if a given array can represent Preorder Traversal of Binary Search Tree
# Given an array of numbers, return true if given array can represent preorder traversal
# of a Binary Search Tree, else return false. Expected time complexity is O(n).


def array_represents_preorder_bst(array):
    stack = []
    root = float("-inf")

    for x in array:
        if x < root:
            return False

        while len(stack) > 0 and stack[-1] < x:
            root = stack.pop()

        stack.append(x)

    return True

print(array_represents_preorder_bst([2, 4, 3]))
print(array_represents_preorder_bst([2, 4, 1]))
print(array_represents_preorder_bst([40, 30, 35, 80, 100]))
print(array_represents_preorder_bst([40, 30, 35, 20, 80, 100]))
