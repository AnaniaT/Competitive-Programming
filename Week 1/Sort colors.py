class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
          m = nums[i]
          for j in range(len(nums[i+1:])):
            if nums[i+1+j] < m:
              m = nums[i+1+j]
              nums[i+1+j], nums[i] = nums[i], nums[i+1+j]
