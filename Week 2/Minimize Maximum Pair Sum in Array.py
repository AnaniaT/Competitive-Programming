class Solution:
    def minPairSum(self, nums: List[int]) -> int:
      nums.sort()
      m = nums[0] + nums[-1]
      for i in range(len(nums)//2):
        m = max(m, nums[i] + nums[-1-i])
      
      return m
