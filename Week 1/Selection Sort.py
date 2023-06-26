#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        m = (float('inf'), None)
        for j in range(len(arr[i:])):
            if arr[i+j] < m[0]:
                m[0] = arr[i+j]
                m[1] = i+j
            
        return m
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minVal, j = self.select(arr, i)
            arr[i], arr[j] = minVal, arr[i]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
