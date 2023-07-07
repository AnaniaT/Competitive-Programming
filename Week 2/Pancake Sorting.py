class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:      
      j = len(arr)
      ans = []
      for i in range(len(arr)-1):
        mai = arr.index(j)
        if mai != j-1:
          k = mai+1
          arr[:k] = arr[::-1][-k:]
          arr[:j] = arr[::-1][-j:]
          ans.append(k)
          ans.append(j)
        j -= 1
      
      return ans
      
      
