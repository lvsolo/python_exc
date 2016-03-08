#define the class "stack" which means in this data stucture ,
#the last-push data pops first
#including functions:
#pop(),push(),isEmpty(),__init__(),__str__()
#class Node(object):
from ListModule import Node
from ListModule import linkedList

class Stack(linkedList):
    def __init__(self,value=None):
        #self.push(value)
        node=Node(value)
        self._firstNode=node
        self._lastNode=node
        
    def push(self,value):
        self.insertAtFront(value)

    def pop(self):
        self.removeFromFront()

    def isEmpty(self):
        return self._firstNode is None

    def __str__(self):
        if self.isEmpty():
            return "empty"
        else:
            output=[]
            currentNode=self._firstNode
            while currentNode is not None:
                output.append(str(currentNode.data))
                currentNode=currentNode.nextNode

        return ' '.join(output)
##        currentNode=self._firstNode
##        if self.isEmpty():
##            raise IndexError,"trying to print an empty stack"
##        else:
##            print currentNode
##            
##        while currentNode is not self._lastNode:
##            print cuurrentNode,"\n"
##            currentNode=currentNode.nextNode

    
