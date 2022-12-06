#제자리 삽입 정렬
def inPlaceInsertSort(arr):
    for i in range(1,len(arr)):
        save = arr[i]
        j = i-1
        while(j>=0 and arr[j]>save):
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = save

# main
n = int(input())
arr = [0] * n
s = input().split()

for i in range(n):
    arr[i] = int(s[i])

inPlaceInsertSort(arr)

print(" ", end='')
for l in arr:
        print(l, end=' ')