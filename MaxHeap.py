# 삽입식 힙 생성
# 최대힙 MaxHeap - 가장 큰 값이 루트에

#힙
class Heap:
    def __init__(self):
        self.queue = [0] * 100
        self.queue[0] = None
        self.last_index = 0
        # 리스트의 0번째 자리에 None 루트의 인덱스 번호를 1로 하기 위해
    
    def insert(self, n):
        # 일단 맨 마지막에 삽입할 원소 임시 추가
        self.last_index += 1
        self.queue[self.last_index] = n
        self.upHeap(self.last_index)
        
    # 부모를 타고 올라가면서 비교    
    def upHeap(self, i):
        parent_index= self.parent(i)
        if i == 1:
            return
        elif self.queue[i] <= self.queue[parent_index]:
            return
        else:
            self.swapElements(i, parent_index)
            self.upHeap(parent_index)
    
    def removeMax(self):
        key = self.queue[1]
        if self.last_index < 1:
            return
        self.swapElements(1, self.last_index)
        key = self.queue[self.last_index]
        self.queue[self.last_index] = 0
        self.downHeap(1)
        self.last_index -= 1
        print(key)
        return key
    
    def downHeap(self, i):
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
        self.downHeap(bigger)
        
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
# 입력
Hp = Heap()
while True:
    command = input().split()
    if command[0] == 'i':
        Hp.insert(int(command[1]))
        print(0)
    elif command[0] == 'd':
        Hp.removeMax()
    elif command[0] == 'p':
        Hp.printHeap()
    elif command[0] == 'q':
        break           