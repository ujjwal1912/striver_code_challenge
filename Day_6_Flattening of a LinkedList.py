# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
# Note: The flattened list will be printed using the bottom pointer instead of next pointer.

def merge(a, b):
    if(a == None):
        return b
    if(b == None):
        return a
    result = None
    if (a.data < b.data):
        result = a
        result.bottom = merge(a.bottom,b)
    else:
        result = b
        result.bottom = merge(a,b.bottom)
    result.next = None
    return result

def flatten(root):
    if(root == None or root.next == None):
        return root
    root.next = flatten(root.next)
    root = merge(root, root.next)
    return root
