# Problem: https://www.hackerrank.com/challenges/insertionsort1

def insertionSort1(n, arr):
    i = arr[n-1]
    for j in range(n-2,-1, -1):
        if(i < arr[j]):
            arr[j+1] = arr[j]
        else:
            arr[j+1] = i
        [print(i, end=' ') for i in arr]
        print()
