# 상향식 힙 생성
# (비재귀적), 시간복잡도 O(n)
# 힙
class Heap:
    def __init__(self):
        self.queue = [0] * 100
        self.queue[0] = None
        self.last_index = 0
        # 리스트의 0번째 자리에 None 루트의 인덱스 번호를 1로 하기 위해
    
    def buildHeap(self):
        for i in range(self.last_index//2, 0, -1):
            self.downHeap(i)
        return
    
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
Hp = Heap()
keycount = int(input())
Hp.last_index = keycount
command = input().split()
for i in range(1, keycount+1):
    Hp.queue[i] = (int(command[i-1]))
Hp.buildHeap()
Hp.printHeap()

