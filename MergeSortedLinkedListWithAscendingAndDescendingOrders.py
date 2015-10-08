__author__ = 'Danylo'


# http://www.geeksforgeeks.org/how-to-sort-a-linked-list-that-is-sorted-alternating-ascending-and-descending-orders/
# Sort a linked list that is sorted alternating ascending and descending orders?
# Given a Linked List. The Linked List is in alternating ascending and descending orders.
# Sort the list efficiently.


class Node:
    def __init__(self, value, ptr):
        self.value = value
        self.ptr = ptr


def revert(lst):
    if lst is None:
        return None

    ptr = lst
    lst = None
    while ptr.ptr is not None:
        tmp = ptr.ptr
        ptr.ptr = lst
        lst = ptr
        ptr = tmp

    ptr.ptr = lst

    return ptr


def merge(asc, desc):
    if asc is None or desc is None:
        return None

    desc = revert(desc)

    if asc.value > desc.value:
        merged = asc
        remaining = desc
    else:
        merged = desc
        remaining = asc

    p_merged = merged
    if p_merged.value > remaining.value:
        tmp = p_merged.value
        p_merged.value = remaining.value
        remaining.value = tmp

    while remaining is not None:
        if p_merged.ptr.value < remaining.value:
            p_merged = p_merged.ptr
        else:
            new = remaining
            remaining = remaining.ptr

            tmp = p_merged.ptr
            p_merged.ptr = new
            new.ptr = tmp

    return merged




desc = Node(17, Node(15, Node(13, Node(11, Node(9, Node(7, Node(5, Node(3, Node(1, None)))))))))
asc = Node(0, Node(2, Node(4, Node(6, Node(8, Node(10, Node(12, Node(14, Node(16, None)))))))))

merged = merge(asc, desc)
while merged.ptr is not None:
    print merged.value
    merged = merged.ptr

print merged.value
