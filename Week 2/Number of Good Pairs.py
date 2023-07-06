class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      a = 0
      dup = filter(lambda x: nums.count(x) > 1, nums)
      for n in map(lambda x: nums.count(x), set(dup)):
        a += n*(n-1)/2
      return int(a)
