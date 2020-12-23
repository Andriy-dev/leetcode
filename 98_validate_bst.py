#!/usr/bin/python3
'''
https://leetcode.com/problems/validate-binary-search-tree/
'''

from binarytree import tree, bst, heap, Node

def inorder(root,traversal=[]):
    if root is None:
        return None

    stack = [ (root,float('-inf'),float('inf')) ]

    while stack:
        node,min_val,max_val = stack.pop()

        if node.left:
            if node.left.val >= node.val or node.left.val <= min_val:
                return False
            stack.append(( node.left, min_val, node.val))

        if node.right:
            if node.right.val <= node.val or node.right.val >= max_val:
                return False
            stack.append((node.right, node.val, max_val))

    return True

if __name__=='__main__':

    root = Node(5)

    root.left = Node(1)
    root.right = Node(4)

    root.right.left = Node(3)
    root.right.right = Node(6)


    print(root)

    print(inorder(root))

