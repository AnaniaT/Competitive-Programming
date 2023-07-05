from statistics import median
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
      m = median(nums)
      arr = filter(lambda x: x<m, nums)
      arr2 = filter(lambda x: x>=m, nums)
      ans = [0]*len(nums)
      ans[::2] = arr2
      ans[1::2] = arr

      return ans
