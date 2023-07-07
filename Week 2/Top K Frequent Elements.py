from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      freq = Counter(nums)
      return [el for el, f in freq.most_common(k)]
