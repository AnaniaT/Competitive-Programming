class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
      hkS = []
      lhalf = []
      ghalf = []
      for n in nums:
        if n == k/2: hkS.append(n)
        elif n < k/2: lhalf.append(n)
        elif n > k/2 and n < k: ghalf.append(n)
      
      ans = len(hkS) // 2

      lhalf.sort()
      ghalf.sort(reverse=True)

      for n in lhalf:
        for m in ghalf:
          if n+m < k: break
          if n+m == k: 
            ans += 1
            ghalf.remove(m)
            break
      
      return ans
