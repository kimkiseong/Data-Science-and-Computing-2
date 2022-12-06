# 제자리 힙 정렬
class Heap:
    def __init__(self):
        self.queue = [0] * 100
        self.queue[0] = None
        self.last_index = 0
        # 리스트의 0번째 자리에 None 루트의 인덱스 번호를 1로 하기 위해

    def inPlaceHeapSort(self):
        self.buildHeapB()
        for i in range(self.last_index, 1, -1):
            temp = self.queue[1]
            self.queue[1] = self.queue[i]
            self.queue[i] = temp
            self.downHeap(1, i-1)
        return
    
    # 1기(B방식)    
    # 비재귀적 상향식 힙 생성
    def buildHeapB(self):
        for i in range(self.last_index//2, 0, -1):
            self.insertItem(i)
        return
    
    def insertItem(self,i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        if self.queue[left_index] == None and self.queue[right_index] == None:
            return
        bigger = left_index
        if self.queue[right_index] != None:
            if self.queue[right_index] > self.queue[bigger]:
                bigger = right_index
        if self.queue[i] >= self.queue[bigger]:
            return
        self.swapElements(i,bigger)
        self.insertItem(bigger)          
    
    #2기
    def downHeap(self, i, last):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        if left_index > last:
            return
        greater = left_index
        if right_index <= last:
            if self.queue[right_index] > self.queue[greater]:
                greater = right_index
        if self.queue[i] > self.queue[greater]:
            return
        self.swapElements(i, greater)
        self.downHeap(greater,last)
        

    def printHeap(self):
        print(" ", end='')
        for i in range(1, self.last_index+1):
            print(self.queue[i], end=' ')
        print()    

    #위치 바꿔주기
    def swapElements(self, i, parent_index):
        temp = self.queue[i]
        self.queue[i] = self.queue[parent_index]
        self.queue[parent_index] = temp
            
    #부모, 왼쪽, 오른쪽 위치 반환
    def parent(self, index):
        return index // 2
    
    def leftchild(self, index):
        return index*2
    
    def rightchild(self, index):
        return index*2 + 1

# main
Hp = Heap()
keyNum = int(input())
command = input().split()
#Hp.last_index = len(command)
Hp.last_index = keyNum
for i in range(1, Hp.last_index+1):
    Hp.queue[i] = (int(command[i-1]))
    
Hp.inPlaceHeapSort()
Hp.printHeap()
