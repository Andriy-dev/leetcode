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
        print(f"Stack={stack}")
        node,min_val,max_val = stack.pop()

        print(f"  node={node.val},min_val={min_val},max_val={max_val}")
        if node.left:
            print(f"  {node.val}.left exist")
            print(f"  {node.left.val} >= {node.val} {node.left.val} <= {min_val}")
            if node.left.val >= node.val or node.left.val <= min_val:
                return False
            print(f"  appnding stack ({node.left.val},{min_val},{node.val}) [ node.val={node.val} as a max_val]")
            stack.append(( node.left, min_val, node.val))

        if node.right:
            print(f"  {node.val}.right exist")
            print(f"  {node.right.val} <= {node.val} {node.right.val} >= {max_val}")
            if node.right.val <= node.val or node.right.val >= max_val:
                return False
            print(f"  appnding stack ({node.right.val},{node.val},{max_val}) [ node.val={node.val} as a min_val]")   
            stack.append((node.right, node.val, max_val))

    return True

if __name__=='__main__':

    root = Node(10)

    root.left = Node(5)
    root.right = Node(15)

    root.left.left = Node(3)
    root.left.right = Node(7)

    root.left.right.left = Node(6)
    root.left.right.right = Node(8)

    root.left.left.left = Node(1)
    root.left.left.right = Node(4)

    root.right.right = Node(20)
    root.right.left = Node(12)

    root.right.right.right = Node(25)
    root.right.right.left = Node(18)

    print(root)

    print(inorder(root))

