import functools
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
      def comp(n1: str, n2: str) -> int:
        l1 = len(n1)
        l2 = len(n2)
        if l1 > l2:
          return -1
        elif l1 < l2:
          return 1
        else:
          for i in range(l1):
            if int(n1[i]) > int(n2[i]): return -1
            elif int(n1[i]) < int(n2[i]): return 1
          return 0

      nums.sort(key=functools.cmp_to_key(comp))
      return nums[k-1]
