#Problem: https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def select(self, arr, i):
        # This is irrelevant for this question
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minI = i
            for j in range(i+1, n):
                if arr[j] < arr[minI]:
                    minI = j
            arr[i], arr[minI] = arr[minI], arr[i]
        
        return arr
      
