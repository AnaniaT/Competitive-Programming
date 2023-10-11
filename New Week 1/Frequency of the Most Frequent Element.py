class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        m = i = tot = 0
        
        for j in range(len(nums)):
          tot += nums[j]
          while nums[j]*(j-i+1) > tot+k:
            tot -= nums[i]
            i += 1
                                 
          c = j-i+1
          if c > m:
            m = c
        
        return m

        
