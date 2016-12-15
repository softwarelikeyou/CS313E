OPERATORS = ['+', '-', '*', '/']

class Operator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def truediv(self, a, b):
        return a / b
            
class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class BinaryTree:
    PREORDER = ''
    POSTORDER = ''
    
    def __init__(self, initVal):
        self.data = initVal
        self.left = None
        self.right = None
        
    def createTree (self, expr):
        self.data = None
        self.left = None
        self.right = None

        stack = Stack()
        stack.push(self)
        
        for token in expr.split():
            if token == ')':
                self = stack.pop()
            elif token == '(':
                self.insertLeft('')
                stack.push(self)
                self = self.getLeftChild()
            elif token in OPERATORS:
                self.setRootVal(token)
                self.insertRight('')
                stack.push(self)
                self = self.getRightChild()
            else:
                if self.isFloat(token):
                    self.setRootVal(float(token))
                else:
                    self.setRootVal(int(token))
                parent = stack.pop()
                self = parent
            
    def evaluate (self, root):
        operator = Operator()
        opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

        leftC = root.getLeftChild()
        rightC = root.getRightChild()

        if leftC and rightC:
            fn = opers[root.getRootVal()]
            return fn(self.evaluate(leftC), self.evaluate(rightC))
        else:
            return root.getRootVal()
    
    def preOrder(self, root):
        if root:
            self.PREORDER += str(root.getRootVal()) + ' '
            self.preOrder(root.getLeftChild())
            self.preOrder(root.getRightChild())
    
    def postOrder(self, root):
        if root != None:
            self.postOrder(root.getLeftChild())
            self.postOrder(root.getRightChild())
            self.POSTORDER += str(root.getRootVal()) + ' '

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self,value):
        self.data = value

    def getRootVal(self):
        return self.data
    
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
         
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def isFloat(self, value):
        if '.' in value:
            return True
        else:
            return False
    
def main():
    in_file = open ('treedata.txt', 'r')
    for expr in in_file:
        bTree = BinaryTree(None)
        bTree.createTree(expr)
        print('Infix expression: ' + expr)
        print('    Value:   ' + str(bTree.evaluate(bTree)))
        bTree.PREORDER = ''
        bTree.preOrder(bTree)
        print('    Prefix expression:   ' + bTree.PREORDER)
        bTree.POSTORDER = ''
        bTree.postOrder(bTree)
        print('    Postfix expression:  ' + bTree.POSTORDER)
        print()
    in_file.close()
    
main()
