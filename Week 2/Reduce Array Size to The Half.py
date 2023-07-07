from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
      freq = Counter(arr)
      c = 0
      res = 0

      for k, v in freq.most_common():
        c += v
        res += 1
        if c >= len(arr)//2:
          break

      return res
