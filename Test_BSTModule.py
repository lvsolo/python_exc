#test for BST Module

from BSTModule import Treenode

from BSTModule import Tree

t0=Tree()
t1=Tree(1)
t2=Tree()
print t0.isEmpty(),t1.isEmpty(),'\n'
i=1
while i <10:
    t0.insertNode(i)
    i+=1
print t0.isEmpty()

t0.inOrderTraversal()

t0.preOrderTraversal()

t0.postOrderTraversal()

t_test=[5,4,6,7,2,1,8,9,3]

for tt in t_test:
    t2.insertNode(tt)

t2.inOrderTraversal()

t2.preOrderTraversal()

t2.postOrderTraversal()


