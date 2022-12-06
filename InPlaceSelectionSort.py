# 제자리 선택 정렬
def inPlaceSelectionSort(arr):
    for i in range(len(arr)-1):
        minLoc = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minLoc]:
                minLoc = j   
        temp = arr[i]
        arr[i] = arr[minLoc]
        arr[minLoc] = temp
        
# main
n = int(input())
arr = [0] * n
s = input().split()

for i in range(n):
    arr[i] = int(s[i])

inPlaceSelectionSort(arr)

print(" ", end='')
for l in arr:
        print(l, end=' ')

