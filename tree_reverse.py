#http://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree-in-python
class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

#左右其实只对显示顺序有意义
def invertBinaryChange(root):
    if root is None:
        return None
    if root.left:
        invertBinaryChange(root.left)
    if root.right:
        invertBinaryChange(root.right)
    root.left, root.right = root.right, root.left
    return root

 


def printTree(tree):
        if tree != None:
            printTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printTree(tree.getRightChild())







# test tree

def testTree():
    myTree = BinaryTree("1")
    myTree.insertLeft("2")
    myTree.insertRight("3")
    myTree.insertRight("4")
    printTree(myTree)
    print('*'*10)
    mytree = invertBinaryChange(myTree)
    printTree(myTree)


def main():
    testTree()

        
if __name__ == "__main__":
    main()
