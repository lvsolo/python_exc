#realize the data structure called BST--bi-search tree
#including the class Treenode and Tree
#Treenode.data ,.left,.right
#Tree.insertNode(),.insertNodeHelper(),.preOrderTraversal(),.preOrderHelper(),.
#.inOrderHelper(),.postOrderTraversal(),.postOrderHelper()
class Treenode(object):

    def __init__(self,value=None):
        self.data=value
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)

    def isEmpty(self):
        return self.data is None

class Tree(object):

    def __init__(self,value=None):

        node=Treenode(value)
        self._rootNode=node

##    def __str__(self):
##
##        currentNode=self._rootNode
##        while currentNode is not None:
##            print curentNode.data
##            currentNode

    def insertNode(self,value):

        #node=Treenode(value)
####        if self.isEmpty():
####            self._rootNode=Treenode(value)
####        else:
            self.insertNodeHelper(self._rootNode,value)

    def insertNodeHelper(self,node,value):
        
####        if value <node.data:
####
####            if node.left is None:
####                node.left=Treenode(value)
####            else:
####                self.insertNodeHelper(node.left,value)
####
####        elif value >node.data:
####
####            if node.right is None:
####                node.right=Treenode(value)
####            else:
####                self.insertNodeHelper(node.right,value)
####
####        else:
####            print value,'diplicate'


        if node.data is None:
            #node=Treenode(value)
            node.data=value
            #print "insert accomplished"
            #return "insert accomplished"
        elif value<node.data:
            if node.left is not None:
                self.insertNodeHelper(node.left,value)
            else:
                node.left=Treenode(value)
        elif value>node.data:
            if node.right is not None:
                self.insertNodeHelper(node.right,value)
            else:
                node.right=Treenode(value)
        else:
            print value,"duplicate"

    def isEmpty(self):
        
        return self._rootNode.isEmpty()

    def inOrderTraversal(self):
        self.inOrderHelper(self._rootNode)
        print "Traversal ends",'\n'

    def inOrderHelper(self,node):
        if node is not None:
            self.inOrderHelper(node.left)
            self.inOrderHelper(node.right)
            print str(node.data),

    def preOrderTraversal(self):
        if self._rootNode.isEmpty():
            print 'trying to print an empty BST\n'
        else:
            self.preOrderHelper(self._rootNode)
    def preOrderHelper(self,node):
        print node,
        if node.left is not None:
            self.preOrderHelper(node.left)
        if node.right is not None:
            self.preOrderHelper(node.right)
        
    def postOrderTraversal(self):
        if self._rootNode.isEmpty():
            print "trying to traversal an empty BST in post order"
        else:
            postOrderHelper(self,node)

    
    def postOrderHelper(self,node):
        
