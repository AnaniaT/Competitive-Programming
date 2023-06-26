class Solution:
    def sortSentence(self, s: str) -> str:
      s= s.split()
      arr = ['']*len(s)
      for i in range(len(s)):
        j = int(s[i][-1])
        arr[j-1] = s[i][:-1]
      
      return ' '.join(arr)
