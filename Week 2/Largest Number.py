import functools

class Solution:
    def largestNumber(self, nums):
      if not any(nums):
          return "0"
      
      def myComp(n1: str, n2: str) -> int:
        if n1+n2 > n2+n1: return -1
        if n1+n2 < n2+n1: return 1
        return 0

      nums = map(str, nums)
      return "".join(sorted(nums, key=functools.cmp_to_key(myComp)))
