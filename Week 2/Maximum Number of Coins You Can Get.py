class Solution:
    def maxCoins(self, piles: List[int]) -> int:
      piles.sort(reverse=True)
      s = 0
      for i in range(len(piles)//3):
        s += piles[2*i+1]
      
      return s
