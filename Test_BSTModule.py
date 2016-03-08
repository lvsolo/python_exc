#test for BST Module

from BSTModule import Treenode

from BSTModule import Tree

t0=Tree()
t1=Tree(1)
print t0.isEmpty(),t1.isEmpty(),'\n'
i=1
while i <10:
    t0.insertNode(i)
    i+=1
print t0.isEmpty()

t0.inOrderTraversal()

t0.preOrderTraversal()

    


