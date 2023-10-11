class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
      w = len(changed)
      if w % 2 != 0:
        return []

      changed.sort()
      ans = []
      r = w-1
      l = r-1
      while l >= 0:
        if changed[r] == -1:
          r -= 1
          continue
        if r == l:
          l -= 1

        if changed[r] / 2 == changed[l]:
          ans.append(changed[l])
          changed[l] = -1
          r -= 1
        elif changed[r] / 2 > changed[l]:
          return []
        l -= 1
      if len(changed)/2 != len(ans):
        return []
      return ans
