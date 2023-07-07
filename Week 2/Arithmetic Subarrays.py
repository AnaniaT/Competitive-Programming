class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
      ans = []
      for x in range(len(l)):
        n = r[x] + 1 - l[x]
        arr = nums[l[x]:r[x]+1]
        arr.sort()
        d = None
        val = True
        for i in range(n-1):
          if d == None:
            d = arr[i+1] - arr[i]
          elif arr[i+1] - arr[i] != d:
            val = False
            break
        ans.append(val)
      
      return ans

