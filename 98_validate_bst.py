#!/usr/bin/python3
'''
https://leetcode.com/problems/validate-binary-search-tree/
'''

from binarytree import tree, bst, heap, Node

def inorder(root,traversal=[]):
    if root is None:
        return None

    if root.left:
        inorder(root.left)
            
   
    traversal.append(root.value)

    if root.right:
        inorder(root.right)

    if len(traversal) == 1:
        return True    

    return(all([traversal[i] < traversal[i+1] for i in range(len(traversal) - 1)]))

if __name__=='__main__':

    root = Node(5)

    root.left = Node(1)
    root.right = Node(4)

    root.right.left = Node(3)
    root.right.right = Node(6)


    print(root)

    print(inorder(root))

