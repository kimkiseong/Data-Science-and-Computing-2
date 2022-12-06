#구조체 생성
from logging import root


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None
    
    #트리 삽입
    def insert(self, n1,n2,n3):
        self.current_node = self.root
        res = 1
        
        if self.root.data == n1:
            data2 = Node(n2)
            data3 = Node(n3)
            self.root.left = data2.data
            self.root.right = data3.data           
            return 0;
        if res and self.root.left:
            res = insert(self.root.left, n1,n2,n3)
                
        while True:
            if self.current_node.left != None:
                self.current_node = self.current_node.left
            else:
                self.current_node.left = Node(n1)
                break


        
        
    def preorder(self, n):
        if n != None:
            print(n.data,'', end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

#이진트리 생성
tree = BinaryTree()
tree.insert(10,20,30)


tree.preorder(tree.root)
