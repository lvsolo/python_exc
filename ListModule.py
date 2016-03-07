#Linked list
#including the function:
#insertAtFront();
#insertAtBack()
#removeFromFront()
#removeFromBack()
class Node(object):
    
    def __init__(self,data):
        
        self.data=data
        self.nextNode=None

    def __str__(self):
        
        return self.data
        
class linkedList(object):
    
    def __init__(self):
        
        self._firstNode=None
        self._lastNode=None

    def insertAtFront(self,value):
        
        node=Node(value)
            
        if(self.isEmpty()):
            node.nextNode=None
            self._firstNode=node
            self._lastNode=node
        else:
            node.nextNode=self._firstNode
            self._firstNode=node

    def insertAtBack(self,value):
        
        node=Node(value)
            
        if self.isEmpty():
            self._firstNode=node
            self._lastNode=node
        else:
            self._lastNode.nextNode=node
            self._lastNode=node

    def removeFromFront(self):
        
        tempNode=self._firstNode
        
        if self.isEmpty():
            raise IndexError,"remove from empty list"
        elif(self._firstNode is self._lastNode):
            self._firstNode=None
            self._lastNode=None
        else:
            self._firstNode=self._firstNode.nextNode

        return tempNode
    
    def removeFromBack(self):
        
        tempNode=self._lastNode
        
        if self.isEmpty():
            raise IndexError,"remove from empty list"
        
        elif self._firstNode is self._lastNode:
            self._firstNode=self._lastNode=None

        else:
            currentNode=self._firstNode
            
        while currentNode.nextNode is not self._lastNode:
            currentNode=currentNode.nextNode

            currentNode.nextNode=None
            self._lastNode=currentNode

        return tempNode
    
    def isEmpty(self):
        return self._firstNode is None

    def __str__(self):
            currentNode=self._firstNode
            while currentNode is not None:
                    print currentNode.data
                    print '\n'
                    currentNode=currentNode.nextNode             
